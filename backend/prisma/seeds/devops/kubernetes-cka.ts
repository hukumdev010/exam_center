import { PrismaClient } from '../../../src/generated/prisma'

export async function seedKubernetesCKA(prisma: PrismaClient, categoryId: number) {
  // Certified Kubernetes Administrator (CKA)
  const kubernetesCKA = await prisma.certification.upsert({
    where: { slug: 'kubernetes-cka' },
    update: {},
    create: {
      name: 'Certified Kubernetes Administrator (CKA)',
      description: 'Validates skills in managing production-ready Kubernetes clusters including cluster setup, networking, security, troubleshooting, and workload management. The CKA certification demonstrates proficiency in cluster administration, node management, and maintaining high availability Kubernetes environments.',
      slug: 'kubernetes-cka',
      level: 'Professional',
      duration: 120,
      questionsCount: 17,
      categoryId,
      questions: {
        create: [
          {
            text: 'What are the core components of a Kubernetes cluster and what is their role?',
            explanation: 'Kubernetes cluster consists of control plane and worker nodes. Control plane components: kube-apiserver (API gateway and authentication), etcd (distributed key-value store for cluster state), kube-scheduler (assigns pods to nodes), kube-controller-manager (runs controllers for replication, endpoints, etc.), cloud-controller-manager (interfaces with cloud providers). Worker node components: kubelet (manages pods and communicates with control plane), kube-proxy (handles network routing and load balancing), container runtime (Docker, containerd, CRI-O for running containers). These components work together to orchestrate containerized applications across the cluster. Reference: https://kubernetes.io/docs/concepts/overview/components/',
            points: 1,
            answers: {
              create: [
                { text: 'Control plane: API server, etcd, scheduler, controllers; Worker nodes: kubelet, kube-proxy, container runtime', isCorrect: true },
                { text: 'Master nodes only contain Docker daemon and container orchestration services', isCorrect: false },
                { text: 'Single control service manages all cluster operations without distributed components', isCorrect: false },
                { text: 'Worker nodes run all management services while control plane handles only networking', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you troubleshoot a Pod that is stuck in Pending state?',
            explanation: 'Pod Pending state troubleshooting steps: 1) Check node resources with kubectl describe nodes and kubectl top nodes, 2) Verify resource requests vs available resources, 3) Check for node selectors and taints/tolerations with kubectl describe pod, 4) Examine scheduler logs: kubectl logs -n kube-system $(kubectl get pods -n kube-system | grep scheduler), 5) Check persistent volume claims status, 6) Verify image pull policies and registry access, 7) Check RBAC permissions for service accounts, 8) Look for admission controller issues, 9) Check for network policies blocking pod creation, 10) Use kubectl get events to see cluster events. Common causes include insufficient resources, scheduling constraints, PVC issues, or image problems. Reference: https://kubernetes.io/docs/tasks/debug-application-cluster/debug-pods/',
            points: 1,
            answers: {
              create: [
                { text: 'Check resources, node selectors, taints, PVCs, events, and scheduler logs systematically', isCorrect: true },
                { text: 'Immediately restart the node where the pod is scheduled to resolve pending state', isCorrect: false },
                { text: 'Delete and recreate the pod without investigating the underlying cause', isCorrect: false },
                { text: 'Only check if the container image exists in the registry', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you backup and restore etcd in a Kubernetes cluster?',
            explanation: 'etcd backup and restore process: BACKUP: 1) Use etcdctl snapshot save with proper endpoints and certificates: ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save backup.db, 2) Verify snapshot: etcdctl --write-out=table snapshot status backup.db. RESTORE: 1) Stop kube-apiserver, 2) Move old etcd data directory, 3) Restore from snapshot: ETCDCTL_API=3 etcdctl snapshot restore backup.db --data-dir=/var/lib/etcd-from-backup, 4) Update etcd.yaml to point to new data directory, 5) Start etcd and kube-apiserver. Test restoration by checking cluster state. Regular automated backups are critical for production. Reference: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/',
            points: 1,
            answers: {
              create: [
                { text: 'Use etcdctl snapshot save/restore with proper certificates, stop API server during restore, verify backup integrity', isCorrect: true },
                { text: 'Simply copy etcd data directory files without stopping services or using etcdctl', isCorrect: false },
                { text: 'Use kubectl backup command to automatically handle etcd backup and restoration', isCorrect: false },
                { text: 'Backup only the master node configuration files without etcd data', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you configure and manage RBAC (Role-Based Access Control) in Kubernetes?',
            explanation: 'RBAC configuration involves: ROLES: Define permissions within namespaces using Role resources (get, list, create, update, delete verbs on resources). CLUSTERROLES: Define cluster-wide permissions using ClusterRole resources. BINDINGS: RoleBinding binds roles to users/groups within namespaces, ClusterRoleBinding binds cluster roles globally. SUBJECTS: Users, groups, service accounts that receive permissions. Example: Create role: kubectl create role pod-reader --verb=get --verb=list --resource=pods, Create binding: kubectl create rolebinding read-pods --role=pod-reader --user=jane. Test permissions: kubectl auth can-i create pods --as=user. Use principle of least privilege, avoid wildcards in production, regularly audit permissions, use service accounts for applications. Reference: https://kubernetes.io/docs/reference/access-authn-authz/rbac/',
            points: 1,
            answers: {
              create: [
                { text: 'Define Roles/ClusterRoles for permissions, create bindings to subjects, test with auth can-i, follow least privilege', isCorrect: true },
                { text: 'Only use default service account with cluster-admin privileges for all applications', isCorrect: false },
                { text: 'Configure permissions only at the container level without cluster-wide access control', isCorrect: false },
                { text: 'Use node-level permissions instead of Kubernetes RBAC for access control', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are the different Service types in Kubernetes and when do you use each?',
            explanation: 'Kubernetes Service types: CLUSTERIP (default): Internal communication within cluster, not accessible from outside, used for microservice communication. NODEPORT: Exposes service on each node\'s IP at static port (30000-32767), accessible from outside cluster, useful for development or when LoadBalancer not available. LOADBALANCER: Creates external load balancer (cloud provider dependent), assigns external IP, ideal for production web services. EXTERNALNAME: Maps service to DNS name, returns CNAME record, used for external service integration. HEADLESS: ClusterIP set to None, returns pod IPs directly, used with StatefulSets for direct pod communication. Choose based on: internal vs external access needs, cloud provider capabilities, networking requirements, and application architecture. Reference: https://kubernetes.io/docs/concepts/services-networking/service/',
            points: 1,
            answers: {
              create: [
                { text: 'ClusterIP: internal; NodePort: node access; LoadBalancer: external LB; ExternalName: DNS mapping', isCorrect: true },
                { text: 'All service types provide identical functionality with different naming conventions only', isCorrect: false },
                { text: 'Services are only for HTTP traffic and cannot handle other protocols', isCorrect: false },
                { text: 'Only LoadBalancer type is suitable for production environments', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement Pod Security Standards (formerly Pod Security Policies) in Kubernetes?',
            explanation: 'Pod Security Standards implementation: THREE LEVELS: Privileged (unrestricted), Baseline (minimally restrictive, prevents known privilege escalations), Restricted (heavily restricted, follows current Pod hardening best practices). ENFORCEMENT MODES: enforce (blocks non-compliant pods), audit (logs violations), warn (shows warnings to users). CONFIGURATION: Namespace-level using labels: pod-security.kubernetes.io/enforce=restricted, pod-security.kubernetes.io/audit=baseline, pod-security.kubernetes.io/warn=baseline. BEST PRACTICES: Start with audit/warn modes, gradually enforce restrictions, test thoroughly, document exceptions, use admission controllers for complex policies. Common restrictions: no privileged containers, no host network/PID/IPC, read-only root filesystem, non-root users, restricted volume types. Reference: https://kubernetes.io/docs/concepts/security/pod-security-standards/',
            points: 1,
            answers: {
              create: [
                { text: 'Three levels (privileged/baseline/restricted) with enforce/audit/warn modes applied via namespace labels', isCorrect: true },
                { text: 'Only binary allow/deny policies without granular control or audit capabilities', isCorrect: false },
                { text: 'Security policies are handled entirely by container runtime without Kubernetes involvement', isCorrect: false },
                { text: 'Pod security is managed only through network policies and service mesh configuration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you configure and troubleshoot Kubernetes networking (CNI)?',
            explanation: 'Kubernetes networking requires CNI (Container Network Interface) plugins. SETUP: Choose CNI plugin (Flannel, Calico, Weave, Cilium), install via manifests or Helm, configure CIDR blocks for pods and services, ensure no overlap with node networks. TROUBLESHOOTING: 1) Check CNI plugin pods: kubectl get pods -n kube-system, 2) Verify node readiness: kubectl get nodes, 3) Check pod-to-pod connectivity: ping between pods, 4) Test DNS resolution: nslookup kubernetes.default, 5) Examine CNI logs: kubectl logs -n kube-system <cni-pod>, 6) Verify network policies, 7) Check firewall rules on nodes, 8) Validate CIDR configurations. NETWORKING MODEL: Every pod gets unique IP, pods communicate without NAT, nodes can communicate with all pods, services provide stable endpoints. Reference: https://kubernetes.io/docs/concepts/cluster-administration/networking/',
            points: 1,
            answers: {
              create: [
                { text: 'Install CNI plugin, configure CIDRs, troubleshoot with pod logs, connectivity tests, and DNS validation', isCorrect: true },
                { text: 'Kubernetes handles all networking automatically without requiring CNI plugin installation', isCorrect: false },
                { text: 'Only configure host networking without pod-specific network isolation', isCorrect: false },
                { text: 'Network configuration is handled exclusively by cloud provider without CNI involvement', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage storage in Kubernetes using Persistent Volumes and Storage Classes?',
            explanation: 'Kubernetes storage management: PERSISTENT VOLUMES (PV): Cluster-wide storage resources provisioned by admin or dynamically via Storage Classes, independent lifecycle from pods, support various storage types (hostPath, NFS, cloud storage). PERSISTENT VOLUME CLAIMS (PVC): User requests for storage with specific size and access modes, bind to available PVs, used in pod specifications. STORAGE CLASSES: Define storage "classes" with different performance/features, enable dynamic provisioning, specify provisioner (kubernetes.io/aws-ebs, kubernetes.io/gce-pd), set parameters like type, zones, encryption. WORKFLOW: Create StorageClass → User creates PVC → System provisions PV → Pod mounts PVC. ACCESS MODES: ReadWriteOnce (single node), ReadOnlyMany (multiple nodes read), ReadWriteMany (multiple nodes read/write). RECLAIM POLICIES: Retain, Delete, Recycle. Reference: https://kubernetes.io/docs/concepts/storage/persistent-volumes/',
            points: 1,
            answers: {
              create: [
                { text: 'PVs provide storage, PVCs request storage, StorageClasses enable dynamic provisioning with access modes', isCorrect: true },
                { text: 'All storage is automatically managed by Kubernetes without administrator intervention', isCorrect: false },
                { text: 'Storage is only available through direct container volume mounts without persistence', isCorrect: false },
                { text: 'Persistent storage requires manual file system management on each worker node', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you perform rolling updates and rollbacks for Deployments?',
            explanation: 'Rolling updates and rollbacks in Kubernetes: ROLLING UPDATE: kubectl set image deployment/myapp container=image:v2, or kubectl apply -f updated-deployment.yaml. UPDATE STRATEGY: RollingUpdate (default) with maxSurge and maxUnavailable parameters controlling pace, Recreate strategy terminates all then creates new. MONITORING: kubectl rollout status deployment/myapp, kubectl get rs to see ReplicaSets, kubectl describe deployment myapp for details. ROLLBACK: kubectl rollout undo deployment/myapp (to previous), kubectl rollout undo deployment/myapp --to-revision=2 (to specific revision), kubectl rollout history deployment/myapp to see revisions. BEST PRACTICES: Use readiness/liveness probes, set resource limits, test in staging, implement gradual rollouts, monitor application metrics, have rollback procedures ready. PAUSE/RESUME: kubectl rollout pause/resume deployment/myapp. Reference: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/',
            points: 1,
            answers: {
              create: [
                { text: 'Use kubectl set image or apply, monitor with rollout status, rollback with rollout undo, control pace with strategy', isCorrect: true },
                { text: 'Manually delete all pods and recreate them with new image versions', isCorrect: false },
                { text: 'Rolling updates are only possible with StatefulSets, not Deployments', isCorrect: false },
                { text: 'Updates require complete cluster downtime and manual intervention', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you configure resource quotas and limit ranges in Kubernetes?',
            explanation: 'Resource management in Kubernetes: RESOURCE QUOTAS: Namespace-level limits on resource consumption, specify total CPU/memory, object counts (pods, services, PVCs), storage requests. Create: kubectl create quota myquota --hard=cpu=2,memory=4Gi,pods=10. LIMIT RANGES: Default and maximum resource limits for containers/pods, prevent resource hogging, set default requests/limits for containers without specifications. Create LimitRange with default, defaultRequest, max, min values. QUALITY OF SERVICE: Guaranteed (requests=limits), Burstable (requests<limits), BestEffort (no requests/limits). MONITORING: kubectl describe quota, kubectl top pods/nodes, monitoring tools for resource usage. BEST PRACTICES: Set appropriate defaults, monitor usage patterns, use horizontal pod autoscaler, implement resource-based alerts, regularly review and adjust quotas. Reference: https://kubernetes.io/docs/concepts/policy/resource-quotas/',
            points: 1,
            answers: {
              create: [
                { text: 'ResourceQuota limits namespace consumption, LimitRange sets container defaults/maximums, monitor with describe/top', isCorrect: true },
                { text: 'Resource limits are only enforced at the cluster level without namespace-specific controls', isCorrect: false },
                { text: 'Kubernetes automatically manages all resource allocation without administrator configuration', isCorrect: false },
                { text: 'Resource quotas apply only to storage and not to CPU or memory consumption', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you configure and use ConfigMaps and Secrets for application configuration?',
            explanation: 'ConfigMaps and Secrets for configuration: CONFIGMAPS: Store non-sensitive configuration data as key-value pairs, environment variables, or files. Create: kubectl create configmap myconfig --from-literal=key1=value1 --from-file=config.properties. Use in pods: envFrom, env with configMapKeyRef, volumeMounts for files. SECRETS: Store sensitive data (passwords, tokens, keys) with base64 encoding, types include Opaque, kubernetes.io/service-account-token, kubernetes.io/dockercfg. Create: kubectl create secret generic mysecret --from-literal=password=mypass. Use similar to ConfigMaps but with additional security considerations. BEST PRACTICES: Don\'t include secrets in images, use external secret management (Vault, AWS Secrets Manager), rotate secrets regularly, limit access with RBAC, use sealed-secrets or external-secrets operators for GitOps. TROUBLESHOOTING: Check mounting, verify keys, validate RBAC permissions. Reference: https://kubernetes.io/docs/concepts/configuration/configmap/',
            points: 1,
            answers: {
              create: [
                { text: 'ConfigMaps for non-sensitive config, Secrets for sensitive data, mount as env vars or volumes with proper RBAC', isCorrect: true },
                { text: 'All configuration should be hardcoded in container images for security', isCorrect: false },
                { text: 'Secrets and ConfigMaps are identical in functionality and security handling', isCorrect: false },
                { text: 'Configuration is only possible through command-line arguments to containers', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement monitoring and logging for Kubernetes clusters?',
            explanation: 'Kubernetes monitoring and logging: MONITORING: Metrics Server for resource metrics (kubectl top), Prometheus for detailed metrics collection, Grafana for visualization, AlertManager for notifications. Node-level: node-exporter, cAdvisor for container metrics. Application-level: custom metrics, service monitors, pod monitors. LOGGING: Container logs: kubectl logs, centralized logging with Fluentd/Fluent Bit + Elasticsearch/Loki + Kibana/Grafana. Log rotation, structured logging, log levels. OBSERVABILITY: Distributed tracing with Jaeger/Zipkin, APM tools, custom dashboards. BEST PRACTICES: Set up resource-based alerts, monitor cluster health, use structured logs, implement log retention policies, monitor application metrics, set up service level indicators (SLIs). Tools integration: ELK stack, Prometheus stack, commercial solutions (Datadog, New Relic). Reference: https://kubernetes.io/docs/concepts/cluster-administration/logging/',
            points: 1,
            answers: {
              create: [
                { text: 'Metrics Server/Prometheus for monitoring, Fluentd/ELK for logging, Grafana for visualization, structured logs', isCorrect: true },
                { text: 'Monitoring is handled automatically by Kubernetes without additional tool installation', isCorrect: false },
                { text: 'Only kubectl logs command is sufficient for production monitoring and troubleshooting', isCorrect: false },
                { text: 'Application monitoring requires direct access to worker nodes without centralized tools', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you troubleshoot node issues and manage node lifecycle in Kubernetes?',
            explanation: 'Node troubleshooting and management: TROUBLESHOOTING: Check node status: kubectl get nodes, describe nodes for conditions and events, check kubelet logs: journalctl -u kubelet, verify container runtime: docker/containerd status, check disk/memory usage: df, free, check network connectivity, examine system resources and kernel logs. NODE CONDITIONS: Ready, OutOfDisk, MemoryPressure, PIDPressure, NetworkUnavailable. LIFECYCLE MANAGEMENT: Drain node for maintenance: kubectl drain node --ignore-daemonsets --delete-emptydir-data, cordon to prevent new pods: kubectl cordon node, uncordon to resume: kubectl uncordon node. MAINTENANCE: OS updates, kernel patches, hardware replacement, capacity planning. RECOVERY: Node replacement, etcd member recovery, certificate renewal. AUTOMATION: Node auto-scaling, cluster autoscaler, node problem detector. Reference: https://kubernetes.io/docs/tasks/administer-cluster/cluster-management/',
            points: 1,
            answers: {
              create: [
                { text: 'Check node status/conditions, kubelet/system logs, drain for maintenance, monitor resource pressure, automate scaling', isCorrect: true },
                { text: 'Node issues are automatically resolved by Kubernetes without administrator intervention', isCorrect: false },
                { text: 'Simply restart problematic nodes without proper draining or workload migration', isCorrect: false },
                { text: 'Node management requires only container runtime operations without Kubernetes integration', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you upgrade a Kubernetes cluster using kubeadm?',
            explanation: 'Kubernetes cluster upgrade with kubeadm: PREPARATION: Check current version: kubectl version, review release notes, backup etcd, test in non-production, check component compatibility. CONTROL PLANE UPGRADE: 1) Upgrade kubeadm: apt update && apt install kubeadm=1.x.x-00, 2) Plan upgrade: kubeadm upgrade plan, 3) Apply upgrade: kubeadm upgrade apply v1.x.x, 4) Drain node: kubectl drain <control-plane> --ignore-daemonsets, 5) Upgrade kubelet and kubectl: apt install kubelet=1.x.x-00 kubectl=1.x.x-00, 6) Restart kubelet: systemctl daemon-reload && systemctl restart kubelet, 7) Uncordon node: kubectl uncordon <control-plane>. WORKER NODES: Drain, upgrade kubeadm, kubeadm upgrade node, upgrade kubelet/kubectl, restart kubelet, uncordon. VERIFICATION: kubectl get nodes, component health checks, application functionality tests. Reference: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/',
            points: 1,
            answers: {
              create: [
                { text: 'Upgrade kubeadm, plan/apply upgrade, drain nodes, upgrade kubelet/kubectl, test functionality systematically', isCorrect: true },
                { text: 'Simultaneously upgrade all cluster components without proper sequencing or testing', isCorrect: false },
                { text: 'Upgrade only the master node while leaving worker nodes on older versions', isCorrect: false },
                { text: 'Replace entire cluster instead of performing in-place upgrades', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between StatefulSets and Deployments, and when do you use each?',
            explanation: 'StatefulSets vs Deployments comparison: DEPLOYMENTS: For stateless applications, pods are interchangeable, random naming (app-deployment-xyz), no persistent identity, can scale up/down quickly, rolling updates replace pods, suitable for web servers, APIs, microservices. STATEFULSETS: For stateful applications, pods have stable identity, ordered naming (app-0, app-1), persistent network identities and storage, ordered deployment/scaling, rolling updates maintain identity, suitable for databases, message queues, clustered applications. KEY DIFFERENCES: Identity preservation, ordered operations, storage persistence, network identity stability. HEADLESS SERVICES: StatefulSets typically use headless services for direct pod communication. USE CASES: Deployment for frontend/API services, StatefulSet for MySQL, PostgreSQL, Kafka, Elasticsearch, MongoDB. CONSIDERATIONS: StatefulSets are more complex, slower scaling, require careful storage management. Reference: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/',
            points: 1,
            answers: {
              create: [
                { text: 'Deployments: stateless, interchangeable pods; StatefulSets: stateful, stable identity, ordered operations, persistent storage', isCorrect: true },
                { text: 'StatefulSets and Deployments are identical in functionality with different naming conventions', isCorrect: false },
                { text: 'Deployments are only for single-pod applications while StatefulSets handle multiple pods', isCorrect: false },
                { text: 'StatefulSets are deprecated in favor of Deployments for all application types', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you implement network policies for pod-to-pod communication security?',
            explanation: 'Network Policies for pod communication security: CONCEPT: Default allow-all behavior, Network Policies enable segmentation, require CNI plugin support (Calico, Cilium, Weave). POLICY TYPES: Ingress (incoming traffic), Egress (outgoing traffic), default deny-all policies. SELECTORS: podSelector for target pods, namespaceSelector for source/destination namespaces, ipBlock for IP ranges. PORTS AND PROTOCOLS: Specify allowed ports and protocols (TCP, UDP, SCTP). EXAMPLES: Deny all: empty podSelector with policyTypes, Allow specific: matchLabels selectors, Database tier: allow only from app tier, Frontend: allow from ingress, deny to database. TESTING: Use network debugging pods, test connectivity with curl/telnet, verify policies with kubectl describe networkpolicy. BEST PRACTICES: Default deny-all approach, least privilege principle, label-based selectors, regular policy audits, document network architecture. Reference: https://kubernetes.io/docs/concepts/services-networking/network-policies/',
            points: 1,
            answers: {
              create: [
                { text: 'Define ingress/egress rules with pod/namespace selectors, implement default deny, test connectivity, require CNI support', isCorrect: true },
                { text: 'Network policies are automatically enforced without requiring specific CNI plugin support', isCorrect: false },
                { text: 'All pod communication is secured by default without additional policy configuration', isCorrect: false },
                { text: 'Network security is handled entirely at the node firewall level without Kubernetes policies', isCorrect: false },
              ],
            },
          },
          {
            text: 'How do you manage certificates and TLS in Kubernetes clusters?',
            explanation: 'Certificate and TLS management in Kubernetes: CLUSTER CERTIFICATES: CA certificates for cluster communication, component certificates (apiserver, kubelet, etcd), automatic certificate rotation in newer versions. LOCATIONS: /etc/kubernetes/pki/ for cluster certificates, /var/lib/kubelet/pki/ for kubelet certificates. COMMANDS: kubeadm certs check-expiration, kubeadm certs renew all, openssl x509 -in cert.pem -text -noout. APPLICATION TLS: Ingress TLS termination, cert-manager for automatic certificate provisioning from Let\'s Encrypt/other CAs, Secret objects for TLS certificates. CERTIFICATE ROTATION: Manual renewal with kubeadm, automatic rotation for kubelet certificates, monitoring certificate expiration. TROUBLESHOOTING: Certificate validation errors, clock sync issues, expired certificates, CA trust chain problems. SECURITY: Protect private keys, regular rotation, monitor expiration dates, use strong key sizes, implement certificate-based authentication. Reference: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/',
            points: 1,
            answers: {
              create: [
                { text: 'Manage cluster CA/component certs, use cert-manager for apps, monitor expiration, implement rotation policies', isCorrect: true },
                { text: 'Kubernetes handles all certificate management automatically without administrator involvement', isCorrect: false },
                { text: 'Only application-level certificates require management while cluster certificates are permanent', isCorrect: false },
                { text: 'Certificate management is handled exclusively by cloud provider services', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  console.log(`✅ Seeded Kubernetes CKA certification with comprehensive questions`)
  return kubernetesCKA
}
