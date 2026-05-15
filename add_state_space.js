import fs from 'fs';

const data = JSON.parse(fs.readFileSync('src/data/flashcards.json', 'utf8'));

const newCard = {
  id: "ce-12-1",
  chapter: "제어공학",
  topic: "12. 상태공간법",
  question: "2차 미분방정식 $\\frac{d^2C}{dt^2} + \\beta\\frac{dC}{dt} + \\gamma C = \\delta r(t)$ 의 상태방정식 시스템 행렬 $A$ 와 $B$ 는?",
  answer: "$A = \\begin{bmatrix} 0 & 1 \\\\ -\\gamma & -\\beta \\end{bmatrix}, \\quad B = \\begin{bmatrix} 0 \\\\ \\delta \\end{bmatrix}$\n\n💡 [변칙 대비: 2차 상태방정식 꿀팁]\n- $A$ 행렬 1행은 고정: `[0, 1]`\n- $A$ 행렬 2행은 계수 부호 반대!: 상수항 $-\\gamma$, 1차항 $-\\beta$ 순서\n- $B$ 행렬은 `[0, 우변입력계수]`"
};

data.push(newCard);

fs.writeFileSync('src/data/flashcards.json', JSON.stringify(data, null, 2), 'utf8');
console.log("Added state space card!");
