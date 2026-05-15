import fs from 'fs';

const data = JSON.parse(fs.readFileSync('src/data/flashcards.json', 'utf8'));

// 1. Add Missing Laplace Cards
const newLaplaceCards = [
  {
    id: "ce-2-7",
    chapter: "제어공학",
    topic: "2. 라플라스 변환 추가",
    question: "단위 임펄스 함수(Unit Impulse Function) $\\delta(t)$ 의 라플라스 변환은?",
    answer: "$\\mathscr{L}[\\delta(t)] = 1$"
  },
  {
    id: "ce-2-8",
    chapter: "제어공학",
    topic: "2. 라플라스 변환 추가",
    question: "시간 다항식 함수 $t^n$ 의 라플라스 변환은?",
    answer: "$\\mathscr{L}[t^n] = \\frac{n!}{s^{n+1}}$\n\n(※ $t$ 의 경우 $n=1$ 이므로 $\\frac{1}{s^2}$)"
  },
  {
    id: "ce-2-9",
    chapter: "제어공학",
    topic: "2. 라플라스 변환 추가",
    question: "감쇠 정현파 함수 $e^{-at}\\sin(\\omega t)$ 의 라플라스 변환은? (복소 추이 정리 적용)",
    answer: "$\\mathscr{L}[e^{-at}\\sin(\\omega t)] = \\frac{\\omega}{(s+a)^2 + \\omega^2}$"
  }
];

// Add energy density cards (since they are missing)
const newEmCards = [
  {
    id: "em-18-1",
    chapter: "전기자기학",
    topic: "18. 에너지 밀도",
    question: "전계 $E$, 전속밀도 $D$, 유전율 $\\varepsilon$ 인 정전계의 체적당 에너지 밀도 $w$ 는?",
    answer: "$w = \\frac{1}{2}\\varepsilon E^2 = \\frac{1}{2}ED = \\frac{D^2}{2\\varepsilon} \\quad [\\text{J/m}^3]$"
  },
  {
    id: "em-31-2",
    chapter: "전기자기학",
    topic: "31. 자계 에너지 밀도",
    question: "자계 $H$, 자속밀도 $B$, 투자율 $\\mu$ 인 정자계의 체적당 에너지 밀도 $w$ 는?",
    answer: "$w = \\frac{1}{2}\\mu H^2 = \\frac{1}{2}HB = \\frac{B^2}{2\\mu} \\quad [\\text{J/m}^3]$"
  }
];

data.push(...newLaplaceCards);
data.push(...newEmCards);

// 2. Add Duality Tip to related Electromagnetic cards
const dualityTip = `
💡 [변칙 대비: 정전계 vs 정자계 쌍대성(Duality)]
- 밀도: $D = \\varepsilon E$ ↔ $B = \\mu H$
- 상수: 유전율 $\\varepsilon$ ↔ 투자율 $\\mu$
- 분극/자화: 분극 세기 $P$ ↔ 자화 세기 $J$
- 경계조건: 접선($E, H$) 연속, 법선($D, B$) 연속
- 굴절법칙: $\\frac{\\tan\\theta_1}{\\tan\\theta_2} = \\frac{\\varepsilon_1}{\\varepsilon_2}$ ↔ $\\frac{\\tan\\theta_1}{\\tan\\theta_2} = \\frac{\\mu_1}{\\mu_2}$
- 에너지밀도: $w = \\frac{1}{2}\\varepsilon E^2$ ↔ $w = \\frac{1}{2}\\mu H^2$`;

let modifiedCount = 0;
data.forEach(card => {
  // Target IDs or keywords in Electromagnetics
  if (card.chapter === "전기자기학" && 
      (card.topic.includes("경계 조건") || 
       card.topic.includes("맥스웰 응력") || 
       card.topic.includes("유전체") || 
       card.topic.includes("자성체") || 
       card.topic.includes("에너지 밀도"))) {
    
    if (card.answer.includes('💡')) {
      card.answer = card.answer.split('\n\n💡')[0];
    }
    
    card.answer += '\n\n' + dualityTip;
    modifiedCount++;
  }
});

fs.writeFileSync('src/data/flashcards.json', JSON.stringify(data, null, 2), 'utf8');
console.log(`Added 5 new cards. Updated ${modifiedCount} EM cards with duality tip.`);
