import { PrismaClient } from '../../src/generated/prisma'

export async function seedSystemsCertifications(prisma: PrismaClient, categoryId: number) {
  // Linux System Administration
  const linuxFundamentals = await prisma.certification.upsert({
    where: { slug: 'linux-fundamentals' },
    update: {},
    create: {
      name: 'Linux System Administration',
      description: 'Core Linux operating system concepts and administration',
      slug: 'linux-fundamentals',
      level: 'Fundamentals',
      duration: 90,
      questionsCount: 50,
      categoryId,
      questions: {
        create: [
          {
            text: 'What command is used to list files and directories?',
            explanation: 'The ls command lists the contents of directories. Common options include -l for detailed listing and -a to show hidden files.',
            points: 1,
            answers: {
              create: [
                { text: 'ls', isCorrect: true },
                { text: 'dir', isCorrect: false },
                { text: 'list', isCorrect: false },
                { text: 'cat', isCorrect: false },
              ],
            },
          },
          {
            text: 'What does the chmod command do?',
            explanation: 'chmod (change mode) is used to change the permissions of files and directories in Unix/Linux systems.',
            points: 1,
            answers: {
              create: [
                { text: 'Changes file and directory permissions', isCorrect: true },
                { text: 'Changes file ownership', isCorrect: false },
                { text: 'Changes file content', isCorrect: false },
                { text: 'Changes file location', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the sudo command?',
            explanation: 'sudo allows users to run commands with the security privileges of another user, typically the superuser (root).',
            points: 1,
            answers: {
              create: [
                { text: 'Run commands with elevated privileges', isCorrect: true },
                { text: 'Change user password', isCorrect: false },
                { text: 'Display system information', isCorrect: false },
                { text: 'Manage network connections', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between hard links and soft links?',
            explanation: 'Hard links point directly to the file data on disk, while soft links (symbolic links) point to the file path.',
            points: 1,
            answers: {
              create: [
                { text: 'Hard links point to file data, soft links point to file path', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: 'Hard links are faster', isCorrect: false },
                { text: 'Soft links take more space', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the cron daemon?',
            explanation: 'The cron daemon is used to schedule and execute recurring tasks at specified times or intervals.',
            points: 1,
            answers: {
              create: [
                { text: 'Schedule and execute recurring tasks', isCorrect: true },
                { text: 'Monitor system performance', isCorrect: false },
                { text: 'Manage user accounts', isCorrect: false },
                { text: 'Handle network connections', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // Network Administration
  const networkingFundamentals = await prisma.certification.upsert({
    where: { slug: 'networking-fundamentals' },
    update: {},
    create: {
      name: 'Network Administration Fundamentals',
      description: 'Basic networking concepts and protocols',
      slug: 'networking-fundamentals',
      level: 'Fundamentals',
      duration: 75,
      questionsCount: 40,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the OSI model?',
            explanation: 'The OSI (Open Systems Interconnection) model is a conceptual framework with 7 layers that describes network communication.',
            points: 1,
            answers: {
              create: [
                { text: 'A 7-layer conceptual framework for network communication', isCorrect: true },
                { text: 'A network security protocol', isCorrect: false },
                { text: 'A type of router configuration', isCorrect: false },
                { text: 'A wireless networking standard', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between TCP and UDP?',
            explanation: 'TCP is connection-oriented and reliable with error checking, while UDP is connectionless and faster but less reliable.',
            points: 1,
            answers: {
              create: [
                { text: 'TCP is reliable and connection-oriented, UDP is faster but less reliable', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: 'UDP is more secure than TCP', isCorrect: false },
                { text: 'TCP is only for web traffic', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a subnet mask?',
            explanation: 'A subnet mask is used to divide an IP address into network and host portions, determining which part identifies the network.',
            points: 1,
            answers: {
              create: [
                { text: 'Divides IP address into network and host portions', isCorrect: true },
                { text: 'Encrypts network traffic', isCorrect: false },
                { text: 'Manages DNS resolution', isCorrect: false },
                { text: 'Controls network bandwidth', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  // System Design (moved to systems category)
  const systemDesign = await prisma.certification.upsert({
    where: { slug: 'system-design' },
    update: {},
    create: {
      name: 'System Design Fundamentals',
      description: 'Comprehensive system design concepts and best practices',
      slug: 'system-design',
      level: 'Advanced',
      duration: 120,
      questionsCount: 30,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is horizontal scaling?',
            explanation: 'Horizontal scaling (scale-out) means adding more servers to handle increased load, distributing the workload across multiple machines.',
            points: 1,
            answers: {
              create: [
                { text: 'Adding more servers to distribute load', isCorrect: true },
                { text: 'Upgrading existing server hardware', isCorrect: false },
                { text: 'Increasing memory on current server', isCorrect: false },
                { text: 'Adding more CPU cores', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the CAP theorem?',
            explanation: 'The CAP theorem states that in a distributed system, you can only guarantee two of: Consistency, Availability, and Partition tolerance.',
            points: 1,
            answers: {
              create: [
                { text: 'Consistency, Availability, Partition tolerance - pick 2', isCorrect: true },
                { text: 'A database design pattern', isCorrect: false },
                { text: 'A caching strategy', isCorrect: false },
                { text: 'A security protocol', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is load balancing?',
            explanation: 'Load balancing distributes incoming requests across multiple servers to ensure no single server becomes overwhelmed.',
            points: 1,
            answers: {
              create: [
                { text: 'Distributing requests across multiple servers', isCorrect: true },
                { text: 'Backing up data to multiple locations', isCorrect: false },
                { text: 'Optimizing database queries', isCorrect: false },
                { text: 'Managing user authentication', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return {
    linuxFundamentals,
    networkingFundamentals,
    systemDesign
  }
}
