import json

expanded_cards = [
    # 제어공학 추가
    {"id": "ce-1-2", "chapter": "제어공학", "topic": "1. 제어량의 분류", "question": "위치, 방위, 자세 등을 제어량으로 하며 기계적 변위를 추종하는 제어 방식은?", "answer": "서보 기구 (Servo mechanism)\n\n(예: 미사일 유도, 로봇 팔, 자동 선반)"},
    {"id": "ce-1-3", "chapter": "제어공학", "topic": "1. 제어량의 분류", "question": "온도, 압력, 유량, 액위, 농도 등을 제어량으로 하는 제어 방식은?", "answer": "프로세스 제어 (Process control)\n\n(예: 화학 공장, 보일러)"},
    {"id": "ce-1-4", "chapter": "제어공학", "topic": "1. 제어량의 분류", "question": "전압, 전류, 주파수, 속도 등을 제어량으로 하며 목표값이 일정한 제어 방식은?", "answer": "자동 조정 (Automatic regulation)\n\n(예: 정전압 장치, 조속기)"},
    {"id": "ce-2-5", "chapter": "제어공학", "topic": "2. 라플라스 변환 추가", "question": "초기값 정리 (Initial Value Theorem) 의 수식은?", "answer": "$\\lim_{t \\to 0} f(t) = \\lim_{s \\to \\infty} s F(s)$"},
    {"id": "ce-2-6", "chapter": "제어공학", "topic": "2. 라플라스 변환 추가", "question": "$t f(t)$ (시간 지연 / $t$ 곱셈 정리) 의 라플라스 변환은?", "answer": "$\\mathscr{L}[t f(t)] = -\\frac{d}{ds} F(s)$"},
    {"id": "ce-5-2", "chapter": "제어공학", "topic": "5. 2차 제어계 특성", "question": "2차 과도 응답에서 지연시간(Delay Time)과 상승시간(Rise Time)의 정의는?", "answer": "지연시간: 최종값의 **50%** 에 도달하는 시간\n상승시간: 최종값의 **10%에서 90%** (또는 0%에서 100%)까지 도달하는 시간"},
    {"id": "ce-8-3", "chapter": "제어공학", "topic": "8. 근궤적법 심화", "question": "근궤적의 이탈점(Break-away point)을 구하기 위한 특성 방정식의 조건은?", "answer": "$\\frac{dK}{ds} = 0$\n($K$를 $s$에 대해 미분하여 0이 되는 $s$값)"},
    {"id": "ce-9-3", "chapter": "제어공학", "topic": "9. 주파수 응답 심화", "question": "나이퀴스트 안정도 판별법의 방정식 $Z = P + N$ 에서 각 변수의 의미는?", "answer": "$Z$: 폐루프 전달함수의 우반면(불안정) 극점 수\n$P$: 개루프 전달함수의 우반면 극점 수\n$N$: 나이퀴스트 선도가 $(-1, j0)$ 점을 둘러싼 횟수\n\n(안정하려면 **$Z=0$** 이어야 함)"},
    {"id": "ce-10-3", "chapter": "제어공학", "topic": "10. 보상기", "question": "진상 보상기(Lead Compensator)의 역할과 특징은?", "answer": "위상을 앞서게 하여 **과도 응답(안정도, 속도) 개선**\n\n(지상 보상기는 정상 상태 오차 개선에 쓰임)"},
    {"id": "ce-11-2", "chapter": "제어공학", "topic": "11. z-변환", "question": "연속 시간 시스템의 $e^{sT}$ (샘플링 함수) 에 대응하는 이산 시스템의 z-변환 변수 $z$ 는?", "answer": "$z = e^{sT}$"},

    # 전기설비기술기준(KEC) 추가
    {"id": "kec-2-5", "chapter": "전기설비기술기준", "topic": "2. 접지시스템 세부", "question": "접지선의 색상 식별 기준은?", "answer": "**녹색-노란색** 교차 (Green/Yellow)\n\n(KEC 개정 전의 단일 녹색은 더 이상 사용되지 않음)"},
    {"id": "kec-3-5", "chapter": "전기설비기술기준", "topic": "3. 가공전선로 지지물", "question": "가공전선로 지지물(철탑 등)의 기초 안전율 기준은?", "answer": "**2.0** 이상\n\n(단, 이상 시 상정 하중에 대해서는 1.33 이상)"},
    {"id": "kec-3-6", "chapter": "전기설비기술기준", "topic": "3. 지선", "question": "가공전선로 지지물을 지지하는 '지선(Guy wire)'의 안전율과 연선 가닥수, 소선 지름 기준은?", "answer": "안전율: **2.5** 이상\n연선 가닥수: **3가닥** 이상\n소선 지름: **2.6mm** 이상 (금속선)"},
    {"id": "kec-4-2", "chapter": "전기설비기술기준", "topic": "4. 전선 접속", "question": "전선을 접속할 때 전기 저항과 인장 하중에 대한 규정은?", "answer": "1. 전선의 **전기 저항을 증가시키지 않을 것**\n2. 전선의 **인장 하중을 20% 이상 감소시키지 않을 것** (즉, 80% 이상 유지)"},
    {"id": "kec-5-4", "chapter": "전기설비기술기준", "topic": "5. 배선공사 장소별", "question": "폭발성 분진이나 가연성 가스가 있는 위험 장소에서 사용할 수 있는 옥내 배선 공사 3가지는?", "answer": "1. **금속관 공사**\n2. **케이블 공사** (캡타이어 케이블 제외)\n3. 합성수지관 공사 (일부 장소 제한적)"},
    {"id": "kec-5-5", "chapter": "전기설비기술기준", "topic": "5. 애자 사용 공사", "question": "저압 옥내 애자사용 공사에서 전선 상호 간의 이격거리와, 전선과 조영재 간의 이격거리는?", "answer": "전선 상호 간: **6cm** 이상\n전선과 조영재 간: **2.5cm** 이상 (400V 초과 시 4.5cm 이상)"},
    {"id": "kec-8-3", "chapter": "전기설비기술기준", "topic": "8. 지중전선로 종류", "question": "지중 전선로의 매설 방식(종류) 3가지는?", "answer": "1. 직접 매설식\n2. 관로식\n3. 암거식"},
    {"id": "kec-11-1", "chapter": "전기설비기술기준", "topic": "11. 분산형 전원", "question": "태양광 발전 설비에서 모듈, 전선, 개폐기 등을 절연 성능 저하로 인한 화재로부터 보호하기 위해 설치해야 하는 장치는?", "answer": "**누전 차단기** 또는 **지락 차단 장치**"},
    {"id": "kec-11-2", "chapter": "전기설비기술기준", "topic": "11. 분산형 전원", "question": "분산형 전원 계통 연계 시 전력계통의 단락 용량이 분산형 전원 정격 용량의 몇 배 이하일 경우 연계 변압기를 통해 접속해야 하는가?", "answer": "단락 용량이 정격 용량의 **20배** 이하인 경우"},
    {"id": "kec-12-1", "chapter": "전기설비기술기준", "topic": "12. 가공 케이블 시설", "question": "가공전선로에 케이블을 사용할 때 조가용선에 매달아 시설하는 경우 지지점 간의 거리는?", "answer": "조가용선 지지점 간 거리: **50cm** 이하\n(금속 테이프 등으로 지지 시 20cm 이하)"},
    {"id": "kec-12-2", "chapter": "전기설비기술기준", "topic": "12. 특고압 시가지 시설", "question": "시가지에 특고압 가공전선로를 시설할 때, 100kV 미만인 경우 전선 지표상 높이는?", "answer": "**10m** 이상 (절연전선 시 8m 이상)\n\n※ 35kV 이하: 10m (절연전선 8m)"},
    {"id": "kec-13-1", "chapter": "전기설비기술기준", "topic": "13. 보행자용 금속관", "question": "옥내 저압선로 중 사람이 쉽게 접촉할 우려가 있는 장소에 금속관/케이블 공사 시 제 몇 종 접지공사를 해야 하는가? (KEC 기준)", "answer": "KEC 개정으로 종별 접지(1,2,3종)가 폐지되었으며,\n**보호접지(PE)** 를 통해 접지단자함(등전위 본딩)에 연결해야 함."},
]

if __name__ == "__main__":
    filepath = r"c:\Users\user\.gemini\antigravity\electric_gisa\flashcard-app\src\data\flashcards.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        existing_cards = json.load(f)
        
    existing_ids = {card["id"] for card in existing_cards}
    cards_to_add = [c for c in expanded_cards if c["id"] not in existing_ids]
    
    combined_cards = existing_cards + cards_to_add
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(combined_cards, f, indent=2, ensure_ascii=False)
        
    print(f"Added {len(cards_to_add)} cards. Total cards: {len(combined_cards)}.")
