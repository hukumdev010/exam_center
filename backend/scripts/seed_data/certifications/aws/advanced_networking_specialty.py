"""AWS Advanced Networking Specialty Certification"""

CERTIFICATION = {
    "name": "AWS Certified Advanced Networking - Specialty",
    "description": "Design and maintain network architecture for all AWS services",
    "slug": "aws-advanced-networking-specialty",
    "level": "Specialty",
    "duration": 170,
    "questions_count": 65,
    "category_slug": "aws",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is AWS Direct Connect used for?",
        "explanation": "AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment.",
        "reference": "https://docs.aws.amazon.com/directconnect/",
        "points": 1,
        "answers": [
            {"text": "Dedicated network connection to AWS", "is_correct": True},
            {"text": "Content delivery network", "is_correct": False},
            {"text": "Load balancing", "is_correct": False},
            {"text": "DNS management", "is_correct": False}
        ]
    },
    {
        "text": "Which AWS service provides DNS management?",
        "explanation": "Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications.",
        "reference": "https://docs.aws.amazon.com/route53/",
        "points": 1,
        "answers": [
            {"text": "Amazon Route 53", "is_correct": True},
            {"text": "AWS CloudFront", "is_correct": False},
            {"text": "Elastic Load Balancing", "is_correct": False},
            {"text": "AWS Direct Connect", "is_correct": False}
        ]
    },
    {
        "text": "What is a VPC endpoint used for?",
        "explanation": "A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.",
        "reference": "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html",
        "points": 1,
        "answers": [
            {"text": "Private connection to AWS services without internet gateway", "is_correct": True},
            {"text": "Public internet access", "is_correct": False},
            {"text": "Cross-region connectivity", "is_correct": False},
            {"text": "Load balancing", "is_correct": False}
        ]
    },
    {
        "text": "Which service provides distributed denial of service (DDoS) protection?",
        "explanation": "AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency.",
        "reference": "https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html",
        "points": 1,
        "answers": [
            {"text": "AWS Shield", "is_correct": True},
            {"text": "AWS WAF", "is_correct": False},
            {"text": "Amazon CloudFront", "is_correct": False},
            {"text": "AWS Security Groups", "is_correct": False}
        ]
    },
    {
        "text": "What is AWS Transit Gateway used for?",
        "explanation": "AWS Transit Gateway is a service that enables customers to connect their Amazon Virtual Private Clouds (VPCs) and their on-premises networks to a single gateway.",
        "reference": "https://docs.aws.amazon.com/vpc/latest/tgw/",
        "points": 1,
        "answers": [
            {"text": "Connecting multiple VPCs and on-premises networks", "is_correct": True},
            {"text": "Internet access management", "is_correct": False},
            {"text": "Load balancing", "is_correct": False},
            {"text": "DNS resolution", "is_correct": False}
        ]
    }
]
