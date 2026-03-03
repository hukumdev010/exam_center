from datetime import datetime, timedelta

TEST_TEACHERS = [
    {
        "user": {
            "id": "test_teacher_1",
            "name": "Dr. Sarah Johnson (TEST TEACHER)",
            "email": "sarah.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=1",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - AWS expert with 8 years experience",
            "experience_years": 8,
            "hourly_rate_one_on_one": 75.0,
            "hourly_rate_group": 45.0,
            "max_group_size": 8,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Spanish"]',
            "timezone": "America/New_York",
            "approved_at": datetime.now() - timedelta(days=30),
        },
        "qualifications": [
            {
                "category_slug": "aws",
                "certification_slug": "aws-solutions-architect-associate",
                "score_percentage": 95.0,
            },
            {
                "category_slug": "system-design",
                "certification_slug": "system-design-fundamentals",
                "score_percentage": 92.0,
            },
            {
                "category_slug": "frontend",
                "certification_slug": "frontend-react-fundamentals",
                "score_percentage": 90.0,
            }
        ]
    },
    {
        "user": {
            "id": "test_teacher_2",
            "name": "Prof. Michael Chen (TEST TEACHER)",
            "email": "michael.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=2",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Azure expert with 10+ years",
            "experience_years": 12,
            "hourly_rate_one_on_one": 85.0,
            "hourly_rate_group": 50.0,
            "max_group_size": 10,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Mandarin"]',
            "timezone": "America/Los_Angeles",
            "approved_at": datetime.now() - timedelta(days=45),
        },
        "qualifications": [
            {
                "category_slug": "azure",
                "certification_slug": "az-900-azure-fundamentals",
                "score_percentage": 98.0,
            }
        ]
    },
    {
        "user": {
            "id": "test_teacher_3",
            "name": "Dr. Emma Wilson (TEST TEACHER)",
            "email": "emma.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=3",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Python and AI/ML specialist with 6 years experience",
            "experience_years": 6,
            "hourly_rate_one_on_one": 70.0,
            "hourly_rate_group": 40.0,
            "max_group_size": 12,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "French"]',
            "timezone": "Europe/London",
            "approved_at": datetime.now() - timedelta(days=20),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_4",
            "name": "Prof. David Rodriguez (TEST TEACHER)",
            "email": "david.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=4",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Cybersecurity expert with 15 years experience",
            "experience_years": 15,
            "hourly_rate_one_on_one": 95.0,
            "hourly_rate_group": 65.0,
            "max_group_size": 6,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Spanish"]',
            "timezone": "America/Chicago",
            "approved_at": datetime.now() - timedelta(days=60),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_5",
            "name": "Dr. Lisa Park (TEST TEACHER)",
            "email": "lisa.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=5",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Google Cloud Platform specialist with 7 years experience",
            "experience_years": 7,
            "hourly_rate_one_on_one": 80.0,
            "hourly_rate_group": 45.0,
            "max_group_size": 10,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Korean"]',
            "timezone": "America/Los_Angeles",
            "approved_at": datetime.now() - timedelta(days=25),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_6",
            "name": "Prof. Ahmed Hassan (TEST TEACHER)",
            "email": "ahmed.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=6",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - DevOps and Docker specialist with 9 years experience",
            "experience_years": 9,
            "hourly_rate_one_on_one": 75.0,
            "hourly_rate_group": 50.0,
            "max_group_size": 8,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Arabic"]',
            "timezone": "Europe/Berlin",
            "approved_at": datetime.now() - timedelta(days=35),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_7",
            "name": "Dr. Rachel Green (TEST TEACHER)",
            "email": "rachel.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=7",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Java and Spring Boot expert with 11 years experience",
            "experience_years": 11,
            "hourly_rate_one_on_one": 85.0,
            "hourly_rate_group": 55.0,
            "max_group_size": 9,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English"]',
            "timezone": "America/New_York",
            "approved_at": datetime.now() - timedelta(days=40),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_8",
            "name": "Prof. Hiroshi Tanaka (TEST TEACHER)",
            "email": "hiroshi.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=8",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - React and JavaScript specialist with 5 years experience",
            "experience_years": 5,
            "hourly_rate_one_on_one": 65.0,
            "hourly_rate_group": 35.0,
            "max_group_size": 15,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Japanese"]',
            "timezone": "Asia/Tokyo",
            "approved_at": datetime.now() - timedelta(days=15),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_9",
            "name": "Dr. Maria Santos (TEST TEACHER)",
            "email": "maria.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=9",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Database and SQL specialist with 8 years experience",
            "experience_years": 8,
            "hourly_rate_one_on_one": 75.0,
            "hourly_rate_group": 45.0,
            "max_group_size": 10,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Portuguese", "Spanish"]',
            "timezone": "America/Sao_Paulo",
            "approved_at": datetime.now() - timedelta(days=50),
        },
        "qualifications": []
    },
    {
        "user": {
            "id": "test_teacher_10",
            "name": "Prof. James Smith (TEST TEACHER)",
            "email": "james.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=10",
            "password": "teacher123",
        },
        "profile": {
            "bio": "TEST TEACHER - Full-stack development specialist with 12 years experience",
            "experience_years": 12,
            "hourly_rate_one_on_one": 90.0,
            "hourly_rate_group": 60.0,
            "max_group_size": 8,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English"]',
            "timezone": "Australia/Sydney",
            "approved_at": datetime.now() - timedelta(days=70),
        },
        "qualifications": []
    }
]


# Test students data
TEST_STUDENTS = [
    {
        "id": "test_student_1",
        "name": "Alice Johnson (TEST STUDENT)",
        "email": "alice.student@examcenter.com",
        "password": "student123",
        "email_verified": datetime.now(),
        "image": "https://i.pravatar.cc/150?img=11",
    },
    {
        "id": "test_student_2",
        "name": "Bob Smith (TEST STUDENT)",
        "email": "bob.student@examcenter.com",
        "password": "student123",
        "email_verified": datetime.now(),
        "image": "https://i.pravatar.cc/150?img=12",
    },
    {
        "id": "test_student_3",
        "name": "Carol Williams (TEST STUDENT)",
        "email": "carol.student@examcenter.com",
        "password": "student123",
        "email_verified": datetime.now(),
        "image": "https://i.pravatar.cc/150?img=13",
    },
    {
        "id": "test_student_4",
        "name": "David Brown (TEST STUDENT)",
        "email": "david.student@examcenter.com",
        "password": "student123",
        "email_verified": datetime.now(),
        "image": "https://i.pravatar.cc/150?img=14",
    },
    {
        "id": "test_student_5",
        "name": "Eva Davis (TEST STUDENT)",
        "email": "eva.student@examcenter.com",
        "password": "student123",
        "email_verified": datetime.now(),
        "image": "https://i.pravatar.cc/150?img=15",
    }
]
