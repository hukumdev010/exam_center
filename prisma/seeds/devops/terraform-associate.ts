import { PrismaClient } from '../../../src/generated/prisma'

export async function seedTerraformAssociate(prisma: PrismaClient, categoryId: number) {
  // HashiCorp Certified: Terraform Associate
  const terraformAssociate = await prisma.certification.upsert({
    where: { slug: 'terraform-associate' },
    update: {},
    create: {
      name: 'HashiCorp Certified: Terraform Associate',
      description: 'Infrastructure as Code with Terraform covering configuration syntax, state management, modules, providers, and best practices. This certification validates knowledge of Terraform fundamentals and the ability to build, change, and destroy infrastructure with Terraform.',
      slug: 'terraform-associate',
      level: 'Associate',
      duration: 60,
      questionsCount: 57,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is Infrastructure as Code (IaC) and what are its key benefits?',
            explanation: 'Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than through physical hardware configuration or interactive configuration tools. Key benefits include: version control for infrastructure, reproducibility, consistency across environments, automation of provisioning, reduced human error, faster deployment cycles, cost optimization through resource management, and improved collaboration between teams. IaC enables treating infrastructure like software. Reference: https://www.terraform.io/intro/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Managing infrastructure through code with version control, reproducibility, and automation benefits', isCorrect: true },
                { text: 'Writing application code using infrastructure libraries and frameworks', isCorrect: false },
                { text: 'Database schema management using SQL migration scripts', isCorrect: false },
                { text: 'User interface development using infrastructure design patterns', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a Terraform provider and how does the provider plugin system work?',
            explanation: 'A Terraform provider is a plugin that enables interaction with cloud providers, SaaS providers, and other APIs. Providers are responsible for understanding API interactions and exposing resources. The provider plugin system works by: downloading providers during terraform init, providers translating HCL configuration to API calls, managing resource lifecycle (create, read, update, delete), handling authentication and API communication, and providing resource schemas and validation. Each provider is maintained separately and versioned independently. Popular providers include AWS, Azure, Google Cloud, Kubernetes, and Docker. Reference: https://www.terraform.io/docs/language/providers/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'A plugin that enables interaction with APIs, translates HCL to API calls, and manages resource lifecycle', isCorrect: true },
                { text: 'A configuration file that defines infrastructure components and their relationships', isCorrect: false },
                { text: 'A database connection string that enables data persistence for Terraform state', isCorrect: false },
                { text: 'A security credential system for managing authentication across cloud platforms', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of terraform plan and what information does it provide?',
            explanation: 'terraform plan creates an execution plan by comparing the current state with the desired state defined in configuration files. It shows: resources to be created (+), resources to be modified (~), resources to be destroyed (-), resource dependencies and order, estimated changes without making actual changes, potential errors before applying, and cost estimation (with appropriate plugins). The plan phase is crucial for reviewing changes before implementation and enables approval workflows in CI/CD pipelines. It\'s a dry-run that helps prevent unwanted infrastructure changes. Reference: https://www.terraform.io/docs/cli/commands/plan.html',
            points: 1,
            answers: {
              create: [
                { text: 'Shows what actions Terraform will take by comparing current state with desired configuration', isCorrect: true },
                { text: 'Applies changes immediately to infrastructure without user confirmation', isCorrect: false },
                { text: 'Initializes a new Terraform workspace with default configuration files', isCorrect: false },
                { text: 'Validates syntax and formatting of Terraform configuration files only', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Terraform state and why is it important for infrastructure management?',
            explanation: 'Terraform state is a file that maps real-world resources to your configuration and keeps track of metadata. State importance includes: tracking resource relationships and dependencies, performance optimization by caching resource attributes, enabling collaboration through shared state, supporting resource drift detection, managing resource metadata and dependencies, enabling partial updates and targeted operations. State can be stored locally (terraform.tfstate) or remotely (S3, Azure Blob, Terraform Cloud). Remote state enables team collaboration and provides locking mechanisms. State contains sensitive information and should be secured appropriately. Reference: https://www.terraform.io/docs/language/state/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'A file that maps real resources to configuration, tracks metadata, and enables collaboration', isCorrect: true },
                { text: 'A temporary cache file that stores API responses for faster subsequent operations', isCorrect: false },
                { text: 'A log file that records all Terraform commands and their execution history', isCorrect: false },
                { text: 'A configuration backup that automatically restores infrastructure after failures', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Terraform modules and how do they promote code reusability?',
            explanation: 'Terraform modules are containers for multiple resources that are used together. They enable: code reusability across projects and environments, standardization of infrastructure patterns, abstraction of complex configurations, version control of infrastructure components, sharing of best practices across teams, simplified maintenance and updates, and composition of larger systems from smaller components. Modules can be sourced from local paths, Git repositories, Terraform Registry, or HTTP URLs. They accept input variables and provide output values, making them composable and flexible. Reference: https://www.terraform.io/docs/language/modules/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Containers for multiple resources that enable reusability, standardization, and abstraction', isCorrect: true },
                { text: 'Individual resource configurations that cannot be shared or reused across projects', isCorrect: false },
                { text: 'Database schemas that define the structure of Terraform state storage', isCorrect: false },
                { text: 'Network configurations that automatically handle load balancing and scaling', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between terraform apply and terraform destroy?',
            explanation: 'terraform apply creates or updates infrastructure to match the configuration, while terraform destroy removes all resources defined in the configuration. Key differences: apply implements the execution plan from terraform plan, creates/modifies resources as needed, updates state file with actual resource details, can be run with -auto-approve to skip confirmation, supports targeted applies with -target flag. destroy removes all tracked resources, requires confirmation (unless -auto-approve), updates state to reflect removed resources, cannot be easily undone, should be used carefully in production. Both commands modify state and require appropriate permissions. Reference: https://www.terraform.io/docs/cli/commands/apply.html',
            points: 1,
            answers: {
              create: [
                { text: 'apply creates/updates infrastructure to match configuration, destroy removes all tracked resources', isCorrect: true },
                { text: 'apply removes old resources, destroy creates new ones based on configuration', isCorrect: false },
                { text: 'apply validates configuration syntax, destroy executes the infrastructure deployment', isCorrect: false },
                { text: 'apply and destroy perform identical operations but in different cloud environments', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Terraform workspaces and when should you use them?',
            explanation: 'Terraform workspaces allow multiple states to be associated with a single configuration, enabling multiple environments from the same codebase. Use cases include: managing dev/staging/prod environments, feature branch testing, A/B testing infrastructure, temporary environments, and multi-tenant scenarios. Each workspace maintains separate state files, allowing isolation between environments. The terraform.workspace variable provides the current workspace name within configurations. However, workspaces have limitations: shared configuration means similar infrastructure, not suitable for completely different architectures, and can lead to complex conditional logic. Alternative approaches include separate directories or repositories for different environments. Reference: https://www.terraform.io/docs/language/state/workspaces.html',
            points: 1,
            answers: {
              create: [
                { text: 'Multiple states for single configuration, enabling environment isolation and multi-tenancy', isCorrect: true },
                { text: 'Separate Terraform installations for different cloud providers and regions', isCorrect: false },
                { text: 'User interface dashboards for visualizing infrastructure topology and dependencies', isCorrect: false },
                { text: 'Automated backup systems for Terraform state files and configuration history', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you handle sensitive data and secrets in Terraform configurations?',
            explanation: 'Handling sensitive data in Terraform requires multiple strategies: use sensitive = true for variable and output declarations to prevent display in logs, store secrets in external systems (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault), use terraform.tfvars files excluded from version control, leverage environment variables for sensitive inputs, implement remote state with encryption, use data sources to retrieve secrets at runtime rather than hardcoding, enable state file encryption and access controls, implement least-privilege access for Terraform execution, and audit secret access and usage. Never commit secrets to version control. Reference: https://www.terraform.io/docs/language/values/variables.html#suppressing-values-in-cli-output',
            points: 1,
            answers: {
              create: [
                { text: 'Use sensitive variables, external secret stores, encrypted remote state, and avoid version control', isCorrect: true },
                { text: 'Store all secrets directly in configuration files with basic password protection', isCorrect: false },
                { text: 'Use only environment variables without any additional security measures', isCorrect: false },
                { text: 'Hardcode secrets in modules since they are automatically encrypted by Terraform', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Terraform data sources and how do they differ from resources?',
            explanation: 'Data sources allow Terraform to read information from external sources without managing them. Key differences: Resources create/manage/destroy infrastructure components, while data sources only read existing information. Data sources are read-only and don\'t appear in state as manageable resources, they\'re used to fetch information about existing infrastructure (AMI IDs, subnet information, DNS records), they\'re evaluated during the plan phase, and they can be used to make configurations dynamic and environment-aware. Data sources enable referencing external resources, looking up dynamic values, and integrating with existing infrastructure not managed by Terraform. They\'re prefixed with "data" in configuration. Reference: https://www.terraform.io/docs/language/data-sources/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Read-only components that fetch information about existing infrastructure without managing it', isCorrect: true },
                { text: 'Manageable resources that create and destroy infrastructure components automatically', isCorrect: false },
                { text: 'Configuration templates that generate multiple similar resources with variations', isCorrect: false },
                { text: 'Backup mechanisms that store copies of resources for disaster recovery', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is terraform import and when would you use it?',
            explanation: 'terraform import allows you to bring existing infrastructure under Terraform management by importing real-world resources into your state file. Use cases include: adopting existing infrastructure, migrating from other IaC tools, recovering from state corruption, bringing manually created resources under management, and integrating with existing systems. The import process requires: writing configuration for the resource, running terraform import with resource address and ID, running terraform plan to verify configuration matches reality, and potentially updating configuration to match existing resource settings. Import only updates state; it doesn\'t generate configuration. Some resources may not support import. Reference: https://www.terraform.io/docs/cli/import/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Brings existing infrastructure under Terraform management by importing into state file', isCorrect: true },
                { text: 'Exports Terraform configuration to other infrastructure management tools', isCorrect: false },
                { text: 'Creates backup copies of infrastructure for disaster recovery purposes', isCorrect: false },
                { text: 'Automatically generates Terraform configuration from existing cloud resources', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Terraform provisioners and what are their limitations?',
            explanation: 'Provisioners execute scripts on local or remote machines as part of resource creation or destruction. Types include: local-exec (runs commands locally), remote-exec (runs commands on remote resources), and file (copies files to remote resources). However, provisioners have significant limitations: they\'re a "last resort" when native provider features aren\'t available, they make Terraform behavior less predictable, they can\'t be planned reliably, they don\'t have rollback capabilities, they break Terraform\'s declarative model, and they can cause state inconsistencies. Better alternatives include cloud-init, configuration management tools (Ansible, Chef, Puppet), or native provider features. Use provisioners sparingly and prefer immutable infrastructure patterns. Reference: https://www.terraform.io/docs/language/resources/provisioners/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Execute scripts during resource lifecycle but are "last resort" with reliability limitations', isCorrect: true },
                { text: 'Automatically provision optimal resource configurations based on workload analysis', isCorrect: false },
                { text: 'Manage user access and authentication for Terraform-managed resources', isCorrect: false },
                { text: 'Provide automated scaling and load balancing for infrastructure components', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Terraform in CI/CD pipelines with proper security and approval workflows?',
            explanation: 'Implementing Terraform in CI/CD requires: separating plan and apply stages with human approval gates, using service accounts with minimal required permissions, storing state remotely with locking and encryption, implementing proper secret management (never in code), using terraform validate and terraform fmt in pre-commit hooks, running terraform plan on pull requests with output as comments, requiring code reviews for infrastructure changes, implementing environment promotion workflows (dev → staging → prod), using workspace or directory separation for environments, enabling detailed logging and audit trails, implementing rollback strategies, and using Terraform Cloud/Enterprise for advanced workflows. Security considerations include state encryption, credential rotation, and least-privilege access. Reference: https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Separate plan/apply stages, service accounts, remote state, approval workflows, and security controls', isCorrect: true },
                { text: 'Fully automated deployment without human review or approval mechanisms', isCorrect: false },
                { text: 'Manual execution only without any CI/CD integration or automation capabilities', isCorrect: false },
                { text: 'Direct production deployment from developer machines using personal credentials', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the best practices for organizing Terraform code structure and file layout?',
            explanation: 'Terraform code organization best practices include: using consistent file naming (main.tf, variables.tf, outputs.tf, versions.tf), organizing by logical groupings rather than resource types, keeping environments in separate directories or repositories, using modules for reusable components, implementing proper variable and output naming conventions, adding comprehensive comments and documentation, using terraform fmt for consistent formatting, implementing .gitignore for sensitive files (.tfvars, .tfstate), organizing provider configurations centrally, separating data sources from resources, using locals for computed values, and maintaining README files for each module/environment. Directory structure should reflect organizational boundaries and blast radius considerations. Reference: https://www.terraform.io/docs/language/modules/develop/structure.html',
            points: 1,
            answers: {
              create: [
                { text: 'Consistent naming, logical groupings, environment separation, modules, documentation, and formatting', isCorrect: true },
                { text: 'Single large file containing all resources for easier management and deployment', isCorrect: false },
                { text: 'Alphabetical organization of all resources regardless of function or relationship', isCorrect: false },
                { text: 'Separate files for each individual resource to maximize granular control', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you handle Terraform state locking and what problems does it solve?',
            explanation: 'State locking prevents multiple concurrent Terraform operations from corrupting state. Implementation varies by backend: local state uses file locking, S3 uses DynamoDB for locking, Azure uses blob lease mechanisms, and Terraform Cloud provides built-in locking. Locking solves: concurrent modification conflicts, state corruption from simultaneous runs, lost updates from race conditions, and coordination issues in team environments. Features include: automatic locking during apply/destroy operations, manual locking for maintenance, lock timeout configurations, and force-unlock for emergency situations. Without locking, teams can experience data loss, inconsistent state, and infrastructure conflicts. Remote backends typically provide locking capabilities automatically. Reference: https://www.terraform.io/docs/language/state/locking.html',
            points: 1,
            answers: {
              create: [
                { text: 'Prevents concurrent operations from corrupting state through backend-specific locking mechanisms', isCorrect: true },
                { text: 'Encrypts state file contents to prevent unauthorized access to sensitive data', isCorrect: false },
                { text: 'Creates backup copies of state before each operation for rollback capabilities', isCorrect: false },
                { text: 'Compresses state files to reduce storage costs and improve transfer speeds', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Terraform expressions and functions, and how do they enable dynamic configurations?',
            explanation: 'Terraform expressions and functions enable dynamic, computed configurations. Expressions include: string interpolation ${...}, conditional expressions (condition ? true_val : false_val), for expressions for iteration, splat expressions (list.*.attribute), and dynamic blocks for repeated nested blocks. Built-in functions provide capabilities like: string manipulation (substr, replace, split), collection functions (length, concat, merge), encoding functions (base64encode, jsonencode), date/time functions (timestamp, formatdate), filesystem functions (file, templatefile), network functions (cidrsubnet, cidrhost), and cryptographic functions (md5, sha256). These enable: environment-specific configurations, resource naming patterns, complex data transformations, and conditional resource creation. Reference: https://www.terraform.io/docs/language/expressions/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Enable dynamic configurations through interpolation, conditionals, loops, and built-in functions', isCorrect: true },
                { text: 'Provide user interface components for visual configuration of infrastructure resources', isCorrect: false },
                { text: 'Handle network routing and load balancing for Terraform-managed infrastructure', isCorrect: false },
                { text: 'Manage version control integration and automatic deployment scheduling', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Terraform testing and validation strategies?',
            explanation: 'Terraform testing strategies include multiple levels: syntax validation with terraform validate, formatting checks with terraform fmt -check, plan validation to ensure successful planning, static analysis with tools like TFLint and Checkov, unit testing with Terratest or terraform-compliance, integration testing in temporary environments, policy validation with Sentinel or Open Policy Agent, security scanning with tools like Terrascan, drift detection to compare actual vs expected state, and automated testing in CI/CD pipelines. Testing approaches include: isolated test environments, test-driven infrastructure development, contract testing for modules, performance testing for large deployments, and disaster recovery testing. Implement testing at development, pre-commit, and deployment stages. Reference: https://www.terraform.io/docs/cli/commands/validate.html',
            points: 1,
            answers: {
              create: [
                { text: 'Multi-level approach including syntax validation, static analysis, unit testing, and policy validation', isCorrect: true },
                { text: 'Manual verification only after deployment to production environments', isCorrect: false },
                { text: 'Simple syntax checking without any functional or security validation', isCorrect: false },
                { text: 'Automated testing only for application code, not infrastructure configurations', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different Terraform backend types and their use cases?',
            explanation: 'Terraform backends determine where state is stored and operations are performed. Types include: Local backend (default) stores state locally, good for individual development but not team collaboration. Remote backends include: S3 with DynamoDB (AWS) for team collaboration with locking, Azure Storage with blob leases for Azure environments, Google Cloud Storage for GCP deployments, Terraform Cloud for SaaS state management with collaboration features, Consul for service discovery integration, etcd for Kubernetes environments, and HTTP for custom backend implementations. Backend selection considerations: team size, security requirements, compliance needs, integration requirements, cost considerations, and operational complexity. Migration between backends requires careful planning and state backup. Reference: https://www.terraform.io/docs/language/settings/backends/index.html',
            points: 1,
            answers: {
              create: [
                { text: 'Determine state storage location with options like local, S3, Azure, Terraform Cloud for different use cases', isCorrect: true },
                { text: 'Define the programming language and framework used for Terraform configuration files', isCorrect: false },
                { text: 'Specify the cloud provider APIs and authentication mechanisms for resource management', isCorrect: false },
                { text: 'Configure the user interface and visualization tools for infrastructure management', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage Terraform provider versions and ensure reproducible deployments?',
            explanation: 'Provider version management ensures reproducible deployments across environments. Strategies include: using terraform block with required_providers to specify version constraints, implementing version pinning for production environments (~> 1.0 for minor version flexibility, = 1.2.3 for exact versions), using .terraform.lock.hcl file to lock provider versions across team members, running terraform init -upgrade to update to latest allowed versions, testing provider upgrades in non-production environments first, documenting version compatibility requirements, implementing automated dependency updates with testing, using terraform providers lock to update lock file for multiple platforms, and maintaining consistent versions across environments. Version constraints syntax: >= 1.0 (minimum), ~> 1.0 (optimistic), >= 1.0, < 2.0 (range). Reference: https://www.terraform.io/docs/language/providers/requirements.html',
            points: 1,
            answers: {
              create: [
                { text: 'Use required_providers with version constraints, lock files, and consistent versioning across environments', isCorrect: true },
                { text: 'Always use the latest available provider versions without any version constraints', isCorrect: false },
                { text: 'Manually download and install specific provider versions for each deployment', isCorrect: false },
                { text: 'Version management is handled automatically by Terraform without user configuration', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded Terraform Associate certification with comprehensive questions`)
  return terraformAssociate
}
