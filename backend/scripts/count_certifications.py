#!/usr/bin/env python3
"""Count total certifications in the seed data"""

from seed_data.certifications import aws, azure, google_cloud, devops, programming, cybersecurity, data_analytics, project_management, networking, database

CERTIFICATION_MODULES = [
    aws, azure, google_cloud, devops, programming, 
    cybersecurity, data_analytics, project_management, networking, database
]

def count_certifications():
    """Count and display certification statistics"""
    print("🔢 CERTIFICATION STATISTICS")
    print("=" * 50)
    
    total_certifications = 0
    total_questions = 0
    
    for module in CERTIFICATION_MODULES:
        module_name = module.__name__.split('.')[-1].replace('_', ' ').title()
        cert_count = len(module.CERTIFICATIONS)
        total_certifications += cert_count
        
        # Count questions if available
        question_count = 0
        if hasattr(module, 'QUESTIONS'):
            for cert_slug, questions in module.QUESTIONS.items():
                question_count += len(questions)
        total_questions += question_count
        
        print(f"📋 {module_name}: {cert_count} certifications, {question_count} sample questions")
    
    print("=" * 50)
    print(f"🎯 TOTAL: {total_certifications} certifications with {total_questions} sample questions")
    print("=" * 50)
    
    # Check if we have 30+ certifications
    if total_certifications >= 30:
        print(f"✅ SUCCESS: We have {total_certifications} certifications (30+ requirement met!)")
    else:
        print(f"❌ Need more: Only {total_certifications} certifications (need 30+)")

if __name__ == "__main__":
    count_certifications()
