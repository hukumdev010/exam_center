import { PrismaClient } from '../../src/generated/prisma'

export async function seedDevOpsCertifications(prisma: PrismaClient, categoryId: number) {
  // Terraform Associate
  const terraformAssociate = await prisma.certification.upsert({
    where: { slug: 'terraform-associate' },
    update: {},
    create: {
      name: 'HashiCorp Certified: Terraform Associate',
      description: 'Infrastructure as Code with Terraform',
      slug: 'terraform-associate',
      level: 'Associate',
      duration: 60,
      questionsCount: 57,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is Infrastructure as Code (IaC)?',
            explanation: 'Infrastructure as Code is the practice of managing and provisioning computing infrastructure through machine-readable definition files.',
            points: 1,
            answers: {
              create: [
                { text: 'Managing infrastructure through code and automation', isCorrect: true },
                { text: 'Writing application code', isCorrect: false },
                { text: 'Database schema management', isCorrect: false },
                { text: 'User interface development', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a Terraform provider?',
            explanation: 'A Terraform provider is a plugin that enables interaction with cloud providers, SaaS providers, and other APIs.',
            points: 1,
            answers: {
              create: [
                { text: 'A plugin to interact with cloud providers and APIs', isCorrect: true },
                { text: 'A configuration file', isCorrect: false },
                { text: 'A database connection', isCorrect: false },
                { text: 'A security credential', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of terraform plan?',
            explanation: 'terraform plan creates an execution plan, showing what actions Terraform will take to reach the desired state.',
            points: 1,
            answers: {
              create: [
                { text: 'Shows what actions Terraform will take', isCorrect: true },
                { text: 'Applies changes to infrastructure', isCorrect: false },
                { text: 'Destroys all resources', isCorrect: false },
                { text: 'Initializes the working directory', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Terraform state?',
            explanation: 'Terraform state is a record of the infrastructure that Terraform manages, stored in a state file.',
            points: 1,
            answers: {
              create: [
                { text: 'A record of managed infrastructure', isCorrect: true },
                { text: 'The current configuration files', isCorrect: false },
                { text: 'The execution plan', isCorrect: false },
                { text: 'The provider plugins', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // Certified Kubernetes Administrator (CKA)
  const cka = await prisma.certification.upsert({
    where: { slug: 'cka' },
    update: {},
    create: {
      name: 'Certified Kubernetes Administrator (CKA)',
      description: 'Kubernetes cluster administration and management',
      slug: 'cka',
      level: 'Professional',
      duration: 120,
      questionsCount: 17,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is a Kubernetes Pod?',
            explanation: 'A Pod is the smallest deployable unit in Kubernetes, containing one or more containers that share storage and network.',
            points: 1,
            answers: {
              create: [
                { text: 'The smallest deployable unit containing containers', isCorrect: true },
                { text: 'A container registry', isCorrect: false },
                { text: 'A networking component', isCorrect: false },
                { text: 'A storage volume', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is kubectl?',
            explanation: 'kubectl is the command-line tool for communicating with a Kubernetes cluster\'s control plane, using the Kubernetes API.',
            points: 1,
            answers: {
              create: [
                { text: 'Command-line tool for Kubernetes cluster management', isCorrect: true },
                { text: 'A container runtime', isCorrect: false },
                { text: 'A monitoring tool', isCorrect: false },
                { text: 'A storage driver', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a Kubernetes Service?',
            explanation: 'A Service is an abstraction that defines a logical set of Pods and a policy by which to access them.',
            points: 1,
            answers: {
              create: [
                { text: 'An abstraction that exposes Pods to the network', isCorrect: true },
                { text: 'A way to store configuration data', isCorrect: false },
                { text: 'A container image registry', isCorrect: false },
                { text: 'A scheduling algorithm', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of a Kubernetes Namespace?',
            explanation: 'Namespaces provide a mechanism for isolating groups of resources within a single cluster.',
            points: 1,
            answers: {
              create: [
                { text: 'To isolate groups of resources within a cluster', isCorrect: true },
                { text: 'To define container images', isCorrect: false },
                { text: 'To manage network policies', isCorrect: false },
                { text: 'To schedule workloads', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // Certified Kubernetes Application Developer (CKAD)
  const ckad = await prisma.certification.upsert({
    where: { slug: 'ckad' },
    update: {},
    create: {
      name: 'Certified Kubernetes Application Developer (CKAD)',
      description: 'Kubernetes application development and deployment',
      slug: 'ckad',
      level: 'Professional',
      duration: 120,
      questionsCount: 19,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is a Kubernetes Deployment?',
            explanation: 'A Deployment provides declarative updates for Pods and ReplicaSets, managing the desired state of your application.',
            points: 1,
            answers: {
              create: [
                { text: 'Manages the desired state of Pods and ReplicaSets', isCorrect: true },
                { text: 'A way to expose services', isCorrect: false },
                { text: 'A storage mechanism', isCorrect: false },
                { text: 'A monitoring tool', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between a ConfigMap and a Secret in Kubernetes?',
            explanation: 'ConfigMaps store non-confidential configuration data, while Secrets store sensitive information like passwords and tokens.',
            points: 1,
            answers: {
              create: [
                { text: 'ConfigMaps for non-sensitive data, Secrets for sensitive data', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: 'ConfigMaps are for applications, Secrets are for infrastructure', isCorrect: false },
                { text: 'Secrets are larger than ConfigMaps', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // Docker Certified Associate (hypothetical)
  const dockerAssociate = await prisma.certification.upsert({
    where: { slug: 'docker-associate' },
    update: {},
    create: {
      name: 'Docker Certified Associate',
      description: 'Container technology and Docker fundamentals',
      slug: 'docker-associate',
      level: 'Associate',
      duration: 90,
      questionsCount: 55,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the difference between a Docker image and a container?',
            explanation: 'A Docker image is a read-only template used to create containers, while a container is a running instance of an image.',
            points: 1,
            answers: {
              create: [
                { text: 'Image is a template, container is a running instance', isCorrect: true },
                { text: 'They are the same thing', isCorrect: false },
                { text: 'Container is larger than image', isCorrect: false },
                { text: 'Image runs faster than container', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of a Dockerfile?',
            explanation: 'A Dockerfile contains instructions for building a Docker image, defining the environment and configuration.',
            points: 1,
            answers: {
              create: [
                { text: 'Contains instructions for building Docker images', isCorrect: true },
                { text: 'Stores container runtime data', isCorrect: false },
                { text: 'Manages container networking', isCorrect: false },
                { text: 'Handles container orchestration', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return {
    terraformAssociate,
    cka,
    ckad,
    dockerAssociate
  }
}
