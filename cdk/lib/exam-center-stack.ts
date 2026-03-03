import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';

export class ExamCenterEc2Stack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const keyPairName = new cdk.CfnParameter(this, 'KeyPairName', {
      type: 'String',
      default: '',
      description: 'Optional EC2 key pair name for SSH access. Leave empty to disable key pair.',
    });

    const instanceTypeParam = new cdk.CfnParameter(this, 'InstanceType', {
      type: 'String',
      default: 't2.micro',
      description: 'EC2 instance type (micro recommended).',
    });

    const repoUrl = new cdk.CfnParameter(this, 'RepoUrl', {
      type: 'String',
      default: 'https://github.com/hukumdev010/exam_center.git',
      description: 'Git repo URL containing /backend and /frontend folders.',
    });

    const repoBranch = new cdk.CfnParameter(this, 'RepoBranch', {
      type: 'String',
      default: 'main',
      description: 'Git branch to deploy.',
    });

    const backendPort = new cdk.CfnParameter(this, 'BackendPort', {
      type: 'Number',
      default: 8000,
      description: 'Backend container port.',
    });

    const frontendPort = new cdk.CfnParameter(this, 'FrontendPort', {
      type: 'Number',
      default: 3000,
      description: 'Frontend Next.js runtime port on EC2.',
    });

    const databaseName = new cdk.CfnParameter(this, 'DatabaseName', {
      type: 'String',
      default: 'exam_center',
      description: 'PostgreSQL database name running on the EC2 instance.',
    });

    const databaseUser = new cdk.CfnParameter(this, 'DatabaseUser', {
      type: 'String',
      default: 'postgres',
      description: 'PostgreSQL user running on the EC2 instance.',
    });

    const databasePassword = new cdk.CfnParameter(this, 'DatabasePassword', {
      type: 'String',
      default: 'postgres',
      description: 'PostgreSQL password running on the EC2 instance.',
      noEcho: true,
    });

    const secretKey = new cdk.CfnParameter(this, 'SecretKey', {
      type: 'String',
      default: 'change-me-in-production',
      description: 'SECRET_KEY passed to backend container.',
      noEcho: true,
    });

    const vpc = new ec2.Vpc(this, 'ExamCenterVpc', {
      maxAzs: 2,
      natGateways: 0,
      subnetConfiguration: [
        {
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
          cidrMask: 24,
        },
      ],
    });

    const securityGroup = new ec2.SecurityGroup(this, 'ExamCenterSg', {
      vpc,
      allowAllOutbound: true,
      description: 'Allow SSH and HTTP access',
    });

    securityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(22), 'SSH');
    securityGroup.addIngressRule(ec2.Peer.anyIpv4(), ec2.Port.tcp(80), 'HTTP');

    const hasKeyPairCondition = new cdk.CfnCondition(this, 'HasKeyPair', {
      expression: cdk.Fn.conditionNot(cdk.Fn.conditionEquals(keyPairName.valueAsString, '')),
    });

    const machineImage = ec2.MachineImage.latestAmazonLinux2023();

    const instance = new ec2.Instance(this, 'ExamCenterInstance', {
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      securityGroup,
      instanceType: new ec2.InstanceType(instanceTypeParam.valueAsString),
      machineImage,
      blockDevices: [
        {
          deviceName: '/dev/xvda',
          volume: ec2.BlockDeviceVolume.ebs(20, {
            deleteOnTermination: true,
            encrypted: false,
          }),
        },
      ],
    });

    const cfnInstance = instance.node.defaultChild as ec2.CfnInstance;
    cfnInstance.keyName = cdk.Fn.conditionIf(
      hasKeyPairCondition.logicalId,
      keyPairName.valueAsString,
      cdk.Aws.NO_VALUE,
    ).toString();

    instance.userData.addCommands(
      'set -euxo pipefail',
      'dnf update -y',
      'dnf install -y git docker nginx nodejs npm',
      'systemctl enable docker',
      'systemctl start docker',
      'systemctl enable nginx',
      'systemctl start nginx',
      'usermod -aG docker ec2-user || true',
      'mkdir -p /opt/exam-center',
      'chown -R ec2-user:ec2-user /opt/exam-center',
      'cat >/opt/exam-center/deploy-app.sh <<\'EOF\'',
      '#!/usr/bin/env bash',
      'set -euxo pipefail',
      'REPO_URL="' + repoUrl.valueAsString + '"',
      'BRANCH="' + repoBranch.valueAsString + '"',
      'BACKEND_PORT="' + backendPort.valueAsNumber + '"',
      'FRONTEND_PORT="' + frontendPort.valueAsNumber + '"',
      'mkdir -p /opt/exam-center',
      'cd /opt/exam-center',
      'if [ ! -d repo ]; then',
      '  git clone --branch "$BRANCH" "$REPO_URL" repo',
      'else',
      '  cd repo && git fetch origin && git checkout "$BRANCH" && git pull --ff-only origin "$BRANCH" && cd ..',
      'fi',
      'cd /opt/exam-center/repo',
      'cat > backend/.env <<\'ENVEOF\'',
      'DATABASE_URL=postgresql+asyncpg://' + databaseUser.valueAsString + ':' + databasePassword.valueAsString + '@exam-center-postgres:5432/' + databaseName.valueAsString,
      'SECRET_KEY=' + secretKey.valueAsString,
      'ALGORITHM=HS256',
      'ACCESS_TOKEN_EXPIRE_MINUTES=30',
      'ENVIRONMENT=production',
      'DEBUG=false',
      'ENVEOF',
      'docker network create exam-center-network || true',
      'docker volume create exam-center-postgres-data || true',
      'docker rm -f exam-center-postgres || true',
      'docker run -d --name exam-center-postgres --restart unless-stopped --network exam-center-network -e POSTGRES_DB=' + databaseName.valueAsString + ' -e POSTGRES_USER=' + databaseUser.valueAsString + ' -e POSTGRES_PASSWORD=' + databasePassword.valueAsString + ' -v exam-center-postgres-data:/var/lib/postgresql/data postgres:16-alpine',
      'until docker exec exam-center-postgres pg_isready -U ' + databaseUser.valueAsString + ' -d ' + databaseName.valueAsString + '; do sleep 2; done',
      'cat > backend/Dockerfile <<\'DOCKERFILE\'',
      'FROM python:3.11-slim',
      'WORKDIR /app',
      'ENV PYTHONDONTWRITEBYTECODE=1',
      'ENV PYTHONUNBUFFERED=1',
      'RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*',
      'COPY backend/requirements.txt /tmp/requirements.txt',
      'RUN pip install --no-cache-dir -r /tmp/requirements.txt',
      'COPY backend /app',
      'EXPOSE 8000',
      'CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]',
      'DOCKERFILE',
      'docker rm -f exam-center-backend || true',
      'docker build -f backend/Dockerfile -t exam-center-backend:latest .',
      'docker run -d --name exam-center-backend --restart unless-stopped --network exam-center-network -p "${BACKEND_PORT}:8000" --env-file backend/.env exam-center-backend:latest',
      'cd frontend',
      'corepack enable || true',
      'if [ -f yarn.lock ]; then',
      '  yarn install --immutable || yarn install',
      '  yarn build',
      '  (pkill -f "next start" || true)',
      '  nohup yarn start --hostname 0.0.0.0 --port "$FRONTEND_PORT" >/var/log/exam-center-frontend.log 2>&1 &',
      'else',
      '  npm install',
      '  npm run build',
      '  (pkill -f "next start" || true)',
      '  nohup npm run start -- --hostname 0.0.0.0 --port "$FRONTEND_PORT" >/var/log/exam-center-frontend.log 2>&1 &',
      'fi',
      'cat >/etc/nginx/conf.d/exam-center.conf <<NGINXEOF',
      'server {',
      '  listen 80;',
      '  server_name _;',
      '  location /api/ {',
      '    proxy_pass http://127.0.0.1:${BACKEND_PORT}/;',
      '    proxy_http_version 1.1;',
      '    proxy_set_header Host $host;',
      '    proxy_set_header X-Real-IP $remote_addr;',
      '    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;',
      '    proxy_set_header X-Forwarded-Proto $scheme;',
      '  }',
      '  location / {',
      '    proxy_pass http://127.0.0.1:${FRONTEND_PORT};',
      '    proxy_http_version 1.1;',
      '    proxy_set_header Upgrade $http_upgrade;',
      '    proxy_set_header Connection "upgrade";',
      '    proxy_set_header Host $host;',
      '    proxy_set_header X-Real-IP $remote_addr;',
      '    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;',
      '    proxy_set_header X-Forwarded-Proto $scheme;',
      '  }',
      '}',
      'NGINXEOF',
      'rm -f /etc/nginx/conf.d/default.conf || true',
      'nginx -t',
      'systemctl restart nginx',
      'EOF',
      'chmod +x /opt/exam-center/deploy-app.sh',
      'bash /opt/exam-center/deploy-app.sh'
    );

    const eip = new ec2.CfnEIP(this, 'ExamCenterEip', {
      domain: 'vpc',
      instanceId: instance.instanceId,
    });

    new cdk.CfnOutput(this, 'PublicIp', {
      value: eip.ref,
      description: 'EC2 public IP',
    });

    new cdk.CfnOutput(this, 'FrontendUrl', {
      value: cdk.Fn.sub('http://${PublicIp}', {
        PublicIp: eip.ref,
      }),
      description: 'Frontend URL via Nginx',
    });

    new cdk.CfnOutput(this, 'BackendHealthUrl', {
      value: cdk.Fn.sub('http://${PublicIp}/api/docs', {
        PublicIp: eip.ref,
      }),
      description: 'Backend docs through Nginx /api path',
    });
  }
}
