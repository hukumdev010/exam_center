#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'fs';

const filePath = './prisma/seeds/javascript.ts';
let content = readFileSync(filePath, 'utf8');

// Define reference mappings for common topics
const referenceMap = {
  'generators': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator',
  'asynchronous': 'https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous',
  'symbol': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol',
  'proxy': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy',
  'reflect': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect',
  'iterator': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols',
  'bigint': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt',
  'spread': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax',
  'regex': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions',
  'fetch': 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API',
  'worker': 'https://developer.mozilla.org/en-US/docs/Web/API/Worker',
  'memory': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management',
  'performance': 'https://developer.mozilla.org/en-US/docs/Web/API/Performance',
  'service': 'https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API',
  'storage': 'https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API',
  'immutable': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze',
  'private': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields'
};

function getReference(explanation, text) {
  const lowerExplanation = explanation.toLowerCase();
  const lowerText = text.toLowerCase();
  
  // Check for specific topics
  for (const [topic, url] of Object.entries(referenceMap)) {
    if (lowerExplanation.includes(topic) || lowerText.includes(topic)) {
      return url;
    }
  }
  
  // Default fallback
  return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript';
}

// Transform remaining questions that don't have shuffleAnswers yet
const questionRegex = /(\s+){\s*\n(\s+)text: '([^']+)',\s*\n(\s+)explanation: '([^']*(?:\\'[^']*)*)',\s*\n(?:(\s+)reference: '[^']*',\s*\n)?(\s+)points: (\d+),\s*\n(\s+)answers: {\s*\n(\s+)create: \[\s*\n((?:\s+{ text: '[^']*(?:\\'[^']*)*', isCorrect: (?:true|false) },?\s*\n?)*)\s*\],\s*\n(\s+)},\s*\n(\s+)},/g;

content = content.replace(questionRegex, (match, indent1, indent2, text, indent3, explanation, refIndent, indent4, points, indent5, indent6, answers, indent7, indent8) => {
  // Skip if already using shuffleAnswers
  if (match.includes('shuffleAnswers')) {
    return match;
  }
  
  // Clean explanation (remove existing reference)
  const cleanExplanation = explanation.replace(/\.\s*Reference: .+$/, '.');
  
  // Get appropriate reference
  const reference = getReference(cleanExplanation, text);
  
  return `${indent1}{
${indent2}text: '${text}',
${indent3}explanation: '${cleanExplanation}',
${indent3}reference: '${reference}',
${indent4}points: ${points},
${indent5}answers: {
${indent6}create: shuffleAnswers([
${answers}              ]),
${indent7}},
${indent8}},`;
});

writeFileSync(filePath, content, 'utf8');
console.log('✅ JavaScript seed transformation completed!');
console.log('📝 All questions now have:');
console.log('   - Randomized answer positions using shuffleAnswers()');
console.log('   - Reference URLs in the reference field');
console.log('   - Clean explanations without inline references');
