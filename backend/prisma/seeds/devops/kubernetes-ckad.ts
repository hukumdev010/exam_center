import { PrismaClient } from '../../../src/generated/prisma'

export async function seedKubernetesCKAD(prisma: PrismaClient, categoryId: number) {
  // Certified Kubernetes Application Developer (CKAD)
  const kubernetesCKAD = await prisma.certification.upsert({
    where: { slug: 'kubernetes-ckad' },
    update: {},
    create: {
      name: 'Certified Kubernetes Application Developer (CKAD)',
      description: 'Validates skills in designing, building, and deploying cloud-native applications on Kubernetes. The CKAD certification focuses on application development, configuration, debugging, and lifecycle management within Kubernetes environments.',
      slug: 'kubernetes-ckad',
      level: 'Professional',
      duration: 120,
      questionsCount: 19,
      categoryId,
      questions: {
        create: [
          {
            text: 'How do you create and configure multi-container pods in Kubernetes?',
            explanation: 'Multi-container pods enable tight coupling of containers that need to share resources. Common patterns: SIDECAR (helper container, logging agent), AMBASSADOR (proxy container for external services), ADAPTER (transform output format). Configuration involves: shared volumes for data exchange, shared network namespace (localhost communication), coordinated lifecycle management, resource sharing considerations. Example: main application container + logging sidecar, web server + SSL termination proxy. Benefits include: shared storage, network, process namespace, atomic scheduling, simplified communication. Design considerations: container responsibilities, resource allocation, startup dependencies, health checks, and security boundaries. Multi-container pods are scheduled as single units. Reference: https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/',
            points: 1,
            answers: {
              create: [
                { text: 'Multiple containers in single pod sharing network/storage, using sidecar/ambassador/adapter patterns', isCorrect: true },
                { text: 'Each container must run in separate pods with network communication between them', isCorrect: false },
                { text: 'Multi-container functionality requires special multi-container deployment resources', isCorrect: false },
                { text: 'Containers in same pod run on different nodes for high availability', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement health checks using liveness, readiness, and startup probes?',
            explanation: 'Kubernetes health check probes ensure application reliability: LIVENESS PROBE: Determines if container is running, restarts container on failure, checks application deadlocks/hangs, should be lightweight and fast. READINESS PROBE: Determines if pod is ready to receive traffic, removes from service endpoints on failure, handles application startup/configuration loading, temporary unavailability. STARTUP PROBE: For slow-starting containers, disables liveness/readiness during startup, prevents premature restarts, long initialDelaySeconds alternative. PROBE TYPES: HTTP GET (httpGet), TCP Socket (tcpSocket), Command execution (exec). CONFIGURATION: initialDelaySeconds, periodSeconds, timeoutSeconds, successThreshold, failureThreshold. BEST PRACTICES: Different endpoints for different probes, avoid expensive operations, proper timeout values, graceful degradation handling. Reference: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/',
            points: 1,
            answers: {
              create: [
                { text: 'Liveness: restart on failure; Readiness: traffic routing; Startup: slow containers; HTTP/TCP/exec probe types', isCorrect: true },
                { text: 'All three probe types perform identical functions with different naming conventions', isCorrect: false },
                { text: 'Health checks are only available for single-container pods, not multi-container setups', isCorrect: false },
                { text: 'Probes only work with HTTP-based applications, not with databases or other services', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you configure resource requests and limits for containers?',
            explanation: 'Resource management ensures predictable application performance: REQUESTS: Guaranteed resources, used for scheduling decisions, affects Quality of Service class, minimum resources required. LIMITS: Maximum resources allowed, prevents resource hogging, triggers throttling (CPU) or OOMKilled (memory), upper boundary for consumption. UNITS: CPU in millicores (m) or cores, Memory in bytes (Ki, Mi, Gi). QOS CLASSES: Guaranteed (requests=limits), Burstable (requests<limits), BestEffort (no requests/limits). CONFIGURATION: resources.requests.cpu/memory, resources.limits.cpu/memory in container specs. BEST PRACTICES: Set requests based on baseline usage, limits based on maximum acceptable usage, monitor actual consumption, avoid over-commitment, use horizontal pod autoscaler, consider node capacity. LimitRange can set defaults. Reference: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/',
            points: 1,
            answers: {
              create: [
                { text: 'Requests: guaranteed minimum, scheduling basis; Limits: maximum allowed, prevents overconsumption; affects QoS', isCorrect: true },
                { text: 'Requests and limits are only suggestions and not enforced by the Kubernetes scheduler', isCorrect: false },
                { text: 'Resource configuration applies only to the entire pod, not individual containers', isCorrect: false },
                { text: 'Only memory limits are enforced while CPU limits are purely informational', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you use init containers for application initialization tasks?',
            explanation: 'Init containers run before app containers and complete successfully before app containers start: USE CASES: Database schema setup, waiting for dependencies, downloading configuration, security setup, environment preparation, data seeding. CHARACTERISTICS: Run sequentially, must complete successfully, share volumes with app containers, separate images from app containers, restart policy affects behavior. PATTERNS: Wait for database availability, clone git repositories, register with service discovery, download certificates, apply database migrations. CONFIGURATION: initContainers section in pod spec, same container specification as regular containers. ADVANTAGES: Separation of concerns, reusable initialization logic, clean app container startup, dependency management. TROUBLESHOOTING: Check init container logs, ensure proper completion, verify shared volume data, check network connectivity for dependencies. Multiple init containers run in sequence. Reference: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/',
            points: 1,
            answers: {
              create: [
                { text: 'Run before app containers, handle initialization tasks, must complete successfully, run sequentially', isCorrect: true },
                { text: 'Init containers run in parallel with application containers for performance optimization', isCorrect: false },
                { text: 'Init containers are optional and application containers can start without them completing', isCorrect: false },
                { text: 'Init containers can only perform network operations, not file system or database tasks', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Jobs and CronJobs for batch processing and scheduled tasks?',
            explanation: 'Jobs and CronJobs manage batch workloads and scheduled tasks: JOBS: Run pods to completion, handle batch processing, ensure successful completion, support parallelism, restart policies for failures. Types: Non-parallel (single completion), parallel with fixed completion count, parallel work queue. CRONJOBS: Schedule-based job execution, cron syntax for timing, manage job history, handle concurrency policies. JOB CONFIGURATION: completions (successful pods needed), parallelism (concurrent pods), activeDeadlineSeconds (timeout), backoffLimit (retry attempts). CRONJOB CONFIGURATION: schedule (cron format), concurrencyPolicy (Allow, Forbid, Replace), successfulJobsHistoryLimit, failedJobsHistoryLimit. BEST PRACTICES: Idempotent operations, proper error handling, resource limits, cleanup policies, monitoring job status. PATTERNS: Data processing, report generation, database backups, ETL operations, maintenance tasks. Reference: https://kubernetes.io/docs/concepts/workloads/controllers/job/',
            points: 1,
            answers: {
              create: [
                { text: 'Jobs: run to completion, parallelism support; CronJobs: scheduled execution, cron syntax, concurrency policies', isCorrect: true },
                { text: 'Jobs and CronJobs can only run single-container pods without initialization support', isCorrect: false },
                { text: 'CronJobs automatically retry failed jobs indefinitely without configuration options', isCorrect: false },
                { text: 'Batch processing requires specialized batch controller resources, not standard Jobs', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you debug and troubleshoot application issues in Kubernetes?',
            explanation: 'Kubernetes debugging involves systematic investigation: BASIC COMMANDS: kubectl get pods, kubectl describe pod, kubectl logs <pod>, kubectl exec -it <pod> -- /bin/bash, kubectl port-forward for local access. LOG INVESTIGATION: Container logs, previous container logs (--previous), multi-container pod logs (-c container), follow logs (-f), timestamps (--timestamps). POD TROUBLESHOOTING: Check events, resource constraints, image pull issues, liveness/readiness probes, network connectivity. ADVANCED DEBUGGING: Debug running pods, attach to processes, network troubleshooting with netcat/curl, DNS resolution testing. DEBUGGING TOOLS: kubectl top for resources, describe for events, get with wide output, custom columns, debug containers (kubectl debug). PATTERNS: Application crashes, network issues, storage problems, configuration errors, performance issues. Set up monitoring and alerting for proactive issue detection. Reference: https://kubernetes.io/docs/tasks/debug-application-cluster/debug-application/',
            points: 1,
            answers: {
              create: [
                { text: 'Use kubectl logs, describe, exec, port-forward; check events, resources, probes; debug containers', isCorrect: true },
                { text: 'Debugging requires direct access to worker nodes and bypassing Kubernetes abstractions', isCorrect: false },
                { text: 'Application issues can only be debugged by recreating pods and checking startup logs', isCorrect: false },
                { text: 'Kubernetes provides automatic issue resolution without manual debugging intervention', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you use volumes for persistent data storage in applications?',
            explanation: 'Kubernetes volumes provide persistent storage for applications: VOLUME TYPES: EmptyDir (pod lifetime), HostPath (node directory), PersistentVolume (cluster storage), ConfigMap/Secret (configuration data), Cloud volumes (EBS, GCE PD), Network storage (NFS, Ceph). PERSISTENT VOLUMES: Cluster-wide storage resources, independent lifecycle, various storage backends, access modes (ReadWriteOnce, ReadOnlyMany, ReadWriteMany). PERSISTENT VOLUME CLAIMS: User storage requests, bind to available PVs, specify size and access modes, used in pod specifications. STORAGE CLASSES: Dynamic provisioning, different storage tiers, cloud provider integration, parameter specification. VOLUME MOUNTING: volumeMounts in containers, volumes in pod spec, subPath for specific directories. PATTERNS: Database storage, shared configuration, logs collection, temporary processing space. BEST PRACTICES: Use appropriate volume types, implement backup strategies, monitor storage usage, set storage quotas. Reference: https://kubernetes.io/docs/concepts/storage/volumes/',
            points: 1,
            answers: {
              create: [
                { text: 'Various types: EmptyDir, PVs/PVCs, ConfigMap; support different lifecycles and access modes', isCorrect: true },
                { text: 'All volumes are automatically persistent and survive pod deletions without configuration', isCorrect: false },
                { text: 'Volume mounting is only possible with specialized storage controller deployments', isCorrect: false },
                { text: 'Kubernetes volumes can only store configuration data, not application-generated content', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement environment-specific configuration using ConfigMaps and Secrets?',
            explanation: 'ConfigMaps and Secrets enable environment-specific configuration: CONFIGMAPS: Store non-confidential configuration data, key-value pairs or files, environment variables or mounted files, hot-reload configuration changes, namespace-scoped resources. SECRETS: Store sensitive information (passwords, tokens, keys), base64 encoded, encrypted at rest, various types (Opaque, TLS, Docker registry), RBAC protection. USAGE PATTERNS: Environment variables (envFrom, env), volume mounts (files), command line arguments through env vars. ENVIRONMENT STRATEGIES: Separate ConfigMaps per environment, environment-specific values, staging vs production configurations, feature flags, database connection strings. BEST PRACTICES: Never hardcode sensitive data, use external secret management, implement secret rotation, validate configurations, version configurations with applications. SECURITY: Limit secret access, use least privilege RBAC, audit secret usage, implement secret scanning. Reference: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/',
            points: 1,
            answers: {
              create: [
                { text: 'ConfigMaps: non-sensitive config; Secrets: sensitive data; env vars or file mounts; environment separation', isCorrect: true },
                { text: 'All configuration must be embedded in container images for proper environment isolation', isCorrect: false },
                { text: 'Secrets and ConfigMaps are identical and can be used interchangeably for any data type', isCorrect: false },
                { text: 'Environment-specific configuration requires separate clusters for each environment', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement autoscaling with Horizontal Pod Autoscaler (HPA)?',
            explanation: 'Horizontal Pod Autoscaler automatically scales replicas based on metrics: METRICS: CPU utilization (default), memory utilization, custom metrics (from applications), external metrics (from monitoring systems), multiple metrics support. CONFIGURATION: Target resource (Deployment, ReplicaSet), min/max replicas, target metric values, scale-up/down policies. REQUIREMENTS: Metrics Server installed, resource requests defined on containers, proper application architecture for scaling. HPA ALGORITHM: Current utilization vs target, calculates desired replicas, respects min/max boundaries, stabilization windows to prevent flapping. CUSTOM METRICS: Application-specific metrics (queue length, request rate), external metrics (cloud monitoring), custom metric APIs. BEST PRACTICES: Set appropriate min/max replicas, define realistic targets, monitor scaling events, use multiple metrics, implement graceful shutdown, test scaling behavior. TROUBLESHOOTING: Check metrics availability, verify resource requests, examine HPA events, validate metric queries. Reference: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/',
            points: 1,
            answers: {
              create: [
                { text: 'Automatically scales replicas based on CPU, memory, or custom metrics; requires Metrics Server and resource requests', isCorrect: true },
                { text: 'HPA only works with CPU metrics and cannot use memory or custom application metrics', isCorrect: false },
                { text: 'Autoscaling requires manual intervention to trigger scaling decisions based on alerts', isCorrect: false },
                { text: 'HPA scales nodes instead of pods and requires cluster autoscaler integration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you use labels and selectors for resource organization and service discovery?',
            explanation: 'Labels and selectors enable resource organization and service discovery: LABELS: Key-value pairs attached to objects, organize and categorize resources, enable flexible queries, immutable after creation for some resources. LABEL CONVENTIONS: app, version, component, environment, tier, release, instance, managed-by. SELECTORS: Equality-based (=, !=), set-based (in, notin, exists), match exact values or sets. USES: Service endpoints (matching pods), Deployments managing ReplicaSets, Network Policies targeting pods, Node selectors for scheduling. SERVICE DISCOVERY: Services use selectors to find backend pods, automatic endpoint updates, load balancing across matching pods. BEST PRACTICES: Consistent labeling strategy, meaningful names, avoid system-reserved prefixes, document label schema, use recommended labels. ORGANIZATION: Environment separation, application grouping, version management, component identification. OPERATIONAL: Monitoring queries, alerting rules, resource cleanup, batch operations. Reference: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/',
            points: 1,
            answers: {
              create: [
                { text: 'Key-value metadata for organization; selectors match resources; enable service discovery and operations', isCorrect: true },
                { text: 'Labels are only for human-readable documentation and not used by Kubernetes controllers', isCorrect: false },
                { text: 'Selectors can only use exact string matching without pattern or set-based operations', isCorrect: false },
                { text: 'Labels are automatically generated by Kubernetes and cannot be manually specified', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement pod security contexts and security policies?',
            explanation: 'Security contexts define security settings for pods and containers: POD SECURITY CONTEXT: Applies to all containers, sets user/group IDs (runAsUser, runAsGroup), file system permissions (fsGroup), supplemental groups, SELinux context, Windows options. CONTAINER SECURITY CONTEXT: Overrides pod context, specific to individual containers, capabilities management, privileged mode, read-only root filesystem. SECURITY SETTINGS: runAsNonRoot (prevent root execution), allowPrivilegeEscalation (prevent privilege escalation), capabilities (add/drop Linux capabilities), seccomp profiles, AppArmor profiles. POD SECURITY STANDARDS: Privileged, Baseline, Restricted policies, namespace-level enforcement, admission controller validation. BEST PRACTICES: Run as non-root users, drop unnecessary capabilities, use read-only filesystems, implement security scanning, regular security updates, principle of least privilege. COMPLIANCE: Security benchmarks, regulatory requirements, vulnerability management, security monitoring. Reference: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/',
            points: 1,
            answers: {
              create: [
                { text: 'Define user/group IDs, capabilities, privileged mode, read-only filesystem; pod and container levels', isCorrect: true },
                { text: 'Security contexts only apply to container runtime security, not Kubernetes-level policies', isCorrect: false },
                { text: 'All pods run with identical security settings that cannot be customized per application', isCorrect: false },
                { text: 'Security policies are only enforced by external security tools, not Kubernetes natively', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you expose applications using Services and Ingress?',
            explanation: 'Services and Ingress provide application exposure and traffic routing: SERVICES: Stable networking for pods, service discovery, load balancing, types include ClusterIP (internal), NodePort (node access), LoadBalancer (external LB), ExternalName (DNS). PORT CONFIGURATION: port (service port), targetPort (container port), nodePort (node port for NodePort type), protocol (TCP/UDP/SCTP). INGRESS: HTTP/HTTPS routing, host-based and path-based routing, TLS termination, external access management, requires Ingress Controller. INGRESS FEATURES: Virtual hosting, path routing, SSL/TLS, authentication, rate limiting, load balancing algorithms. PATTERNS: Microservice exposure, API gateway functionality, blue-green deployments, canary releases. INGRESS CONTROLLERS: nginx, Traefik, HAProxy, cloud-specific (ALB, GKE). CONFIGURATION: Rules, backends, annotations for controller-specific features. BEST PRACTICES: Health checks, proper TLS configuration, monitoring, security policies. Reference: https://kubernetes.io/docs/concepts/services-networking/service/',
            points: 1,
            answers: {
              create: [
                { text: 'Services: stable networking, load balancing; Ingress: HTTP routing, TLS termination, requires controller', isCorrect: true },
                { text: 'Ingress can only handle HTTP traffic while Services handle all other protocols exclusively', isCorrect: false },
                { text: 'Services automatically provide external access without requiring LoadBalancer or NodePort types', isCorrect: false },
                { text: 'Ingress controllers are built into Kubernetes and do not require separate installation', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage application lifecycle with deployment strategies?',
            explanation: 'Deployment strategies manage application updates and releases: ROLLING UPDATE: Default strategy, gradual replacement of old pods, configurable pace (maxSurge, maxUnavailable), zero-downtime deployments, rollback capability. RECREATE: Terminate all pods then create new ones, downtime during update, suitable for applications that can\'t run multiple versions. BLUE-GREEN: Two identical environments, instant switching, requires double resources, minimal downtime, easy rollback. CANARY: Gradual traffic shifting to new version, risk mitigation, A/B testing, monitoring-driven decisions. ADVANCED PATTERNS: Traffic splitting with service mesh, feature flags, progressive delivery, automated rollback triggers. KUBERNETES SUPPORT: Built-in rolling update, manual blue-green with services, canary with ingress controllers or service mesh. BEST PRACTICES: Health checks, monitoring, gradual rollouts, automated testing, rollback procedures, resource planning. CONSIDERATIONS: Application architecture, resource constraints, downtime tolerance, rollback requirements. Reference: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/',
            points: 1,
            answers: {
              create: [
                { text: 'Rolling update: gradual replacement; Recreate: terminate all; Blue-green/Canary: advanced patterns', isCorrect: true },
                { text: 'All deployment strategies require complete application downtime during updates', isCorrect: false },
                { text: 'Kubernetes only supports rolling updates and no other deployment strategies natively', isCorrect: false },
                { text: 'Deployment strategies are only relevant for single-container applications', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement custom resource definitions and work with operators?',
            explanation: 'Custom Resource Definitions (CRDs) extend Kubernetes API: CUSTOM RESOURCES: Domain-specific objects, extend Kubernetes functionality, use kubectl like built-in resources, stored in etcd. CRD STRUCTURE: API version, kind, metadata, spec (desired state), status (current state), validation schemas, subresources. OPERATORS: Automate operational tasks, implement domain knowledge, watch custom resources, reconciliation loops, lifecycle management. OPERATOR PATTERNS: Controller pattern (desired vs current state), event-driven automation, custom logic implementation, integration with external systems. DEVELOPMENT: Custom controllers, client libraries, webhook integrations, admission controllers. USE CASES: Database operators, monitoring system operators, application-specific automation, compliance automation. TOOLS: Operator SDK, Kubebuilder, KUDO, helm-operator. BEST PRACTICES: Proper RBAC, status reporting, event generation, error handling, versioning strategies. ECOSYSTEM: Operator Hub, community operators, vendor operators, certification programs. Reference: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/',
            points: 1,
            answers: {
              create: [
                { text: 'CRDs extend API with custom resources; Operators automate operations using controller patterns', isCorrect: true },
                { text: 'Custom resources are only for configuration data and cannot trigger automated operations', isCorrect: false },
                { text: 'Operators require separate cluster installations and cannot integrate with existing Kubernetes', isCorrect: false },
                { text: 'CRDs and Operators are only available in enterprise Kubernetes distributions', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you handle application data persistence with StatefulSets?',
            explanation: 'StatefulSets manage stateful applications with persistence requirements: STATEFUL CHARACTERISTICS: Stable network identities (pod-0, pod-1), ordered deployment/scaling, persistent storage per pod, stable hostnames. PERSISTENT STORAGE: VolumeClaimTemplates create PVCs per pod, storage persists beyond pod lifecycle, each pod gets dedicated storage. NETWORK IDENTITY: Headless service for direct pod access, stable DNS names (pod-0.service.namespace.svc.cluster.local), consistent network identity across restarts. ORDERING: Sequential pod creation/deletion, wait for ready state before next pod, ordered rolling updates. USE CASES: Databases (MySQL, PostgreSQL), Message queues (Kafka, RabbitMQ), Distributed systems (Cassandra, Elasticsearch), Clustered applications. SCALING: Careful scaling procedures, data replication considerations, cluster membership management, backup strategies. BEST PRACTICES: Proper health checks, graceful shutdown procedures, data backup strategies, monitoring cluster state, disaster recovery planning. CONSIDERATIONS: Storage requirements, network topology, application clustering, data consistency. Reference: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/',
            points: 1,
            answers: {
              create: [
                { text: 'Stable identity, ordered operations, persistent storage per pod, headless services for direct access', isCorrect: true },
                { text: 'StatefulSets are identical to Deployments but with different naming conventions only', isCorrect: false },
                { text: 'Persistent storage in StatefulSets is shared among all pods for data consistency', isCorrect: false },
                { text: 'StatefulSets do not support scaling operations due to their stateful nature', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement monitoring and observability for applications?',
            explanation: 'Application monitoring and observability in Kubernetes: METRICS COLLECTION: Prometheus for metrics, custom metrics via /metrics endpoint, business metrics, infrastructure metrics. APPLICATION MONITORING: APM tools integration, custom metrics exposition, SLI/SLO definition, alerting rules. LOGGING: Structured logging, centralized log aggregation, log correlation, application-specific logs. TRACING: Distributed tracing (Jaeger, Zipkin), request correlation, performance profiling, dependency mapping. KUBERNETES INTEGRATION: ServiceMonitor and PodMonitor for Prometheus, sidecar pattern for log collection, metrics server for autoscaling. DASHBOARDS: Grafana for visualization, application-specific dashboards, business metrics dashboards, infrastructure monitoring. ALERTING: Prometheus AlertManager, application alerts, runbook automation, escalation policies. BEST PRACTICES: Proper instrumentation, meaningful metrics, structured logs, dashboard standardization, alerting hygiene. OBSERVABILITY PILLARS: Metrics (what happened), Logs (detailed context), Traces (request flow). Reference: https://kubernetes.io/docs/concepts/cluster-administration/monitoring/',
            points: 1,
            answers: {
              create: [
                { text: 'Metrics (Prometheus), logs (centralized), traces (distributed); ServiceMonitor, dashboards, alerts', isCorrect: true },
                { text: 'Monitoring is only available through cloud provider services, not self-hosted solutions', isCorrect: false },
                { text: 'Application observability requires specialized APM containers running alongside applications', isCorrect: false },
                { text: 'Kubernetes provides all monitoring capabilities built-in without additional tool installation', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement network communication between microservices?',
            explanation: 'Microservice communication in Kubernetes involves multiple patterns: SERVICE DISCOVERY: DNS-based service discovery (service-name.namespace.svc.cluster.local), environment variables, service mesh integration. COMMUNICATION PATTERNS: Synchronous (HTTP/gRPC), asynchronous (message queues), event-driven (pub/sub), request-response, fire-and-forget. SERVICE MESH: Istio, Linkerd for advanced networking, traffic management, security policies, observability, circuit breaking. NETWORKING: ClusterIP for internal communication, headless services for direct pod access, ingress for external access, network policies for security. RESILIENCE: Circuit breakers, retries with backoff, timeouts, bulkhead isolation, graceful degradation. PROTOCOLS: HTTP REST APIs, gRPC for high performance, WebSockets for real-time, message queues (RabbitMQ, Kafka). SECURITY: mTLS encryption, authentication, authorization, network policies, service mesh security. PATTERNS: API Gateway, Backend for Frontend (BFF), Event sourcing, CQRS, Saga pattern for distributed transactions. Reference: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/',
            points: 1,
            answers: {
              create: [
                { text: 'DNS service discovery, various protocols (HTTP/gRPC), service mesh for advanced features, resilience patterns', isCorrect: true },
                { text: 'All microservice communication must go through external load balancers outside the cluster', isCorrect: false },
                { text: 'Direct pod-to-pod communication using IP addresses is the recommended approach', isCorrect: false },
                { text: 'Service mesh is required for any microservice communication within Kubernetes', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage secrets and sensitive configuration in cloud-native applications?',
            explanation: 'Secrets management in Kubernetes applications: KUBERNETES SECRETS: Base64 encoded sensitive data, mounted as files or environment variables, RBAC access control, encryption at rest. EXTERNAL SECRET MANAGEMENT: AWS Secrets Manager, Azure Key Vault, HashiCorp Vault, Google Secret Manager integration. SECRET OPERATORS: External Secrets Operator, Vault Agent, Sealed Secrets for GitOps, Bank-Vaults for Vault integration. BEST PRACTICES: Never hardcode secrets, rotate secrets regularly, use least privilege access, audit secret usage, implement secret scanning. PATTERNS: Init containers for secret retrieval, sidecar containers for secret rotation, CSI secret drivers, service account tokens. SECURITY CONSIDERATIONS: Encrypt etcd, secure secret storage, network encryption, secret lifecycle management. APPLICATION INTEGRATION: SDK integration, environment variable injection, file-based secrets, service account authentication. GITOPS: Sealed secrets, encrypted values, separate secret repositories, CI/CD secret injection. COMPLIANCE: Secret auditing, compliance reporting, secret governance policies, regulatory requirements. Reference: https://kubernetes.io/docs/concepts/configuration/secret/',
            points: 1,
            answers: {
              create: [
                { text: 'K8s Secrets with RBAC, external secret stores, rotation, operators, GitOps-safe encrypted secrets', isCorrect: true },
                { text: 'All secrets must be stored in external systems and cannot be managed within Kubernetes', isCorrect: false },
                { text: 'Secret management is handled automatically by Kubernetes without security considerations', isCorrect: false },
                { text: 'Secrets can only be accessed through environment variables, not mounted as files', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded Kubernetes CKAD certification with comprehensive questions`)
  return kubernetesCKAD
}
