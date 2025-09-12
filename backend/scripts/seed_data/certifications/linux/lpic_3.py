"""Linux Professional Institute Certification Level 3 (LPIC-3)"""

CERTIFICATION = {
    "name": "Linux Professional Institute Certification Level 3 (LPIC-3)",
    "description": "Senior level Linux professional and enterprise-level skills",
    "slug": "lpic-3",
    "level": "Expert",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "linux",
    "is_active": True
}

QUESTIONS = [
    {
        "text": "Which tool is primarily used for advanced LDAP directory management?",
        "explanation": "OpenLDAP's slapd is the primary LDAP directory server, and ldapmodify, ldapsearch, and other ldap* tools are used for advanced directory management.",
        "reference": "https://www.lpi.org/our-certifications/lpic-3-overview",
        "points": 1,
        "answers": [
            {"text": "Active Directory", "is_correct": False},
            {"text": "OpenLDAP (slapd)", "is_correct": True},
            {"text": "NIS", "is_correct": False},
            {"text": "Kerberos", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary configuration file for Samba server?",
        "explanation": "The main Samba configuration file is /etc/samba/smb.conf, which contains global settings and share definitions.",
        "reference": "https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html",
        "points": 1,
        "answers": [
            {"text": "/etc/samba/smb.conf", "is_correct": True},
            {"text": "/etc/smb.conf", "is_correct": False},
            {"text": "/etc/samba/samba.conf", "is_correct": False},
            {"text": "/usr/local/samba/smb.conf", "is_correct": False}
        ]
    },
    {
        "text": "Which command is used to test Samba configuration syntax?",
        "explanation": "The testparm command is used to check the syntax of the Samba configuration file and display the configuration parameters.",
        "reference": "https://www.samba.org/samba/docs/current/man-html/testparm.1.html",
        "points": 1,
        "answers": [
            {"text": "smbstatus", "is_correct": False},
            {"text": "testparm", "is_correct": True},
            {"text": "smbclient", "is_correct": False},
            {"text": "nmblookup", "is_correct": False}
        ]
    },
    {
        "text": "What protocol does NFS version 4 use for security by default?",
        "explanation": "NFSv4 uses Kerberos for authentication and security by default, providing strong security mechanisms for network file systems.",
        "reference": "https://tools.ietf.org/rfc/rfc7530.txt",
        "points": 1,
        "answers": [
            {"text": "SSL/TLS", "is_correct": False},
            {"text": "Kerberos", "is_correct": True},
            {"text": "LDAP", "is_correct": False},
            {"text": "SSH", "is_correct": False}
        ]
    },
    {
        "text": "Which file contains the NFS export configuration?",
        "explanation": "/etc/exports contains the configuration for NFS exports, specifying which directories are shared and with what permissions.",
        "reference": "https://man7.org/linux/man-pages/man5/exports.5.html",
        "points": 1,
        "answers": [
            {"text": "/etc/fstab", "is_correct": False},
            {"text": "/etc/exports", "is_correct": True},
            {"text": "/etc/nfs.conf", "is_correct": False},
            {"text": "/etc/nfs/exports", "is_correct": False}
        ]
    }
]
