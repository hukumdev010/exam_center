"""Azure AI Engineer Associate Certification"""

CERTIFICATION = {
    "name": "Azure AI Engineer Associate",
    "description": "Design and implement AI solutions on Azure",
    "slug": "azure-ai-engineer-associate-ai102",
    "level": "Associate",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "azure",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which Azure service provides pre-built AI models for common scenarios like sentiment analysis and language detection?",
        "explanation": "Azure Cognitive Services provides pre-built AI models that can be easily integrated into applications without requiring machine learning expertise. It includes Text Analytics for sentiment analysis and language detection.",
        "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/",
        "points": 1,
        "answers": [
            {"text": "Azure Machine Learning", "is_correct": False},
            {"text": "Azure Cognitive Services", "is_correct": True},
            {"text": "Azure Databricks", "is_correct": False},
            {"text": "Azure Synapse Analytics", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Azure Bot Framework?",
        "explanation": "Azure Bot Framework is a comprehensive offering to build and deploy high-quality bots for your users to enjoy wherever they are talking. It provides tools and services for building conversational AI experiences.",
        "reference": "https://docs.microsoft.com/en-us/azure/bot-service/",
        "points": 1,
        "answers": [
            {"text": "To analyze big data", "is_correct": False},
            {"text": "To build conversational AI applications", "is_correct": True},
            {"text": "To create virtual networks", "is_correct": False},
            {"text": "To manage container orchestration", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service is used for computer vision tasks like object detection and image classification?",
        "explanation": "Azure Computer Vision is part of Azure Cognitive Services and provides algorithms to process images and return information about visual content, including object detection, image classification, and OCR capabilities.",
        "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/",
        "points": 1,
        "answers": [
            {"text": "Azure Custom Vision", "is_correct": False},
            {"text": "Azure Computer Vision", "is_correct": True},
            {"text": "Azure Face API", "is_correct": False},
            {"text": "Azure Form Recognizer", "is_correct": False},
        ],
    },
    {
        "text": "What is Azure Language Understanding (LUIS) primarily used for?",
        "explanation": "LUIS (Language Understanding Intelligent Service) is used to build natural language understanding into applications. It helps applications understand user intents and extract entities from conversational text.",
        "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/luis/",
        "points": 1,
        "answers": [
            {"text": "Image recognition", "is_correct": False},
            {"text": "Natural language understanding", "is_correct": True},
            {"text": "Speech synthesis", "is_correct": False},
            {"text": "Document translation", "is_correct": False},
        ],
    },
    {
        "text": "Which Azure service provides speech-to-text and text-to-speech capabilities?",
        "explanation": "Azure Speech Services provides speech-to-text (speech recognition), text-to-speech (speech synthesis), speech translation, and speaker recognition capabilities through REST APIs and SDKs.",
        "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/",
        "points": 1,
        "answers": [
            {"text": "Azure Language Understanding", "is_correct": False},
            {"text": "Azure Speech Services", "is_correct": True},
            {"text": "Azure Text Analytics", "is_correct": False},
            {"text": "Azure Translator", "is_correct": False},
        ],
    },
]
