"""Certified Kubernetes Administrator (CKA) Certification"""

CERTIFICATION = {
    "name": "Certified Kubernetes Administrator",
    "description": "Kubernetes cluster administration skills",
    "slug": "certified-kubernetes-administrator-cka",
    "level": "Professional",
    "duration": 15,
    "questions_count": 5,
    "category_slug": "devops",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is a Pod in Kubernetes?",
        "explanation": "A Pod is the smallest deployable unit in Kubernetes that can contain one or more containers. Containers in a Pod share the same network namespace and storage volumes.",
        "reference": "https://kubernetes.io/docs/concepts/workloads/pods/",
        "points": 1,
        "answers": [
            {"text": "A Kubernetes cluster", "is_correct": False},
            {
                "text": "The smallest deployable unit containing containers",
                "is_correct": True,
            },
            {"text": "A networking component", "is_correct": False},
            {"text": "A storage volume", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of a Kubernetes Service?",
        "explanation": "A Service is an abstraction that defines a logical set of Pods and a policy to access them. It provides stable networking and load balancing for Pods that may come and go.",
        "reference": "https://kubernetes.io/docs/concepts/services-networking/service/",
        "points": 1,
        "answers": [
            {"text": "To store persistent data", "is_correct": False},
            {
                "text": "To provide stable networking and load balancing for Pods",
                "is_correct": True,
            },
            {"text": "To manage container images", "is_correct": False},
            {"text": "To schedule workloads", "is_correct": False},
        ],
    },
    {
        "text": "What is kubectl?",
        "explanation": "kubectl is the command-line tool for interacting with Kubernetes clusters. It allows you to deploy applications, inspect and manage cluster resources, and view logs.",
        "reference": "https://kubernetes.io/docs/reference/kubectl/overview/",
        "points": 1,
        "answers": [
            {"text": "A container runtime", "is_correct": False},
            {"text": "The Kubernetes command-line tool", "is_correct": True},
            {"text": "A monitoring dashboard", "is_correct": False},
            {"text": "A package manager", "is_correct": False},
        ],
    },
    {
        "text": "What is a Deployment in Kubernetes?",
        "explanation": "A Deployment provides declarative updates for Pods and ReplicaSets. It allows you to describe the desired state and the Deployment controller changes the actual state to the desired state at a controlled rate.",
        "reference": "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/",
        "points": 1,
        "answers": [
            {"text": "A type of storage volume", "is_correct": False},
            {
                "text": "A controller for managing Pod replicas and updates",
                "is_correct": True,
            },
            {"text": "A networking policy", "is_correct": False},
            {"text": "A security configuration", "is_correct": False},
        ],
    },
    {
        "text": "What is a Namespace in Kubernetes?",
        "explanation": "Namespaces provide a mechanism for isolating groups of resources within a single cluster. They are intended for use in environments with many users spread across multiple teams or projects.",
        "reference": "https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/",
        "points": 1,
        "answers": [
            {"text": "A container image repository", "is_correct": False},
            {
                "text": "A way to isolate groups of resources within a cluster",
                "is_correct": True,
            },
            {"text": "A type of persistent volume", "is_correct": False},
            {"text": "A load balancing mechanism", "is_correct": False},
        ],
    },
]
