from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CertificateCreate(BaseModel):
    quiz_attempt_id: str
    certification_id: int
    score: int


class Certificate(BaseModel):
    id: str
    user_id: str
    quiz_attempt_id: str
    certification_id: int
    certification_name: str
    category_name: str
    user_name: Optional[str]
    user_email: str
    score: int
    total_questions: int
    issued_at: datetime
    pdf_filename: Optional[str]
    
    class Config:
        from_attributes = True


class CertificateDownloadResponse(BaseModel):
    filename: str
    content_type: str
    file_data: bytes