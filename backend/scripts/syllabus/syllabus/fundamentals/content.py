"""Syllabus content for System Design - Fundamentals (seed)

This file exports SYLLABUS_JSON which is a JSON string consumed by the
existing seeding machinery. Keeping the content as a JSON string preserves
the existing behavior (the Certification.syllabus column expects text).
"""

"""
Note: Detailed content for topics is loaded dynamically from the topics/ 
directory by the SyllabusService. This allows us to keep the detailed 
content in separate, maintainable files while preserving the existing 
seeding process.
"""

SYLLABUS_JSON = """{
        "courseOverview": {
            "title": "System Design Fundamentals",
            "description": "A comprehensive course covering essential system design concepts for building scalable and reliable distributed systems",
            "duration": "6-8 weeks",
            "difficulty": "Intermediate",
            "prerequisites": ["Basic programming knowledge", "Understanding of web applications", "Familiarity with databases"]
        },
        "modules": [
            {
                "moduleNumber": 1,
                "title": "Introduction to System Design",
                "duration": "Week 1",
                "topics": [
{
                        "title": "What is System Design?",
                        "content": {
                            "introduction": "System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements.",
                            "keyPoints": [
                                "Definition and scope of system design",
                                "High-level vs low-level system design",
                                "System design vs software architecture",
                                "Real-world examples of well-designed systems"
                            ],
                            "practicalExamples": [
                                "Designing a simple web application architecture",
                                "Comparing monolithic vs distributed system designs",
                                "Analyzing existing system architectures (Netflix, Uber, etc.)"
                            ],
                            "whatToTeach": [
                                "Start with a simple web app example (frontend, backend, database)",
                                "Explain the difference between functional and non-functional requirements",
                                "Show how requirements drive design decisions",
                                "Demonstrate the evolution from simple to complex systems",
                                "Discuss the importance of trade-offs in system design"
                            ]
                        }
                    },
                    {
                        "title": "Why System Design matters",
                        "content": {
                            "introduction": "Understanding why system design is crucial for building scalable, reliable, and maintainable software systems.",
                            "keyPoints": [
                                "Impact on business success and user experience",
                                "Cost implications of poor design decisions",
                                "Career advancement opportunities",
                                "Technical interview requirements"
                            ],
                            "practicalExamples": [
                                "Case studies of system failures due to poor design",
                                "Success stories of well-designed systems",
                                "Cost analysis of scaling decisions"
                            ],
                            "whatToTeach": [
                                "Share real-world examples of system failures (Instagram outages, Twitter scaling issues)",
                                "Explain how good system design prevents technical debt",
                                "Discuss the relationship between system design and business metrics",
                                "Show salary differences for engineers with system design skills",
                                "Explain how system design skills help in technical leadership roles"
                            ]
                        }
                    },
                    {
                        "title": "System Design Interview Process",
                        "content": {
                            "introduction": "A comprehensive guide to approaching system design interviews at top tech companies.",
                            "keyPoints": [
                                "Structure of system design interviews",
                                "Common evaluation criteria",
                                "Time management strategies",
                                "Communication best practices"
                            ],
                            "practicalExamples": [
                                "Mock interview walkthrough",
                                "Sample questions from FAANG companies",
                                "Do's and don'ts in system design interviews"
                            ],
                            "whatToTeach": [
                                "Break down the typical 45-60 minute interview structure",
                                "Teach the framework: Clarify requirements → Estimate scale → High-level design → Detailed design → Scale",
                                "Show how to ask the right clarifying questions",
                                "Demonstrate effective whiteboarding techniques",
                                "Practice common interview scenarios with time constraints"
                            ]
                        }
                    },
                    {
                        "title": "Common Architecture Patterns",
                        "content": {
                            "introduction": "Fundamental architectural patterns that form the building blocks of modern distributed systems.",
                            "keyPoints": [
                                "Client-server architecture",
                                "Three-tier architecture",
                                "Microservices vs Monolithic",
                                "Event-driven architecture",
                                "Layered architecture patterns"
                            ],
                            "practicalExamples": [
                                "Web application using three-tier architecture",
                                "E-commerce platform with microservices",
                                "Real-time chat application with event-driven design"
                            ],
                            "whatToTeach": [
                                "Start with simple client-server model and build complexity",
                                "Show when to use each pattern with concrete examples",
                                "Explain the pros and cons of each architectural approach",
                                "Demonstrate pattern selection based on requirements",
                                "Use visual diagrams to show data flow and component interactions"
                            ]
                        }
                    },
                    {
                        "title": "Scalability Fundamentals",
                        "content": {
                            "introduction": "Core principles of building systems that can handle growth in users, data, and traffic.",
                            "keyPoints": [
                                "Definition of scalability and its types",
                                "Performance vs scalability",
                                "Identifying bottlenecks",
                                "Scalability planning and metrics"
                            ],
                            "practicalExamples": [
                                "Scaling a blog from 100 to 1M users",
                                "Database scaling strategies",
                                "CDN implementation for global reach"
                            ],
                            "whatToTeach": [
                                "Define scalability with concrete numbers (RPS, concurrent users, data volume)",
                                "Explain the difference between vertical and horizontal scaling with cost analysis",
                                "Show how to identify system bottlenecks using monitoring tools",
                                "Demonstrate scalability testing and capacity planning",
                                "Discuss the relationship between scalability and system complexity"
                            ]
                        }
                    }
                ],
                "learningObjectives": [
                    "Understand the importance of system design",
                    "Learn the basic components of a distributed system",
                    "Identify common architectural patterns"
                ]
            },
            {
                "moduleNumber": 2,
                "title": "Scalability Concepts",
                "duration": "Week 1-2",
                "topics": [
                    {
                        "title": "Horizontal vs Vertical Scaling",
                        "content": {
                            "introduction": "Understanding the two fundamental approaches to scaling systems and when to use each approach.",
                            "keyPoints": [
                                "Vertical scaling: Adding more power (CPU, RAM, Storage)",
                                "Horizontal scaling: Adding more machines",
                                "Cost implications and limits of each approach",
                                "When to choose vertical vs horizontal scaling"
                            ],
                            "practicalExamples": [
                                "Scaling a database server vertically (upgrading from 4GB to 32GB RAM)",
                                "Horizontal scaling with web server clusters",
                                "Real-world examples: Netflix (horizontal) vs traditional banking systems (vertical)"
                            ],
                            "whatToTeach": [
                                "Start with a simple web application serving 1000 users",
                                "Show vertical scaling: upgrading server specs and its limitations",
                                "Demonstrate horizontal scaling: adding multiple servers behind load balancer",
                                "Compare costs: $1000/month for powerful server vs $200/month × 5 smaller servers",
                                "Explain scaling limits: vertical has hardware limits, horizontal has complexity limits",
                                "Show real AWS/Azure pricing for different instance types"
                            ]
                        }
                    },
                    {
                        "title": "Load Balancing Strategies",
                        "content": {
                            "introduction": "Distributing incoming requests across multiple servers to ensure optimal resource utilization and avoid overloading.",
                            "keyPoints": [
                                "Round-robin load balancing",
                                "Weighted round-robin",
                                "Least connections method",
                                "IP hash-based routing",
                                "Health checks and failover mechanisms"
                            ],
                            "practicalExamples": [
                                "Setting up NGINX as a load balancer",
                                "AWS Application Load Balancer configuration",
                                "Handling server failures with health checks"
                            ],
                            "whatToTeach": [
                                "Start with the problem: 1 server getting overwhelmed, 2 servers idle",
                                "Demonstrate round-robin with simple examples (Server A, B, C rotation)",
                                "Show weighted balancing: Server A (50%), Server B (30%), Server C (20%)",
                                "Explain sticky sessions and when they're needed (shopping carts, user sessions)",
                                "Demo health checks: removing failed servers from rotation",
                                "Show real load balancer configurations and monitoring dashboards"
                            ]
                        }
                    },
                    {
                        "title": "Auto-scaling Mechanisms",
                        "content": {
                            "introduction": "Automatically adjusting system resources based on demand to maintain performance while optimizing costs.",
                            "keyPoints": [
                                "Reactive vs predictive scaling",
                                "Scaling triggers and metrics (CPU, memory, request rate)",
                                "Scaling policies and cooldown periods",
                                "Cost optimization strategies"
                            ],
                            "practicalExamples": [
                                "AWS Auto Scaling Groups configuration",
                                "Kubernetes Horizontal Pod Autoscaler",
                                "Database read replica auto-scaling"
                            ],
                            "whatToTeach": [
                                "Show traffic patterns: Black Friday spikes, daily/weekly cycles",
                                "Demonstrate reactive scaling: CPU > 80% → add server, CPU < 30% → remove server",
                                "Explain scaling delays and the importance of cooldown periods",
                                "Show predictive scaling: historical data to predict traffic spikes",
                                "Demo real auto-scaling setup with CloudWatch metrics",
                                "Calculate cost savings: manual vs auto-scaling over time"
                            ]
                        }
                    },
                    {
                        "title": "Performance Metrics",
                        "content": {
                            "introduction": "Key metrics to monitor system performance and make informed scaling decisions.",
                            "keyPoints": [
                                "Response time and latency measurements",
                                "Throughput (requests per second)",
                                "Resource utilization (CPU, memory, disk, network)",
                                "Error rates and availability metrics",
                                "User experience metrics"
                            ],
                            "practicalExamples": [
                                "Setting up monitoring with Prometheus and Grafana",
                                "Creating performance dashboards",
                                "Alerting on performance degradation"
                            ],
                            "whatToTeach": [
                                "Define each metric with concrete examples: latency in milliseconds, throughput in RPS",
                                "Show how to measure: using tools like Apache Bench, JMeter for load testing",
                                "Explain the relationship between metrics: high CPU → increased latency → lower throughput",
                                "Demonstrate real monitoring dashboards with good vs bad performance patterns",
                                "Show how to set meaningful alerting thresholds",
                                "Connect metrics to business impact: 100ms delay = 1% revenue loss"
                            ]
                        }
                    },
                    {
                        "title": "Capacity Planning",
                        "content": {
                            "introduction": "Forecasting future resource needs based on business growth and usage patterns.",
                            "keyPoints": [
                                "Traffic growth forecasting",
                                "Resource requirement calculations",
                                "Peak load planning",
                                "Budget planning for infrastructure",
                                "Scalability testing strategies"
                            ],
                            "practicalExamples": [
                                "Planning for 10x user growth over 12 months",
                                "Black Friday traffic preparation",
                                "New product launch capacity planning"
                            ],
                            "whatToTeach": [
                                "Start with current metrics: 1000 users, 100 RPS, 2GB RAM usage",
                                "Show growth projections: 10x users = 10x traffic? (not always linear)",
                                "Calculate resource needs: if 1000 users need 2GB RAM, do 10k users need 20GB?",
                                "Plan for peak loads: normal load vs Black Friday vs viral events",
                                "Demo load testing to validate capacity plans",
                                "Show cost projections and budget planning spreadsheets"
                            ]
                        }
                    }
                ],
                "learningObjectives": [
                    "Differentiate between scaling approaches",
                    "Design load balancing solutions",
                    "Plan for system capacity and growth"
                ]
            },
            {
                "moduleNumber": 3,
                "title": "Database Design & Management",
                "duration": "Week 2-3",
                "topics": [
                    "SQL vs NoSQL Databases",
                    "Database Sharding",
                    "Database Replication",
                    "Database Partitioning",
                    "Database Normalization vs Denormalization",
                    "Connection Pooling",
                    "Database Indexing Strategies"
                ],
                "learningObjectives": [
                    "Choose appropriate database types for different use cases",
                    "Design database scaling strategies",
                    "Optimize database performance"
                ]
            },
            {
                "moduleNumber": 4,
                "title": "Distributed System Fundamentals",
                "duration": "Week 3-4",
                "topics": [
                    "CAP Theorem",
                    "Consistency Models",
                    "Eventual Consistency",
                    "ACID vs BASE Properties",
                    "Distributed Transactions",
                    "Consensus Algorithms",
                    "Fault Tolerance & Resilience"
                ],
                "learningObjectives": [
                    "Understand trade-offs in distributed systems",
                    "Apply consistency models appropriately",
                    "Design fault-tolerant systems"
                ]
            },
            {
                "moduleNumber": 5,
                "title": "Caching & Performance",
                "duration": "Week 4-5",
                "topics": [
                    "Caching Strategies",
                    "Cache-aside vs Write-through",
                    "CDN (Content Delivery Networks)",
                    "In-memory Caching",
                    "Database Query Optimization",
                    "Performance Monitoring"
                ],
                "learningObjectives": [
                    "Implement effective caching strategies",
                    "Optimize system performance",
                    "Monitor and measure system metrics"
                ]
            },
            {
                "moduleNumber": 6,
                "title": "Communication Patterns",
                "duration": "Week 5-6",
                "topics": [
                    "Synchronous vs Asynchronous Communication",
                    "Message Queues",
                    "Message Brokers",
                    "API Design & Versioning",
                    "API Rate Limiting",
                    "Service Discovery",
                    "Circuit Breaker Pattern"
                ],
                "learningObjectives": [
                    "Design efficient communication patterns",
                    "Implement asynchronous messaging",
                    "Create robust API strategies"
                ]
            },
            {
                "moduleNumber": 7,
                "title": "System Architecture Patterns",
                "duration": "Week 6-7",
                "topics": [
                    "Monolithic vs Microservices Architecture",
                    "Service-Oriented Architecture (SOA)",
                    "Event-Driven Architecture",
                    "Stateful vs Stateless Services",
                    "Proxy Servers & Reverse Proxies",
                    "Load Balancer Types & Algorithms"
                ],
                "learningObjectives": [
                    "Compare different architectural approaches",
                    "Design microservices architectures",
                    "Implement event-driven patterns"
                ]
            },
            {
                "moduleNumber": 8,
                "title": "Reliability & Monitoring",
                "duration": "Week 7-8",
                "topics": [
                    "Single Points of Failure",
                    "Graceful Degradation",
                    "Health Checks & Monitoring",
                    "Logging & Observability",
                    "Disaster Recovery",
                    "Blue-Green Deployment",
                    "A/B Testing"
                ],
                "learningObjectives": [
                    "Build reliable and resilient systems",
                    "Implement comprehensive monitoring",
                    "Plan for disaster recovery"
                ]
            },
            {
                "moduleNumber": 9,
                "title": "Data Management & Storage",
                "duration": "Week 8",
                "topics": [
                    "Data Partitioning Strategies",
                    "Data Locality",
                    "Data Compression",
                    "Distributed Hash Tables",
                    "Data Replication Lag",
                    "Backup & Recovery Strategies"
                ],
                "learningObjectives": [
                    "Design data storage solutions",
                    "Implement data management strategies",
                    "Plan data backup and recovery"
                ]
            },
            {
                "moduleNumber": 10,
                "title": "Modern System Design Practices",
                "duration": "Week 8",
                "topics": [
                    "Containerization & Docker",
                    "Orchestration with Kubernetes",
                    "Infrastructure as Code",
                    "DevOps Integration",
                    "Security Considerations",
                    "Cost Optimization"
                ],
                "learningObjectives": [
                    "Apply modern deployment practices",
                    "Implement security best practices",
                    "Optimize system costs"
                ]
            }
        ],
        "practicalExercises": [
            "Design a URL Shortener (like bit.ly)",
            "Design a Chat Application (like WhatsApp)",
            "Design a Social Media Feed (like Twitter)",
            "Design a Video Streaming Platform (like YouTube)",
            "Design an E-commerce Platform (like Amazon)",
            "Design a Ride-sharing Service (like Uber)",
            "Design a Search Engine (like Google)"
        ],
        "assessmentCriteria": [
            "Understanding of scalability principles",
            "Ability to identify system bottlenecks",
            "Knowledge of appropriate technology choices",
            "Understanding of trade-offs in system design",
            "Ability to design for reliability and fault tolerance"
        ],
        "recommendedReadings": [
            "Designing Data-Intensive Applications by Martin Kleppmann",
            "System Design Interview by Alex Xu",
            "Building Microservices by Sam Newman",
            "Site Reliability Engineering by Google",
            "The Architecture of Open Source Applications"
        ],
        "toolsAndTechnologies": [
            "Load Balancers: HAProxy, NGINX, AWS ELB",
            "Databases: PostgreSQL, MongoDB, Redis, Cassandra",
            "Message Queues: RabbitMQ, Apache Kafka, AWS SQS",
            "Caching: Redis, Memcached, Varnish",
            "Monitoring: Prometheus, Grafana, ELK Stack",
            "Containerization: Docker, Kubernetes"
        ]
    }"""
