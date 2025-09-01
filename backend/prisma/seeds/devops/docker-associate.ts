import { PrismaClient } from '../../../src/generated/prisma'

export async function seedDockerAssociate(prisma: PrismaClient, categoryId: number) {
  // Docker Certified Associate (DCA)
  const dockerAssociate = await prisma.certification.upsert({
    where: { slug: 'docker-associate' },
    update: {},
    create: {
      name: 'Docker Certified Associate (DCA)',
      description: 'Validates skills in containerization with Docker including image creation, container orchestration, networking, security, and Docker Enterprise administration. The DCA certification demonstrates proficiency in Docker fundamentals and production deployment strategies.',
      slug: 'docker-associate',
      level: 'Associate',
      duration: 90,
      questionsCount: 55,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the difference between Docker images and containers?',
            explanation: 'Docker images and containers have distinct characteristics: IMAGES: Read-only templates containing application code, dependencies, and filesystem, built from Dockerfile instructions, composed of layers for efficiency, stored in registries, immutable once created, used as blueprints for containers. CONTAINERS: Running instances of images, writable layer on top of image layers, isolated process with own filesystem/network/PID namespace, mutable during runtime, can be started/stopped/deleted, ephemeral by design. RELATIONSHIP: Image is the class, container is the instance. Multiple containers can run from same image. Container changes don\'t affect the original image. LAYERED FILESYSTEM: Images use union filesystem with copy-on-write, containers add writable layer on top, enables efficient storage and fast container startup. Reference: https://docs.docker.com/get-started/overview/',
            points: 1,
            answers: {
              create: [
                { text: 'Images: read-only templates/blueprints; Containers: running instances with writable layer', isCorrect: true },
                { text: 'Images and containers are identical terms referring to the same Docker concept', isCorrect: false },
                { text: 'Containers are permanent while images are temporary and deleted after use', isCorrect: false },
                { text: 'Images run applications while containers store the application code', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you optimize Docker image size and build performance?',
            explanation: 'Docker image optimization involves multiple strategies: LAYER OPTIMIZATION: Combine RUN commands to reduce layers, order instructions by change frequency (least to most frequent), use .dockerignore to exclude unnecessary files. MULTI-STAGE BUILDS: Separate build and runtime environments, copy only necessary artifacts, reduce final image size significantly. BASE IMAGE SELECTION: Use minimal base images (alpine, distroless), avoid full OS images when possible, choose language-specific lightweight images. CLEANUP: Remove package managers cache (apt-get clean, yum clean), remove temporary files, uninstall build dependencies in same layer. BUILD CACHE: Leverage Docker build cache, optimize layer caching, use --mount=type=cache for package managers. SECURITY: Use non-root users, minimize attack surface, scan for vulnerabilities, keep base images updated. TOOLS: Docker BuildKit for advanced features, dive tool for layer analysis, docker-slim for automatic optimization. Reference: https://docs.docker.com/develop/dev-best-practices/',
            points: 1,
            answers: {
              create: [
                { text: 'Multi-stage builds, minimal base images, layer optimization, cleanup, build cache, .dockerignore', isCorrect: true },
                { text: 'Always use the largest base images to ensure all dependencies are available', isCorrect: false },
                { text: 'Image size optimization is only important for development, not production deployments', isCorrect: false },
                { text: 'Docker automatically optimizes all images without requiring manual configuration', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Docker volumes and how do they differ from bind mounts?',
            explanation: 'Docker provides multiple options for persistent data storage: VOLUMES: Managed by Docker, stored in Docker area (/var/lib/docker/volumes), created and managed through Docker API, can be named or anonymous, support volume drivers for cloud storage, easier to backup and migrate, work across platforms. BIND MOUNTS: Mount host directory/file into container, full host path required, depend on host filesystem structure, direct host access, performance comparable to host filesystem. TMPFS MOUNTS: Stored in host memory, not persisted to disk, useful for temporary data, security for sensitive data. USE CASES: Volumes for persistent app data, databases, shared data between containers; Bind mounts for development, configuration files, host tool access. MANAGEMENT: docker volume create/ls/rm/prune, volume inspection, backup/restore strategies. BEST PRACTICES: Use volumes for production, bind mounts for development, proper permissions, security considerations, data backup strategies. Reference: https://docs.docker.com/storage/',
            points: 1,
            answers: {
              create: [
                { text: 'Volumes: Docker-managed, portable; Bind mounts: host filesystem, full path, development-friendly', isCorrect: true },
                { text: 'Volumes and bind mounts provide identical functionality with different naming only', isCorrect: false },
                { text: 'Bind mounts are always faster than volumes for all types of storage operations', isCorrect: false },
                { text: 'Volumes can only store configuration files while bind mounts handle application data', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Docker networking for container communication?',
            explanation: 'Docker networking enables container communication: NETWORK TYPES: Bridge (default, single host), Host (container uses host network), None (no networking), Overlay (multi-host with Swarm), Macvlan (assign MAC addresses). BRIDGE NETWORKS: Default docker0 bridge, custom bridge networks, container isolation, port publishing (-p), automatic DNS resolution between containers. CUSTOM NETWORKS: docker network create, better isolation, custom DNS, network policies, IP address management. CONTAINER CONNECTIVITY: Containers on same network can communicate by name, port exposure for external access, link containers (deprecated), environment variables for service discovery. ADVANCED FEATURES: Network aliases, multiple network attachment, ingress networking, load balancing. SECURITY: Network isolation, firewall rules, encrypted overlay networks, network policies. TROUBLESHOOTING: docker network ls/inspect, container networking namespace, port binding verification, connectivity testing. BEST PRACTICES: Use custom networks, avoid default bridge, implement network security, monitor network performance. Reference: https://docs.docker.com/network/',
            points: 1,
            answers: {
              create: [
                { text: 'Bridge, host, overlay networks; custom networks for isolation; DNS resolution; port publishing', isCorrect: true },
                { text: 'All containers share the same network interface without any isolation options', isCorrect: false },
                { text: 'Docker networking only works within single host and cannot span multiple machines', isCorrect: false },
                { text: 'Network configuration is handled entirely by the host OS without Docker involvement', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Docker Compose and how do you use it for multi-container applications?',
            explanation: 'Docker Compose orchestrates multi-container applications: PURPOSE: Define and run multi-container applications, YAML configuration files, service definitions, dependency management, development workflow simplification. COMPOSE FILE: docker-compose.yml defines services, networks, volumes, environment variables, build contexts, port mappings. SERVICES: Each service represents a containerized application, can specify image or build context, scaling support, health checks, restart policies. NETWORKING: Automatic network creation, service discovery by name, external networks, network aliases, port publishing. VOLUMES: Data persistence, shared volumes between services, bind mounts, named volumes. COMMANDS: docker-compose up/down, build, logs, ps, exec, scale, pull. ENVIRONMENTS: Multiple compose files (docker-compose.override.yml), environment-specific configurations, variable substitution. PRODUCTION: Docker Compose vs Kubernetes/Swarm, scaling limitations, single-host deployment. BEST PRACTICES: Version control compose files, use .env files, health checks, proper dependency ordering, resource limits. Reference: https://docs.docker.com/compose/',
            points: 1,
            answers: {
              create: [
                { text: 'YAML-based multi-container orchestration, service definitions, networking, volumes, development workflow', isCorrect: true },
                { text: 'Docker Compose is only for single-container applications with complex configurations', isCorrect: false },
                { text: 'Compose files are binary configurations that cannot be version controlled', isCorrect: false },
                { text: 'Docker Compose requires separate installation and cannot use existing Docker daemon', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement container security best practices?',
            explanation: 'Container security involves multiple layers: IMAGE SECURITY: Use trusted base images, scan for vulnerabilities, keep images updated, minimal attack surface, non-root users, read-only filesystems. RUNTIME SECURITY: Resource limits, security contexts, capability dropping, SELinux/AppArmor profiles, seccomp filters, no privileged containers. NETWORK SECURITY: Network segmentation, firewall rules, encrypted communication, service mesh for microservices, network policies. SECRET MANAGEMENT: External secret stores, avoid secrets in images, runtime secret injection, secret rotation. ACCESS CONTROL: RBAC implementation, least privilege principle, user namespaces, container isolation. MONITORING: Security scanning, runtime monitoring, anomaly detection, audit logging, compliance reporting. TOOLS: Docker Bench Security, Clair, Twistlock, Aqua Security, Falco for runtime security. COMPLIANCE: CIS benchmarks, regulatory requirements, security policies, vulnerability management. HOST SECURITY: Secure Docker daemon, TLS encryption, regular updates, minimal host OS. Reference: https://docs.docker.com/engine/security/',
            points: 1,
            answers: {
              create: [
                { text: 'Image scanning, non-root users, resource limits, network security, secret management, monitoring', isCorrect: true },
                { text: 'Security is only relevant for production environments, not development containers', isCorrect: false },
                { text: 'Running all containers as root provides the best compatibility and performance', isCorrect: false },
                { text: 'Container security is handled entirely by the host OS without container-specific measures', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is Docker Swarm and how does it differ from Kubernetes?',
            explanation: 'Docker Swarm is Docker\'s native orchestration platform: DOCKER SWARM: Built into Docker Engine, simple setup and management, service-based deployments, ingress load balancing, secrets management, rolling updates. ARCHITECTURE: Manager nodes (raft consensus), worker nodes, overlay networking, service mesh, global/replicated services. KEY FEATURES: Docker-native, simple YAML, automatic load balancing, built-in security, service discovery, rolling updates, scaling. KUBERNETES: More complex, powerful ecosystem, declarative configuration, extensive third-party integrations, advanced scheduling, custom resources. COMPARISON: Swarm simpler to learn/operate, Kubernetes more features/flexibility, Swarm better for Docker-centric environments, Kubernetes for complex microservices, Swarm has Docker CLI integration, Kubernetes separate kubectl. MIGRATION: Docker Stack Deploy, Compose file compatibility, service migration strategies. PRODUCTION: Swarm suitable for smaller deployments, Kubernetes for enterprise scale, hybrid approaches possible. DECISION FACTORS: Team expertise, application complexity, ecosystem requirements, operational overhead, vendor support. Reference: https://docs.docker.com/engine/swarm/',
            points: 1,
            answers: {
              create: [
                { text: 'Swarm: Docker-native, simple; Kubernetes: complex, feature-rich; different use cases and complexity levels', isCorrect: true },
                { text: 'Docker Swarm and Kubernetes provide identical functionality and can be used interchangeably', isCorrect: false },
                { text: 'Kubernetes is deprecated in favor of Docker Swarm for all container orchestration needs', isCorrect: false },
                { text: 'Docker Swarm requires Kubernetes installation and cannot operate independently', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement health checks and monitoring for Docker containers?',
            explanation: 'Container health checks and monitoring ensure application reliability: DOCKERFILE HEALTHCHECK: HEALTHCHECK instruction defines check command, interval, timeout, retries configuration, application-specific validation. DOCKER HEALTHCHECK: docker run --health-cmd, --health-interval, --health-retries options, container status reporting, automatic restart policies. MONITORING STRATEGIES: Application metrics collection, resource utilization monitoring, log aggregation, distributed tracing, APM integration. TOOLS: Prometheus for metrics, Grafana for visualization, ELK stack for logs, Jaeger for tracing, Docker Stats API. HEALTH CHECK PATTERNS: HTTP endpoint checks, database connectivity, dependency verification, custom validation scripts, deep vs shallow checks. ORCHESTRATOR INTEGRATION: Docker Swarm service health, Kubernetes liveness/readiness probes, load balancer health checks, service discovery. ALERTING: Threshold-based alerts, anomaly detection, escalation procedures, runbook automation, incident response. BEST PRACTICES: Lightweight checks, appropriate intervals, graceful degradation, circuit breakers, comprehensive monitoring stack. TROUBLESHOOTING: Log analysis, metric correlation, distributed tracing, container inspection, debugging techniques. Reference: https://docs.docker.com/engine/reference/builder/#healthcheck',
            points: 1,
            answers: {
              create: [
                { text: 'HEALTHCHECK instruction, monitoring tools (Prometheus/Grafana), HTTP checks, orchestrator integration', isCorrect: true },
                { text: 'Health checks are only available in Kubernetes and not supported by Docker directly', isCorrect: false },
                { text: 'Container monitoring requires specialized hardware and cannot use standard server resources', isCorrect: false },
                { text: 'Health checks automatically fix application issues without requiring manual intervention', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage Docker registries and image distribution?',
            explanation: 'Docker registries manage image storage and distribution: REGISTRY TYPES: Docker Hub (public), private registries (Harbor, Nexus, GitLab), cloud registries (ECR, ACR, GCR), self-hosted registry. DOCKER HUB: Public/private repositories, automated builds, webhooks, organizations, teams, vulnerability scanning. PRIVATE REGISTRIES: Docker Registry 2.0, Harbor with UI and security, Nexus Repository, GitLab Container Registry, authentication and authorization. AUTHENTICATION: Username/password, service accounts, token-based, OIDC integration, registry credentials management. IMAGE MANAGEMENT: Tagging strategies (semantic versioning, latest, environment tags), image signing, vulnerability scanning, cleanup policies. DISTRIBUTION: Docker Content Trust, image layers, delta uploads, registry mirrors, content delivery networks. SECURITY: TLS encryption, access controls, image scanning, policy enforcement, audit logging, compliance requirements. AUTOMATION: CI/CD integration, automated builds, image promotion pipelines, registry webhooks, notification systems. BEST PRACTICES: Immutable tags, security scanning, access controls, backup strategies, monitoring registry health. Reference: https://docs.docker.com/registry/',
            points: 1,
            answers: {
              create: [
                { text: 'Public/private registries, authentication, tagging strategies, security scanning, CI/CD integration', isCorrect: true },
                { text: 'All Docker images must be stored in Docker Hub and cannot use private registries', isCorrect: false },
                { text: 'Image distribution requires manual copying between registries without automation capabilities', isCorrect: false },
                { text: 'Registry management is handled automatically by Docker without configuration options', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are Docker secrets and how do you manage sensitive data in containers?',
            explanation: 'Docker secrets provide secure sensitive data management: DOCKER SWARM SECRETS: Encrypted at rest and in transit, mounted as in-memory filesystem, automatic rotation support, RBAC access control, service-based assignment. SECRET CREATION: docker secret create from file/stdin, versioning support, immutable after creation, removal and recreation for updates. USAGE: Services access secrets via --secret flag, mounted at /run/secrets/<secret-name>, not visible in container filesystem, process environment separation. EXTERNAL SECRET MANAGEMENT: Integration with HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, Kubernetes secrets, custom secret providers. BEST PRACTICES: Never include secrets in images, use external secret stores, rotate regularly, least privilege access, audit secret usage. ALTERNATIVE APPROACHES: Environment variables (less secure), bind mounts (development), init containers for secret retrieval, sidecar pattern for secret management. SECURITY CONSIDERATIONS: Encryption in transit and at rest, access controls, secret scanning, compliance requirements, secret lifecycle management. TROUBLESHOOTING: Secret mount verification, permission issues, service deployment failures, secret rotation testing. Reference: https://docs.docker.com/engine/swarm/secrets/',
            points: 1,
            answers: {
              create: [
                { text: 'Swarm secrets: encrypted, in-memory mount, RBAC; external secret stores; avoid secrets in images', isCorrect: true },
                { text: 'Docker secrets can only be used with Kubernetes and not with Docker Swarm', isCorrect: false },
                { text: 'All sensitive data should be stored in environment variables for easy access', isCorrect: false },
                { text: 'Secrets are automatically shared among all containers without access control', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Docker logging and log management strategies?',
            explanation: 'Docker logging enables application monitoring and troubleshooting: LOGGING DRIVERS: json-file (default), syslog, journald, fluentd, awslogs, splunk, gelf, none, local drivers. LOG CONFIGURATION: docker run --log-driver, --log-opt for options, daemon.json for defaults, service-level configuration in Swarm/Compose. JSON-FILE DRIVER: Local file storage, log rotation (max-size, max-file), timestamping, structured format. CENTRALIZED LOGGING: ELK Stack (Elasticsearch, Logstash, Kibana), Fluentd/Fluent Bit, Splunk, cloud logging services (CloudWatch, Azure Monitor). LOG AGGREGATION: Sidecar containers, log shipping agents, direct driver integration, streaming to external systems. STRUCTURED LOGGING: JSON format, consistent fields, correlation IDs, log levels, contextual information. BEST PRACTICES: Proper log levels, avoid logging sensitive data, log rotation, centralized collection, monitoring and alerting. TROUBLESHOOTING: docker logs command, log driver debugging, connectivity issues, performance impact, storage management. ANALYSIS: Log correlation, pattern detection, error tracking, performance monitoring, business intelligence. Reference: https://docs.docker.com/config/containers/logging/',
            points: 1,
            answers: {
              create: [
                { text: 'Multiple drivers (json-file, syslog, fluentd), centralized logging (ELK), structured format, rotation', isCorrect: true },
                { text: 'Docker containers cannot generate logs and all logging must be handled externally', isCorrect: false },
                { text: 'All container logs are automatically sent to system logs without configuration options', isCorrect: false },
                { text: 'Log management requires separate container orchestration platforms like Kubernetes', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you troubleshoot Docker container and networking issues?',
            explanation: 'Docker troubleshooting requires systematic investigation: CONTAINER TROUBLESHOOTING: docker logs for application logs, docker exec for interactive access, docker inspect for detailed info, docker stats for resource usage, container exit codes analysis. NETWORKING ISSUES: docker network ls/inspect, port binding verification (docker port), connectivity testing (ping, telnet, curl), DNS resolution testing, firewall rules checking. PERFORMANCE PROBLEMS: Resource constraints (CPU, memory limits), disk I/O issues, network latency, container overhead analysis, host system performance. COMMON ISSUES: Image not found, port conflicts, volume mounting problems, permission issues, resource exhaustion, networking configuration. DEBUGGING TOOLS: docker system events for real-time events, docker system df for disk usage, docker system prune for cleanup, nsenter for namespace debugging. ADVANCED DEBUGGING: Container namespace inspection, cgroup analysis, strace for system calls, tcpdump for network analysis, performance profiling tools. HEALTH MONITORING: Container health checks, resource monitoring, log analysis, metric collection, alerting systems. BEST PRACTICES: Systematic approach, log correlation, environment comparison, documentation of solutions, preventive monitoring. Reference: https://docs.docker.com/config/containers/logging/configure/',
            points: 1,
            answers: {
              create: [
                { text: 'Logs, exec, inspect, stats; network troubleshooting; performance analysis; systematic debugging approach', isCorrect: true },
                { text: 'Container issues can only be resolved by restarting the entire Docker daemon', isCorrect: false },
                { text: 'Networking problems are always caused by firewall rules and cannot have other causes', isCorrect: false },
                { text: 'Docker troubleshooting requires specialized debugging containers that must be pre-installed', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the Docker build process and how do you optimize Dockerfile instructions?',
            explanation: 'Docker build process creates images from Dockerfiles: BUILD PROCESS: Docker daemon reads Dockerfile, executes instructions sequentially, creates intermediate layers, final image with combined layers, build context sent to daemon. DOCKERFILE INSTRUCTIONS: FROM (base image), RUN (execute commands), COPY/ADD (files), WORKDIR (working directory), EXPOSE (ports), CMD/ENTRYPOINT (startup), ENV (environment), USER (security). LAYER OPTIMIZATION: Each instruction creates layer, combine RUN commands, order by change frequency, use multi-stage builds, leverage build cache. BUILD CACHE: Docker caches layers, invalidated by changes, use --no-cache to bypass, optimize instruction order for cache efficiency. MULTI-STAGE BUILDS: Separate build and runtime stages, copy artifacts between stages, reduce final image size, security improvements. BEST PRACTICES: Minimal base images, non-root user, .dockerignore file, combine commands, remove unnecessary files, pin package versions. BUILDKIT: Advanced build features, parallel execution, cache mounts, secret mounts, better performance, syntax improvements. BUILD CONTEXT: Files sent to daemon, .dockerignore reduces context, remote contexts (Git, HTTP), build-time arguments. Reference: https://docs.docker.com/engine/reference/builder/',
            points: 1,
            answers: {
              create: [
                { text: 'Sequential instruction execution, layer creation, build cache, multi-stage builds, context optimization', isCorrect: true },
                { text: 'Docker builds execute all instructions simultaneously for maximum performance', isCorrect: false },
                { text: 'Each Dockerfile instruction creates a new container that runs independently', isCorrect: false },
                { text: 'Build optimization is only relevant for large applications, not small containers', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement container orchestration and service discovery?',
            explanation: 'Container orchestration manages distributed container applications: SERVICE DISCOVERY: DNS-based resolution, service registries (Consul, etcd), load balancer integration, environment variables, container networking. DOCKER SWARM: Built-in orchestration, service definitions, ingress networking, automatic load balancing, rolling updates, health checks. KUBERNETES INTEGRATION: Docker as container runtime, pod management, service abstraction, ingress controllers, custom resources. SERVICE MESH: Istio, Linkerd for advanced networking, traffic management, security policies, observability, circuit breakers. LOAD BALANCING: Layer 4/7 load balancing, health-based routing, session affinity, failover mechanisms, traffic distribution. SCALING: Horizontal scaling, auto-scaling policies, resource-based scaling, custom metrics, performance monitoring. HIGH AVAILABILITY: Multi-zone deployment, redundancy, failover strategies, disaster recovery, data replication. DEPLOYMENT STRATEGIES: Blue-green deployments, rolling updates, canary releases, A/B testing, feature toggles. MONITORING: Service health monitoring, distributed tracing, metrics collection, alerting, capacity planning. BEST PRACTICES: Immutable deployments, stateless services, proper health checks, resource limits, security policies. Reference: https://docs.docker.com/engine/swarm/services/',
            points: 1,
            answers: {
              create: [
                { text: 'DNS service discovery, Swarm/K8s orchestration, service mesh, load balancing, scaling, HA strategies', isCorrect: true },
                { text: 'Service discovery requires manual IP address management without automated resolution', isCorrect: false },
                { text: 'Container orchestration is only possible with cloud-managed services, not self-hosted', isCorrect: false },
                { text: 'All containers must be stateful and cannot benefit from orchestration platforms', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage Docker daemon configuration and system resources?',
            explanation: 'Docker daemon configuration controls system behavior: DAEMON CONFIGURATION: /etc/docker/daemon.json file, systemd service configuration, runtime options, logging configuration, storage driver settings. STORAGE DRIVERS: overlay2 (recommended), aufs, devicemapper, btrfs, zfs, vfs, performance and compatibility considerations. RESOURCE MANAGEMENT: Memory limits, CPU limits, disk space management, ulimits configuration, cgroup settings. NETWORKING: Default bridge configuration, DNS settings, IP address management, MTU settings, IPv6 support. SECURITY SETTINGS: TLS configuration, user namespace mapping, seccomp profiles, AppArmor/SELinux, rootless mode. REGISTRY CONFIGURATION: Insecure registries, registry mirrors, pull limits, authentication configuration. LOGGING: Default logging driver, log rotation, centralized logging, audit logging. MONITORING: Metrics endpoint, Prometheus integration, health checks, performance monitoring. MAINTENANCE: System pruning, log rotation, update procedures, backup strategies, troubleshooting tools. BEST PRACTICES: Resource limits, security hardening, monitoring setup, regular maintenance, configuration management. Reference: https://docs.docker.com/engine/reference/commandline/dockerd/',
            points: 1,
            answers: {
              create: [
                { text: 'daemon.json configuration, storage drivers, resource limits, security settings, monitoring setup', isCorrect: true },
                { text: 'Docker daemon configuration is fixed and cannot be modified after installation', isCorrect: false },
                { text: 'All daemon settings must be configured through command-line flags only', isCorrect: false },
                { text: 'Resource management is handled automatically without requiring administrator configuration', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded Docker Associate certification with comprehensive questions`)
  return dockerAssociate
}
