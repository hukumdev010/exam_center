"""Juniper Networks Certified Internet Professional (JNCIP) Certification"""

CERTIFICATION = {
    "name": "Juniper Networks Certified Internet Professional (JNCIP)",
    "description": "Advanced Juniper networking technologies and enterprise routing",
    "slug": "juniper-jncip",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "networking",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the primary routing protocol used in Juniper's MPLS networks?",
        "explanation": "BGP is the primary protocol for MPLS VPN implementations in Juniper networks, used for distributing VPN routes between PE routers.",
        "reference": "https://www.juniper.net/documentation/us/en/software/junos/mpls/topics/concept/mpls-bgp-overview.html",
        "points": 1,
        "answers": [
            {"text": "OSPF", "is_correct": False},
            {"text": "BGP", "is_correct": True},
            {"text": "ISIS", "is_correct": False},
            {"text": "RIP", "is_correct": False},
        ],
    },
    {
        "text": "Which Junos command is used to display the routing table?",
        "explanation": "The 'show route' command displays the routing table in Junos OS, showing all learned routes and their preferences.",
        "reference": "https://www.juniper.net/documentation/us/en/software/junos/cli/topics/ref/command/show-route.html",
        "points": 1,
        "answers": [
            {"text": "show ip route", "is_correct": False},
            {"text": "show route", "is_correct": True},
            {"text": "display route", "is_correct": False},
            {"text": "get route", "is_correct": False},
        ],
    },
    {
        "text": "What is the default preference value for OSPF internal routes in Junos?",
        "explanation": "In Junos OS, OSPF internal routes have a default preference (administrative distance) of 10, making them highly preferred.",
        "reference": "https://www.juniper.net/documentation/us/en/software/junos/ospf/topics/ref/statement/preference-edit-protocols-ospf.html",
        "points": 1,
        "answers": [
            {"text": "10", "is_correct": True},
            {"text": "100", "is_correct": False},
            {"text": "110", "is_correct": False},
            {"text": "150", "is_correct": False},
        ],
    },
    {
        "text": "Which Juniper technology provides network segmentation and virtualization?",
        "explanation": "EVPN (Ethernet VPN) provides advanced Layer 2 and Layer 3 VPN services with enhanced segmentation and multi-tenancy capabilities in Juniper networks.",
        "reference": "https://www.juniper.net/documentation/us/en/software/junos/evpn-vxlan/topics/concept/evpn-overview.html",
        "points": 1,
        "answers": [
            {"text": "VPLS", "is_correct": False},
            {"text": "EVPN", "is_correct": True},
            {"text": "L2Circuit", "is_correct": False},
            {"text": "CCC", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the Junos commit model?",
        "explanation": "The Junos commit model allows administrators to make configuration changes, validate them, and then commit all changes atomically, ensuring configuration consistency.",
        "reference": "https://www.juniper.net/documentation/us/en/software/junos/cli/topics/concept/junos-cli-configuration-mode-overview.html",
        "points": 1,
        "answers": [
            {"text": "Backup configurations", "is_correct": False},
            {"text": "Atomic configuration changes", "is_correct": True},
            {"text": "Performance monitoring", "is_correct": False},
            {"text": "User authentication", "is_correct": False},
        ],
    },
]
