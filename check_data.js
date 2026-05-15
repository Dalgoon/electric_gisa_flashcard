import fs from 'fs';

const data = JSON.parse(fs.readFileSync('src/data/flashcards.json', 'utf8'));

const laplace = data.filter(c => c.question.includes('라플라스') || c.topic.includes('라플라스') || c.answer.includes('라플라스'));
const dielectric = data.filter(c => c.question.includes('유전체') || c.topic.includes('유전체') || c.answer.includes('유전체') || c.topic.includes('유전율') || c.question.includes('유전율'));
const magnetic = data.filter(c => c.question.includes('자성체') || c.topic.includes('자성체') || c.answer.includes('자성체') || c.topic.includes('자계') || c.topic.includes('투자율') || c.question.includes('투자율'));

console.log("=== 라플라스 관련 ===");
laplace.forEach(c => console.log(`[${c.id}] ${c.topic}: ${c.question}`));

console.log("\n=== 유전체 관련 ===");
dielectric.forEach(c => console.log(`[${c.id}] ${c.topic}: ${c.question}`));

console.log("\n=== 자성체 관련 ===");
magnetic.forEach(c => console.log(`[${c.id}] ${c.topic}: ${c.question}`));
