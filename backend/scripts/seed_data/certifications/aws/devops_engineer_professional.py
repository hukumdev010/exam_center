"""AWS DevOps Engineer Professional Certification"""

CERTIFICATION = {
    "name": "AWS Certified DevOps Engineer - Professional",
    "description": "Implement and manage continuous delivery systems and methodologies on AWS",
    "slug": "aws-devops-engineer-professional",
    "level": "Professional",
    "duration": 180,
    "questions_count": 75,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which AWS service provides infrastructure as code?",
        "explanation": "AWS CloudFormation provides a common language for you to model and provision AWS and third party application resources in your cloud environment. CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts.",
        "reference": "https://docs.aws.amazon.com/cloudformation/",
        "points": 1,
        "answers": [
            {"text": "AWS CloudFormation", "is_correct": True},
            {"text": "AWS Lambda", "is_correct": False},
            {"text": "Amazon EC2", "is_correct": False},
            {"text": "AWS S3", "is_correct": False}
        ]
    },
    {
        "text": "What is AWS CodePipeline used for?",
        "explanation": "AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.",
        "reference": "https://docs.aws.amazon.com/codepipeline/",
        "points": 1,
        "answers": [
            {"text": "Continuous integration and delivery", "is_correct": True},
            {"text": "Code storage", "is_correct": False},
            {"text": "Load balancing", "is_correct": False},
            {"text": "Database management", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides managed Git repositories?",
        "explanation": "AWS CodeCommit is a fully-managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem.",
        "reference": "https://docs.aws.amazon.com/codecommit/",
        "points": 1,
        "answers": [
            {"text": "AWS CodeCommit", "is_correct": True},
            {"text": "AWS CodeBuild", "is_correct": False},
            {"text": "AWS CodeDeploy", "is_correct": False},
            {"text": "AWS CodePipeline", "is_correct": False}
        ]
    },
    {
        "text": "What is AWS CodeBuild primarily used for?",
        "explanation": "AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.",
        "reference": "https://docs.aws.amazon.com/codebuild/",
        "points": 1,
        "answers": [
            {"text": "Building and testing code", "is_correct": True},
            {"text": "Deploying applications", "is_correct": False},
            {"text": "Storing source code", "is_correct": False},
            {"text": "Monitoring applications", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service automates application deployments?",
        "explanation": "AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers.",
        "reference": "https://docs.aws.amazon.com/codedeploy/",
        "points": 1,
        "answers": [
            {"text": "AWS CodeDeploy", "is_correct": True},
            {"text": "AWS CodeCommit", "is_correct": False},
            {"text": "AWS CodeBuild", "is_correct": False},
            {"text": "AWS CloudFormation", "is_correct": False}
        ]
    }
]
