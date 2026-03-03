# Exam Center Database Seeding System

This directory contains an organized seeding system for the exam center database with comprehensive certification data.

## 📁 Structure

```
seed_data/
├── categories.py          # Base categories definition
├── certifications/        # Individual certification files
│   ├── aws.py            # AWS certifications (11 certs)
│   ├── azure.py          # Microsoft Azure certifications (10 certs)
│   ├── google_cloud.py   # Google Cloud Platform certifications (9 certs)
│   ├── devops.py         # DevOps & Infrastructure certifications (8 certs)
│   ├── programming.py    # Programming languages certifications (10 certs)
│   ├── cybersecurity.py  # Security certifications (8 certs)
│   ├── data_analytics.py # Data Science & Analytics certifications (7 certs)
│   ├── project_management.py # Project Management certifications (6 certs)
│   ├── networking.py     # Networking certifications (5 certs)
│   └── database.py       # Database certifications (6 certs)
```

## 🎯 Total Content

- **📁 10 Categories**: AWS, Azure, Google Cloud, DevOps, Programming, Cybersecurity, Data & Analytics, Project Management, Networking, Database
- **📜 80+ Certifications**: Comprehensive coverage of industry-standard certifications
- **❓ 25+ Sample Questions**: Real-world questions with explanations and references
- **✅ 100+ Answer Options**: Multiple choice answers for each question

## 🚀 Usage

### Run the Complete Seed

```bash
# Activate virtual environment
source venv/bin/activate

# Run the comprehensive seed
python scripts/seed_new.py
```

### Count Certifications

```bash
# Get detailed statistics
python scripts/count_certifications.py
```

### Legacy Seed (Original)

```bash
# Run the original seed (for comparison)
python scripts/seed.py
```

## 📋 Certification Categories

### 1. AWS (11 certifications)
- Cloud Practitioner (Foundational)
- Solutions Architect Associate/Professional
- Developer Associate
- SysOps Administrator Associate
- DevOps Engineer Professional
- Security, ML, Database, Networking, Data Analytics Specialties

### 2. Azure (10 certifications)
- Fundamentals
- Solutions Architect Expert
- Developer/Administrator Associates
- Security Engineer, DevOps Engineer
- Data Scientist, Data Engineer, Database Administrator
- AI Engineer Associates

### 3. Google Cloud (9 certifications)
- Digital Leader
- Associate Cloud Engineer
- Professional Cloud Architect
- Professional Data Engineer, Developer, DevOps Engineer
- Professional Security, Network, ML Engineers

### 4. DevOps (8 certifications)
- Docker Certified Associate
- Kubernetes Administrator (CKA)
- Kubernetes Application Developer (CKAD)
- Terraform Associate
- Jenkins Engineer
- GitLab CI/CD Specialist
- Ansible Automation Platform Specialist
- Prometheus Certified Associate

### 5. Programming (10 certifications)
- Python (PCEP, PCAP)
- Java SE 11 (Programmer I & II)
- JavaScript, React, Node.js
- C#, Go, Rust

### 6. Cybersecurity (8 certifications)
- CompTIA Security+
- CISSP
- Certified Ethical Hacker (CEH)
- CompTIA CySA+, PenTest+
- CISM, CISA
- GIAC Security Essentials (GSEC)

### 7. Data & Analytics (7 certifications)
- Google Data Analytics Professional
- Azure Data Scientist Associate
- Tableau Desktop Specialist
- SAS Statistical Business Analyst
- IBM Data Science Professional
- Databricks Certified Data Analyst
- Snowflake SnowPro Core

### 8. Project Management (6 certifications)
- PMP (Project Management Professional)
- CAPM (Certified Associate)
- Certified ScrumMaster (CSM)
- Professional Scrum Master I (PSM I)
- Certified Scrum Product Owner (CSPO)
- SAFe Agilist

### 9. Networking (5 certifications)
- Cisco CCNA/CCNP
- CompTIA Network+
- Juniper JNCIA
- CISSP Network Security

### 10. Database (6 certifications)
- Oracle MySQL DBA
- Azure Database Administrator
- Oracle Database SQL Associate
- MongoDB Certified Developer
- PostgreSQL Certified Professional
- IBM DB2 Administrator

## 🔧 Adding New Certifications

1. **Add to existing category**: Edit the relevant file in `certifications/`
2. **Create new category**: 
   - Add to `categories.py`
   - Create new certification file
   - Update imports in `seed_new.py`

## 📝 Question Format

Each certification can have sample questions with this structure:

```python
QUESTIONS = {
    "certification-slug": [
        {
            "text": "Question text?",
            "explanation": "Detailed explanation of the answer",
            "reference": "https://documentation-url",
            "points": 1,
            "answers": [
                {"text": "Option A", "is_correct": False},
                {"text": "Option B", "is_correct": True},
                {"text": "Option C", "is_correct": False},
                {"text": "Option D", "is_correct": False}
            ]
        }
    ]
}
```

## 🎯 Benefits of This System

1. **Organized**: Each certification category has its own file
2. **Scalable**: Easy to add new certifications and questions
3. **Maintainable**: Clear separation of concerns
4. **Comprehensive**: 80+ real-world certifications
5. **Professional**: Industry-standard certifications from major providers
6. **Educational**: Questions include explanations and references

## 🚀 Next Steps

1. Add more sample questions to existing certifications
2. Include practice exams with full question sets
3. Add certification prerequisites and learning paths
4. Implement difficulty levels and adaptive testing
5. Add certification expiration dates and renewal requirements
