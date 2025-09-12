"""CompTIA Network+ Certification (Security Focus)"""

CERTIFICATION = {
    "name": "CompTIA Network+ (Security Focus)",
    "description": "Networking fundamentals with emphasis on network security concepts",
    "slug": "comptia-network-plus-security",
    "level": "Intermediate",
    "duration": 90,
    "questions_count": 90,
    "category_slug": "cybersecurity",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "What is the purpose of a VLAN in network security?",
        "explanation": "A VLAN (Virtual Local Area Network) segments network traffic to improve security by isolating different types of traffic and limiting broadcast domains.",
        "reference": "https://www.cisco.com/c/en/us/tech/lan-switching/virtual-local-area-networks-vlans/index.html",
        "points": 1,
        "answers": [
            {"text": "Segment network traffic for improved security", "is_correct": True},
            {"text": "Increase network speed", "is_correct": False},
            {"text": "Reduce hardware costs", "is_correct": False},
            {"text": "Improve wireless signals", "is_correct": False}
        ]
    },
    {
        "text": "Which protocol provides secure remote access to network devices?",
        "explanation": "SSH (Secure Shell) provides encrypted remote access to network devices, replacing insecure protocols like Telnet with strong authentication and encryption.",
        "reference": "https://tools.ietf.org/html/rfc4251",
        "points": 1,
        "answers": [
            {"text": "SSH (Secure Shell)", "is_correct": True},
            {"text": "Telnet", "is_correct": False},
            {"text": "HTTP", "is_correct": False},
            {"text": "FTP", "is_correct": False}
        ]
    },
    {
        "text": "What is the difference between IDS and IPS?",
        "explanation": "An IDS (Intrusion Detection System) monitors and alerts on suspicious activity, while an IPS (Intrusion Prevention System) can actively block threats in real-time.",
        "reference": "https://www.sans.org/reading-room/whitepapers/detection/intrusion-detection-prevention-systems-ids-ips-1351",
        "points": 1,
        "answers": [
            {"text": "IDS detects and alerts; IPS detects and blocks", "is_correct": True},
            {"text": "IDS blocks threats; IPS only monitors", "is_correct": False},
            {"text": "They are the same thing", "is_correct": False},
            {"text": "IDS is hardware; IPS is software", "is_correct": False}
        ]
    },
    {
        "text": "Which type of attack involves redirecting network traffic?",
        "explanation": "A man-in-the-middle (MITM) attack occurs when an attacker intercepts and potentially alters communications between two parties who believe they are communicating directly.",
        "reference": "https://www.sans.org/reading-room/whitepapers/detection/man-middle-attack-2005",
        "points": 1,
        "answers": [
            {"text": "Man-in-the-middle attack", "is_correct": True},
            {"text": "DDoS attack", "is_correct": False},
            {"text": "Phishing attack", "is_correct": False},
            {"text": "SQL injection", "is_correct": False}
        ]
    },
    {
        "text": "What is network access control (NAC)?",
        "explanation": "Network Access Control (NAC) is a security approach that restricts access to network resources based on device compliance, user identity, and security policies.",
        "reference": "https://www.sans.org/reading-room/whitepapers/networkdevs/network-access-control-overview-36012",
        "points": 1,
        "answers": [
            {"text": "Security approach to control device access to network resources", "is_correct": True},
            {"text": "A type of firewall", "is_correct": False},
            {"text": "A wireless encryption standard", "is_correct": False},
            {"text": "A network monitoring tool", "is_correct": False}
        ]
    }
]
