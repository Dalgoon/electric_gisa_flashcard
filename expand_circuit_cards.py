import json

expanded_cards = [
    # 2. 정현파 교류 추가
    {"id": "ct-2-3", "chapter": "회로이론", "topic": "2. 파형별 실효값과 평균값", "question": "반파 정류파의 실효값과 평균값은? (최댓값 $V_m$)", "answer": "실효값: $\\frac{V_m}{2}$\n평균값: $\\frac{V_m}{\\pi}$"},
    {"id": "ct-2-4", "chapter": "회로이론", "topic": "2. 파형별 실효값과 평균값", "question": "삼각파(톱니파)의 실효값과 평균값은?", "answer": "실효값: $\\frac{V_m}{\\sqrt{3}}$\n평균값: $\\frac{V_m}{2}$"},
    {"id": "ct-2-5", "chapter": "회로이론", "topic": "2. 파형별 파고율과 파형율", "question": "구형파(사각파)의 파고율과 파형율은?", "answer": "파고율 = 1\n파형율 = 1\n(실효값, 평균값 모두 $V_m$ 으로 동일)"},

    # 3. 기본 교류회로 추가
    {"id": "ct-3-3", "chapter": "회로이론", "topic": "3. RLC 직렬 공진", "question": "RLC 직렬 회로의 공진 조건과 공진 주파수 $f_r$ 은?", "answer": "조건: $X_L = X_C$ (즉, 허수부 임피던스 = 0)\n\n$f_r = \\frac{1}{2\\pi\\sqrt{LC}} \\quad [\\text{Hz}]$"},
    {"id": "ct-3-4", "chapter": "회로이론", "topic": "3. 직렬 공진시 특성", "question": "RLC 직렬 공진 시 임피던스와 전류의 크기 특성은?", "answer": "임피던스 $Z$: **최소** ($Z=R$)\n전류 $I$: **최대**"},
    {"id": "ct-3-5", "chapter": "회로이론", "topic": "3. 선택도 (Q-factor)", "question": "RLC 직렬 공진 회로의 선택도(첨예도) $Q$ 를 $R, L, C$ 로 나타낸 공식은?", "answer": "$Q = \\frac{\\omega_r L}{R} = \\frac{1}{\\omega_r C R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$"},
    {"id": "ct-3-6", "chapter": "회로이론", "topic": "3. 병렬 공진", "question": "RLC 병렬 공진 시 임피던스와 전류의 크기 특성은?", "answer": "임피던스 $Z$: **최대**\n전류 $I$: **최소**"},

    # 4. 교류 전력 추가
    {"id": "ct-4-3", "chapter": "회로이론", "topic": "4. 복소 전력", "question": "전압 $\\dot{V}$, 전류 $\\dot{I}$ 일 때, 피상전력 $\\dot{P_a}$ 를 구하는 복소 전력 식은?", "answer": "$\\dot{P_a} = \\dot{V} \\overline{\\dot{I}} = P \\pm jP_r$\n(전류에 공액 복소수를 취함)"},

    # 5. 회로망 정리 (새로 추가)
    {"id": "ct-5-3", "chapter": "회로이론", "topic": "5. 회로망 정리", "question": "복잡한 회로를 하나의 등가 전압원 $V_{th}$ 와 직렬 등가 임피던스 $Z_{th}$ 로 단순화하는 정리는?", "answer": "테브난의 정리 (Thevenin's Theorem)"},
    {"id": "ct-5-4", "chapter": "회로이론", "topic": "5. 회로망 정리", "question": "다수의 전압원/전류원이 있는 선형 회로에서, 각 전원 단독으로 작용할 때의 응답의 합이 전체 응답과 같다는 정리는?", "answer": "중첩의 원리 (Superposition Theorem)"},
    {"id": "ct-5-5", "chapter": "회로이론", "topic": "5. 회로망 정리", "question": "중첩의 원리 적용 시, 나머지 전압원과 전류원의 처리 방법은?", "answer": "전압원: **단락 (Short)**\n전류원: **개방 (Open)**"},
    {"id": "ct-5-6", "chapter": "회로이론", "topic": "5. 최대 전력 전달", "question": "전원측 임피던스가 $Z_s = R_s + jX_s$ 일 때, 부하측 임피던스 $Z_L$ 에 최대 전력이 전달되기 위한 조건은?", "answer": "$Z_L = \\overline{Z_s} = R_s - jX_s$\n(전원 임피던스의 공액 복소수)"},
    {"id": "ct-5-7", "chapter": "회로이론", "topic": "5. 밀만의 정리", "question": "병렬로 연결된 여러 개의 전압원과 저항 회로에서 양단 전압 $V_{ab}$ 를 구하는 밀만의 정리 공식은?", "answer": "$V_{ab} = \\frac{\\sum \\frac{V_i}{R_i}}{\\sum \\frac{1}{R_i}} = \\frac{\\sum I_i}{\\sum Y_i}$"},

    # 6. 다상 교류 추가
    {"id": "ct-6-4", "chapter": "회로이론", "topic": "6. 2전력계법", "question": "2대의 전력계 $W_1, W_2$ 로 3상 전력을 측정할 때, 유효전력 $P$ 와 무효전력 $P_r$ 공식은?", "answer": "유효전력 $P = W_1 + W_2$\n\n무효전력 $P_r = \\sqrt{3} (W_1 - W_2)$"},
    {"id": "ct-6-5", "chapter": "회로이론", "topic": "6. Y-Delta 변환", "question": "대칭 3상 회로에서 $\\Delta$결선 임피던스 $Z_\\Delta$ 와 Y결선 임피던스 $Z_Y$ 의 관계는?", "answer": "$Z_\\Delta = 3 Z_Y$\n($\\Delta$결선 시 임피던스가 3배 커짐)"},

    # 7. 대칭좌표법 확장
    {"id": "ct-7-2", "chapter": "회로이론", "topic": "7. 고장 조건과 대칭분", "question": "1선 지락 고장 시 영상, 정상, 역상 전류 $I_0, I_1, I_2$ 의 관계는?", "answer": "$I_0 = I_1 = I_2 = \\frac{1}{3} I_g$\n(세 대칭분이 모두 같고 직렬로 연결된 것과 같음)"},
    {"id": "ct-7-3", "chapter": "회로이론", "topic": "7. 고장 조건과 대칭분", "question": "선간 단락 고장 시 포함되지 않는 대칭분 전류는?", "answer": "영상 전류 ($I_0 = 0$)\n(정상 전류 $I_1$ 과 역상 전류 $I_2$ 의 크기는 같고 방향이 반대)"},
    {"id": "ct-7-4", "chapter": "회로이론", "topic": "7. 비대칭률", "question": "비대칭률의 정의는?", "answer": "비대칭률 = $\\frac{\\text{역상분 크기}}{\\text{정상분 크기}} = \\frac{|I_2|}{|I_1|}$"},

    # 8. 라플라스 변환 및 s-영역 회로해석 (회로이론에 필수적임)
    {"id": "ct-8-3", "chapter": "회로이론", "topic": "8. 라플라스 회로 소자", "question": "저항 $R$, 인덕터 $L$, 커패시터 $C$ 의 라플라스 변환 (s-영역) 임피던스는?", "answer": "저항: $R$\n인덕터: $sL$\n커패시터: $\\frac{1}{sC}$"},
    {"id": "ct-8-4", "chapter": "회로이론", "topic": "8. 라플라스 변환 기본식", "question": "라플라스 변환의 선형성, 미분 정리의 수식은? ($f(0)=0$ 일 때)", "answer": "미분 정리: $\\mathscr{L} \\left[ \\frac{df(t)}{dt} \\right] = sF(s)$\n적분 정리: $\\mathscr{L} \\left[ \\int f(t)dt \\right] = \\frac{F(s)}{s}$"},

    # 10. 4단자망 확장
    {"id": "ct-10-4", "chapter": "회로이론", "topic": "10. 4단자망 파라미터 변환", "question": "대칭 4단자망에서 파라미터 $A$ 와 $D$ 의 관계는?", "answer": "$A = D$\n($A$: 개방 전압 이득의 역수, $D$: 단락 전류 이득의 역수)"},
    {"id": "ct-10-5", "chapter": "회로이론", "topic": "10. 4단자망 연결", "question": "두 개의 4단자망을 '종속 접속 (Cascade)' 할 때 전체 4단자 정수 행렬은?", "answer": "각 4단자망 행렬의 **곱 (행렬의 곱셈)**"},
    {"id": "ct-10-6", "chapter": "회로이론", "topic": "10. Z, Y 파라미터 연결", "question": "두 2단자망을 직렬 연결할 때와 병렬 연결할 때 편리한 파라미터는?", "answer": "직렬 연결: **Z 파라미터** (임피던스 행렬 합)\n병렬 연결: **Y 파라미터** (어드미턴스 행렬 합)"},

    # 11. 분포정수회로 확장
    {"id": "ct-11-4", "chapter": "회로이론", "topic": "11. 반사계수", "question": "특성 임피던스 $Z_0$ 선로에 부하 임피던스 $Z_L$ 이 연결될 때 반사계수 $\\rho$ 의 공식은?", "answer": "$\\rho = \\frac{Z_L - Z_0}{Z_L + Z_0}$"},
    {"id": "ct-11-5", "chapter": "회로이론", "topic": "11. 정재파비", "question": "반사계수 크기가 $|\\rho|$ 일 때 정재파비 $S$ (또는 VSWR) 공식은?", "answer": "$S = \\frac{1 + |\\rho|}{1 - |\\rho|}$"},

    # 12. 과도현상 확장
    {"id": "ct-12-3", "chapter": "회로이론", "topic": "12. RLC 직렬 과도현상", "question": "RLC 직렬 회로에서 직류 전압 인가 시 $R^2 < \\frac{4L}{C}$ 일 때의 과도 응답 형태는?", "answer": "**진동적 (부족제동, Underdamped)**\n\n(참고: $R^2 = 4L/C$ 이면 임계제동, $R^2 > 4L/C$ 이면 비진동)"},
    {"id": "ct-12-4", "chapter": "회로이론", "topic": "12. R-L 단락", "question": "전류 $I$ 가 흐르던 R-L 직렬회로를 단락시켰을 때 전류 $i(t)$ 식은?", "answer": "$i(t) = I e^{-\\frac{R}{L}t}$"},
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
