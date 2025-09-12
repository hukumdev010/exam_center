"""Wireshark Certified Network Analyst (WCNA) Certification"""

CERTIFICATION = {
    "name": "Wireshark Certified Network Analyst (WCNA)",
    "description": "Network protocol analysis and troubleshooting with Wireshark",
    "slug": "wireshark-wcna",
    "level": "Professional",
    "duration": 60,
    "questions_count": 50,
    "category_slug": "networking",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which Wireshark filter would you use to display only HTTP traffic?",
        "explanation": "The display filter 'http' in Wireshark shows only HTTP protocol traffic, helping analysts focus on web-related communications.",
        "reference": "https://wiki.wireshark.org/DisplayFilters",
        "points": 1,
        "answers": [
            {"text": "tcp.port == 80", "is_correct": False},
            {"text": "http", "is_correct": True},
            {"text": "protocol == http", "is_correct": False},
            {"text": "port 80", "is_correct": False}
        ]
    },
    {
        "text": "What does the TCP sequence number help identify in network analysis?",
        "explanation": "TCP sequence numbers help identify packet ordering, detect retransmissions, and ensure reliable data delivery by tracking the position of data in the stream.",
        "reference": "https://wiki.wireshark.org/TCP",
        "points": 1,
        "answers": [
            {"text": "Packet encryption", "is_correct": False},
            {"text": "Packet ordering and retransmissions", "is_correct": True},
            {"text": "Network latency", "is_correct": False},
            {"text": "Bandwidth utilization", "is_correct": False}
        ]
    },
    {
        "text": "Which Wireshark feature allows you to follow a complete TCP conversation?",
        "explanation": "'Follow TCP Stream' reconstructs and displays the complete conversation between two endpoints, making it easy to analyze application-layer communications.",
        "reference": "https://wiki.wireshark.org/FollowTCPStream",
        "points": 1,
        "answers": [
            {"text": "Flow Graph", "is_correct": False},
            {"text": "Follow TCP Stream", "is_correct": True},
            {"text": "Conversation List", "is_correct": False},
            {"text": "Protocol Hierarchy", "is_correct": False}
        ]
    },
    {
        "text": "What information does the Wireshark Expert System provide?",
        "explanation": "The Expert System automatically analyzes captured traffic and highlights potential problems, warnings, and noteworthy events to assist in network troubleshooting.",
        "reference": "https://wiki.wireshark.org/ExpertInfo",
        "points": 1,
        "answers": [
            {"text": "Bandwidth statistics", "is_correct": False},
            {"text": "Automatic problem detection and warnings", "is_correct": True},
            {"text": "Protocol documentation", "is_correct": False},
            {"text": "Capture file compression", "is_correct": False}
        ]
    },
    {
        "text": "Which Wireshark statistic would help identify the most active talkers on a network?",
        "explanation": "The Conversations statistic shows traffic between pairs of endpoints, helping identify the most active communication sessions and bandwidth consumers.",
        "reference": "https://wiki.wireshark.org/Statistics",
        "points": 1,
        "answers": [
            {"text": "Protocol Hierarchy", "is_correct": False},
            {"text": "Conversations", "is_correct": True},
            {"text": "Packet Lengths", "is_correct": False},
            {"text": "IO Graph", "is_correct": False}
        ]
    }
]
