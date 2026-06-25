import json
import os

filepath = r"c:\Users\user\.gemini\antigravity\electric_gisa\flashcard-app\src\data\flashcards.json"

with open(filepath, "r", encoding="utf-8") as f:
    cards = json.load(f)

# 1. 제어공학의 라플라스 변환 관련 카드를 회로이론으로 이동
laplace_count = 0
for card in cards:
    if card.get("chapter") == "제어공학" and ("라플라스" in card.get("topic", "") or "라플라스" in card.get("question", "")):
        card["chapter"] = "회로이론"
        # 통일성을 위해 토픽 이름도 회로이론의 8단원에 맞춤
        if card["topic"].startswith("2."):
            card["topic"] = card["topic"].replace("2.", "8.")
        laplace_count += 1

# 2. 여러 도체계의 정전계(E, V, C, R) 누락 공식 추가 (전기자기학)
new_cards = [
    # 구도체 보충 (C는 기존 em-11-1에 있음, E, V는 점전하와 같음)
    {"id": "em-11-7", "chapter": "전기자기학", "topic": "11. 저항과 정전용량", "question": "반지름이 $a$ 인 구도체의 누설 저항 $R$ 은?", "answer": "$R = \\frac{\\rho}{4\\pi a} \\, [\\Omega]$"},
    
    # 동심 구도체 보충 (C는 기존 em-11-2에 있음)
    {"id": "em-11-8", "chapter": "전기자기학", "topic": "11. 전위와 정전용량", "question": "내구 반경 $a$, 외구 반경 $b$ 인 동심 구도체 사이의 전위차 $V$ 는?", "answer": "$V = \\frac{Q}{4\\pi\\varepsilon_0} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) \\, [\\text{V}]$"},
    {"id": "em-11-9", "chapter": "전기자기학", "topic": "11. 저항과 정전용량", "question": "내구 반경 $a$, 외구 반경 $b$ 인 동심 구도체의 누설 저항 $R$ 은?", "answer": "$R = \\frac{\\rho}{4\\pi} \\left( \\frac{1}{a} - \\frac{1}{b} \\right) \\, [\\Omega]$"},
    {"id": "em-11-10", "chapter": "전기자기학", "topic": "11. 전계", "question": "내구 반경 $a$, 외구 반경 $b$ 인 동심 구도체 내부(거리 $r$, $a < r < b$)의 전계 $E$ 는?", "answer": "$E = \\frac{Q}{4\\pi\\varepsilon_0 r^2} \\, [\\text{V/m}]$"},

    # 원주형 / 동축 케이블 보충 (E는 기존 em-9-1, C는 기존 em-11-3에 있음)
    {"id": "em-11-11", "chapter": "전기자기학", "topic": "11. 전위와 정전용량", "question": "내원주 반경 $a$, 외원주 반경 $b$ 인 원주형(동축 케이블) 콘덴서의 전위차 $V$ 는? (선전하밀도 $\\lambda$)", "answer": "$V = \\frac{\\lambda}{2\\pi\\varepsilon_0} \\ln\\left(\\frac{b}{a}\\right) \\, [\\text{V}]$"},
    {"id": "em-11-12", "chapter": "전기자기학", "topic": "11. 저항과 정전용량", "question": "내원주 반경 $a$, 외원주 반경 $b$ 인 원주형(동축 케이블) 콘덴서의 단위 길이당 누설 저항 $R$ 은?", "answer": "$R = \\frac{\\rho}{2\\pi} \\ln\\left(\\frac{b}{a}\\right) \\, [\\Omega\\cdot\\text{m}]$ (전체 길이가 $l$ 이면 분모에 $l$ 곱함)"},

    # 평행 왕복 도선 보충 (L만 기존 em-36-4에 있음)
    {"id": "em-11-13", "chapter": "전기자기학", "topic": "11. 정전용량", "question": "반경 $a$, 중심 간격 $d$ 인 평행 왕복 도선의 단위 길이당 정전용량 $C$ 는?", "answer": "$C = \\frac{\\pi\\varepsilon_0}{\\ln(d/a)} \\, [\\text{F/m}]$"},
    {"id": "em-11-14", "chapter": "전기자기학", "topic": "11. 전위와 정전용량", "question": "반경 $a$, 중심 간격 $d$ 인 평행 왕복 도선 사이의 전위차 $V$ 는? (선전하밀도 $\\lambda$)", "answer": "$V = \\frac{\\lambda}{\\pi\\varepsilon_0} \\ln\\left(\\frac{d}{a}\\right) \\, [\\text{V}]$"},

    # 평행판 콘덴서 보충 (E, C, R은 기존에 존재)
    {"id": "em-11-15", "chapter": "전기자기학", "topic": "11. 전위", "question": "간격 $d$ 인 평행판 콘덴서 양단 사이의 전위차 $V$ 와 전계 $E$ 의 관계식은?", "answer": "$V = E d \\, [\\text{V}]$"}
]

existing_ids = {c["id"] for c in cards}
added_count = 0
for nc in new_cards:
    if nc["id"] not in existing_ids:
        cards.append(nc)
        added_count += 1

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

print(f"라플라스 카드 {laplace_count}개를 회로이론으로 이동했습니다.")
print(f"여러 도체계 정전계 (E, V, C, R) 공식 {added_count}개를 추가했습니다.")
