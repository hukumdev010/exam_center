import uuid
import os
from datetime import datetime
from typing import Optional, List
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor
from reportlab.lib import colors

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import (
    Certificate as CertificateModel,
    User,
    Certification,
    Category
)


class CertificateService:
    def __init__(self):
        self.certificates_dir = os.path.join(os.getcwd(), "certificates")
        os.makedirs(self.certificates_dir, exist_ok=True)

    async def generate_certificate_pdf(
        self,
        db: AsyncSession,
        certificate: CertificateModel,
        user: User,
        certification: Certification,
        category: Category
    ) -> str:
        """Generate PDF certificate and return the filename"""
        
        # Create filename
        safe_cert_name = "".join(
            c for c in certification.name
            if c.isalnum() or c in (' ', '-', '_')
        ).rstrip()
        safe_cert_name = safe_cert_name.replace(' ', '_')
        filename = f"certificate_{certificate.id}_{safe_cert_name}.pdf"
        filepath = os.path.join(self.certificates_dir, filename)

        # Create PDF
        doc = SimpleDocTemplate(filepath, pagesize=A4)
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,  # Center alignment
            textColor=HexColor('#2563eb')
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=18,
            spaceAfter=20,
            alignment=1,
            textColor=HexColor('#1e40af')
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=12,
            alignment=1,
            textColor=colors.black
        )
        
        name_style = ParagraphStyle(
            'NameStyle',
            parent=styles['Normal'],
            fontSize=20,
            spaceAfter=20,
            alignment=1,
            textColor=HexColor('#059669'),
            fontName='Helvetica-Bold'
        )

        # Content
        content = []
        
        # Header
        content.append(Paragraph("CERTIFICATE OF COMPLETION", title_style))
        content.append(Spacer(1, 20))
        
        # This certifies that
        content.append(Paragraph("This is to certify that", body_style))
        content.append(Spacer(1, 15))
        
        # User name
        user_display_name = user.name or user.email
        content.append(Paragraph(user_display_name, name_style))
        content.append(Spacer(1, 15))
        
        # Has successfully completed
        completion_text = "has successfully completed the certification exam for"
        content.append(Paragraph(completion_text, body_style))
        content.append(Spacer(1, 15))
        
        # Certification name
        content.append(Paragraph(certification.name, subtitle_style))
        content.append(Spacer(1, 10))
        
        # Category
        content.append(Paragraph(f"in {category.name}", body_style))
        content.append(Spacer(1, 20))
        
        # Score details
        correct_answers = (
            certificate.score * certificate.total_questions // 100
        )
        score_text = (
            f"Score achieved: {certificate.score}% "
            f"({correct_answers} out of {certificate.total_questions} questions)"
        )
        content.append(Paragraph(score_text, body_style))
        content.append(Spacer(1, 20))
        
        # Date
        issued_date = certificate.issued_at.strftime("%B %d, %Y")
        content.append(Paragraph(f"Issued on: {issued_date}", body_style))
        content.append(Spacer(1, 30))
        
        # Footer
        platform_text = "ExamCenter Certification Platform"
        content.append(Paragraph(platform_text, body_style))
        
        cert_id_style = ParagraphStyle(
            'CertId',
            parent=styles['Normal'],
            fontSize=8,
            alignment=1,
            textColor=colors.grey
        )
        content.append(
            Paragraph(f"Certificate ID: {certificate.id}", cert_id_style)
        )

        # Build PDF
        doc.build(content)
        
        return filename

    async def create_certificate(
        self,
        db: AsyncSession,
        user_id: str,
        quiz_attempt_id: str,
        certification_id: int,
        score: int,
        total_questions: int
    ) -> Optional[CertificateModel]:
        """Create a certificate for a completed quiz"""
        
        # Check if certificate already exists
        existing_cert = await db.execute(
            select(CertificateModel).where(
                CertificateModel.quiz_attempt_id == quiz_attempt_id
            )
        )
        if existing_cert.scalar_one_or_none():
            return None  # Certificate already exists
        
        # Only create certificate if score is 80% or higher
        if score < 80:
            return None
        
        # Get user, certification, and category info
        user_stmt = select(User).where(User.id == user_id)
        user_result = await db.execute(user_stmt)
        user = user_result.scalar_one_or_none()
        
        cert_stmt = (
            select(Certification)
            .options(selectinload(Certification.category))
            .where(Certification.id == certification_id)
        )
        cert_result = await db.execute(cert_stmt)
        certification = cert_result.scalar_one_or_none()
        
        if not user or not certification:
            return None
        
        # Create certificate record
        certificate_id = str(uuid.uuid4())
        certificate = CertificateModel(
            id=certificate_id,
            user_id=user_id,
            quiz_attempt_id=quiz_attempt_id,
            certification_id=certification_id,
            score=score,
            total_questions=total_questions,
            issued_at=datetime.utcnow()
        )
        
        db.add(certificate)
        await db.flush()  # Get the ID
        
        # Generate PDF
        try:
            pdf_filename = await self.generate_certificate_pdf(
                db, certificate, user, certification, certification.category
            )
            certificate.pdf_filename = pdf_filename
            await db.commit()
            await db.refresh(certificate)
            return certificate
        except Exception as e:
            await db.rollback()
            raise e

    async def get_user_certificates(
        self,
        db: AsyncSession,
        user_id: str
    ) -> List[CertificateModel]:
        """Get all certificates for a user"""
        
        stmt = (
            select(CertificateModel)
            .options(
                selectinload(CertificateModel.certification)
                .selectinload(Certification.category)
            )
            .where(CertificateModel.user_id == user_id)
            .order_by(CertificateModel.issued_at.desc())
        )
        
        result = await db.execute(stmt)
        return result.scalars().all()

    async def get_certificate_pdf(
        self,
        db: AsyncSession,
        certificate_id: str,
        user_id: str
    ) -> Optional[bytes]:
        """Get certificate PDF content"""
        
        # Get certificate
        stmt = select(CertificateModel).where(
            CertificateModel.id == certificate_id,
            CertificateModel.user_id == user_id
        )
        result = await db.execute(stmt)
        certificate = result.scalar_one_or_none()
        
        if not certificate or not certificate.pdf_filename:
            return None
        
        filepath = os.path.join(self.certificates_dir, certificate.pdf_filename)
        
        try:
            with open(filepath, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return None

    async def delete_certificate(
        self, 
        db: AsyncSession, 
        certificate_id: str, 
        user_id: str
    ) -> bool:
        """Delete a certificate and its PDF file"""
        
        # Get certificate
        stmt = select(CertificateModel).where(
            CertificateModel.id == certificate_id,
            CertificateModel.user_id == user_id
        )
        result = await db.execute(stmt)
        certificate = result.scalar_one_or_none()
        
        if not certificate:
            return False
        
        # Delete PDF file if it exists
        if certificate.pdf_filename:
            filepath = os.path.join(self.certificates_dir, certificate.pdf_filename)
            try:
                os.remove(filepath)
            except FileNotFoundError:
                pass  # File already deleted
        
        # Delete from database
        await db.delete(certificate)
        await db.commit()
        return True