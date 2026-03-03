#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { ExamCenterEc2Stack } from '../lib/exam-center-stack';

const app = new cdk.App();

new ExamCenterEc2Stack(app, 'ExamCenterEc2Stack', {
  description: 'Deploy frontend + backend (backend in Docker) on one EC2 micro instance',
});
