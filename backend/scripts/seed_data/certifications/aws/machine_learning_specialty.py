"""AWS Machine Learning Specialty Certification"""

CERTIFICATION = {
    "name": "AWS Certified Machine Learning - Specialty",
    "description": "Design, implement, deploy, and maintain machine learning solutions for given business problems",
    "slug": "aws-machine-learning-specialty",
    "level": "Specialty",
    "duration": 180,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service provides pre-built machine learning models via APIs?",
        "explanation": "Amazon Rekognition, Amazon Comprehend, Amazon Polly, Amazon Lex, and other AI services provide pre-built machine learning capabilities via simple APIs that don't require machine learning expertise.",
        "reference": "https://aws.amazon.com/machine-learning/ai-services/",
        "points": 1,
        "answers": [
            {"text": "Amazon AI Services (Rekognition, Comprehend, etc.)", "is_correct": True},
            {"text": "Amazon SageMaker", "is_correct": False},
            {"text": "AWS Lambda", "is_correct": False},
            {"text": "Amazon EC2", "is_correct": False}
        ]
    },
    {
        "text": "What is Amazon SageMaker primarily used for?",
        "explanation": "Amazon SageMaker is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly.",
        "reference": "https://docs.aws.amazon.com/sagemaker/",
        "points": 1,
        "answers": [
            {"text": "Building, training, and deploying ML models", "is_correct": True},
            {"text": "Data storage only", "is_correct": False},
            {"text": "Web hosting", "is_correct": False},
            {"text": "Database management", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides automatic speech recognition?",
        "explanation": "Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications.",
        "reference": "https://docs.aws.amazon.com/transcribe/",
        "points": 1,
        "answers": [
            {"text": "Amazon Transcribe", "is_correct": True},
            {"text": "Amazon Polly", "is_correct": False},
            {"text": "Amazon Lex", "is_correct": False},
            {"text": "Amazon Comprehend", "is_correct": False}
        ]
    },
    {
        "text": "What does Amazon Comprehend provide?",
        "explanation": "Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text.",
        "reference": "https://docs.aws.amazon.com/comprehend/",
        "points": 1,
        "answers": [
            {"text": "Natural language processing and text analytics", "is_correct": True},
            {"text": "Image recognition", "is_correct": False},
            {"text": "Speech synthesis", "is_correct": False},
            {"text": "Video analysis", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service is used for building conversational interfaces?",
        "explanation": "Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text.",
        "reference": "https://docs.aws.amazon.com/lex/",
        "points": 1,
        "answers": [
            {"text": "Amazon Lex", "is_correct": True},
            {"text": "Amazon Polly", "is_correct": False},
            {"text": "Amazon Transcribe", "is_correct": False},
            {"text": "Amazon Translate", "is_correct": False}
        ]
    }
]
