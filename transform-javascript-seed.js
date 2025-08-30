const fs = require('fs');

// Read the current file
const filePath = './prisma/seeds/javascript.ts';
let content = fs.readFileSync(filePath, 'utf8');

// Function to extract reference from explanation and clean it
function extractReference(explanation) {
  const referenceMatch = explanation.match(/Reference: (.+)$/);
  if (referenceMatch) {
    const refText = referenceMatch[1];
    // Convert common reference patterns to proper URLs
    if (refText.includes('MDN Web Docs')) {
      if (refText.includes('Array methods')) return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array';
      if (refText.includes('JavaScript modules')) return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules';
      if (refText.includes('WeakMap')) return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap';
      if (refText.includes('Generators')) return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator';
      if (refText.includes('Function methods')) return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function';
      if (refText.includes('Asynchronous JavaScript')) return 'https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous';
    }
    // Default fallback
    return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript';
  }
  return 'https://developer.mozilla.org/en-US/docs/Web/JavaScript';
}

// Transform each question block
content = content.replace(
  /(\s+){\s*\n(\s+)text: '([^']+)',\s*\n(\s+)explanation: '([^']+)',\s*\n(\s+)points: (\d+),\s*\n(\s+)answers: {\s*\n(\s+)create: \[\s*\n((?:\s+{ text: '[^']+', isCorrect: (?:true|false) },?\s*\n)*)\s+\],\s*\n(\s+)},\s*\n(\s+)},/g,
  (match, indent1, indent2, text, indent3, explanation, indent4, points, indent5, indent6, answers, indent7, indent8) => {
    // Clean explanation (remove reference part)
    const cleanExplanation = explanation.replace(/\s*Reference: .+$/, '');
    
    // Extract reference
    const reference = extractReference(explanation);
    
    // Transform answers to use shuffleAnswers
    const answersArray = answers.trim().split('\n').map(line => line.trim()).filter(line => line.length > 0);
    const transformedAnswers = answersArray.join('\n                ');
    
    return `${indent1}{
${indent2}text: '${text}',
${indent3}explanation: '${cleanExplanation}',
${indent3}reference: '${reference}',
${indent4}points: ${points},
${indent5}answers: {
${indent6}create: shuffleAnswers([
                ${transformedAnswers}
              ]),
${indent7}},
${indent8}},`;
  }
);

// Write the transformed content back
fs.writeFileSync(filePath, content, 'utf8');
console.log('Transformation completed!');
