import { PrismaClient } from '../../src/generated/prisma'

export async function seedWebHacking(prisma: PrismaClient, categoryId: number) {
  const webHacking = await prisma.certification.upsert({
    where: { slug: 'web-security-hacking' },
    update: {},
    create: {
      name: 'Web Security & Ethical Hacking',
      description: 'Web application security testing, penetration testing, and ethical hacking fundamentals',
      slug: 'web-security-hacking',
      level: 'Intermediate',
      duration: 90,
      questionsCount: 35,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is SQL injection?',
            explanation: 'SQL injection is a code injection technique that exploits vulnerabilities in applications that construct SQL queries from user input without proper validation or sanitization.',
            points: 1,
            answers: {
              create: [
                { text: 'A technique that exploits vulnerabilities in SQL query construction', isCorrect: true },
                { text: 'A method to optimize database performance', isCorrect: false },
                { text: 'A way to backup databases', isCorrect: false },
                { text: 'A database administration tool', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Cross-Site Scripting (XSS)?',
            explanation: 'XSS is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users, potentially stealing cookies, session tokens, or other sensitive information.',
            points: 1,
            answers: {
              create: [
                { text: 'A vulnerability allowing injection of malicious scripts into web pages', isCorrect: true },
                { text: 'A method to share content between websites', isCorrect: false },
                { text: 'A way to optimize website loading', isCorrect: false },
                { text: 'A cross-platform development framework', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is CSRF (Cross-Site Request Forgery)?',
            explanation: 'CSRF is an attack that forces authenticated users to execute unwanted actions on a web application where they are currently authenticated.',
            points: 1,
            answers: {
              create: [
                { text: 'An attack forcing authenticated users to execute unwanted actions', isCorrect: true },
                { text: 'A method to forge SSL certificates', isCorrect: false },
                { text: 'A way to bypass firewalls', isCorrect: false },
                { text: 'A technique to steal passwords', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of penetration testing?',
            explanation: 'Penetration testing is a simulated cyber attack against a system to check for exploitable vulnerabilities and assess security posture.',
            points: 1,
            answers: {
              create: [
                { text: 'Simulated cyber attack to find exploitable vulnerabilities', isCorrect: true },
                { text: 'Testing network speed', isCorrect: false },
                { text: 'Checking database performance', isCorrect: false },
                { text: 'Testing user interface design', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a buffer overflow attack?',
            explanation: 'Buffer overflow occurs when a program writes more data to a buffer than it can hold, potentially allowing attackers to execute malicious code or crash the program.',
            points: 1,
            answers: {
              create: [
                { text: 'Writing more data to a buffer than it can hold', isCorrect: true },
                { text: 'A network congestion issue', isCorrect: false },
                { text: 'A database connection problem', isCorrect: false },
                { text: 'A memory optimization technique', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is social engineering in cybersecurity?',
            explanation: 'Social engineering is the psychological manipulation of people into performing actions or divulging confidential information, often used as the initial step in cyberattacks.',
            points: 1,
            answers: {
              create: [
                { text: 'Psychological manipulation to obtain confidential information', isCorrect: true },
                { text: 'Building secure software systems', isCorrect: false },
                { text: 'Network architecture design', isCorrect: false },
                { text: 'Database optimization', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the OWASP Top 10?',
            explanation: 'OWASP Top 10 is a regularly updated list of the most critical web application security risks, providing guidance for developers and security professionals.',
            points: 1,
            answers: {
              create: [
                { text: 'A list of the most critical web application security risks', isCorrect: true },
                { text: 'Top 10 programming languages', isCorrect: false },
                { text: 'Best web development frameworks', isCorrect: false },
                { text: 'Most popular databases', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a man-in-the-middle (MITM) attack?',
            explanation: 'MITM attack occurs when an attacker secretly intercepts and potentially alters communications between two parties who believe they are communicating directly.',
            points: 1,
            answers: {
              create: [
                { text: 'Intercepting and potentially altering communications between two parties', isCorrect: true },
                { text: 'A network routing protocol', isCorrect: false },
                { text: 'A database replication method', isCorrect: false },
                { text: 'A load balancing technique', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of a Web Application Firewall (WAF)?',
            explanation: 'A WAF protects web applications by filtering, monitoring, and blocking HTTP traffic between a web application and the Internet based on predefined security rules.',
            points: 1,
            answers: {
              create: [
                { text: 'Filter and block malicious HTTP traffic to web applications', isCorrect: true },
                { text: 'Optimize web application performance', isCorrect: false },
                { text: 'Manage database connections', isCorrect: false },
                { text: 'Handle user authentication', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is directory traversal attack?',
            explanation: 'Directory traversal (path traversal) attack allows attackers to access files and directories outside the web root directory by manipulating file paths in URLs.',
            points: 1,
            answers: {
              create: [
                { text: 'Accessing files outside the web root directory through path manipulation', isCorrect: true },
                { text: 'Organizing website folder structure', isCorrect: false },
                { text: 'Searching through file systems', isCorrect: false },
                { text: 'Creating directory backups', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is clickjacking?',
            explanation: 'Clickjacking is an attack that tricks users into clicking on something different from what they perceive, often by using transparent or opaque layers.',
            points: 1,
            answers: {
              create: [
                { text: 'Tricking users into clicking on hidden or disguised elements', isCorrect: true },
                { text: 'Improving website click-through rates', isCorrect: false },
                { text: 'Analyzing user click patterns', isCorrect: false },
                { text: 'Preventing accidental clicks', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between black box, white box, and gray box penetration testing?',
            explanation: 'Black box testing has no prior knowledge, white box has full knowledge of the system, and gray box has partial knowledge of the target system.',
            points: 1,
            answers: {
              create: [
                { text: 'Different levels of prior knowledge about the target system', isCorrect: true },
                { text: 'Different colors used in testing reports', isCorrect: false },
                { text: 'Different types of testing tools', isCorrect: false },
                { text: 'Different stages of the testing process', isCorrect: false },
              ],
            },
          },
        ],
      },
    },
  })

  return webHacking
}
