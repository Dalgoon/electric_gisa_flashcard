import json
import os

new_cards = [
    # 회로이론
    {"id": "ct-1-1", "chapter": "회로이론", "topic": "1. 직류회로", "question": "옴의 법칙 (Ohm's Law)의 수식은?", "answer": "$V = IR \\quad [\\text{V}]$"},
    {"id": "ct-1-2", "chapter": "회로이론", "topic": "1. 직류회로", "question": "도체의 저항 $R$과 도전율 $k$(또는 $\\sigma$)의 관계식은?", "answer": "$R = \\rho \\frac{l}{A} = \\frac{1}{k} \\frac{l}{A} \\quad [\\Omega]$"},
    {"id": "ct-1-3", "chapter": "회로이론", "topic": "1. 직류회로", "question": "전력 $P$ 와 전력량 $W$ 의 관계식은?", "answer": "$P = VI = I^2 R = \\frac{V^2}{R} \\quad [\\text{W}]$\n\n$W = Pt = VIt \\quad [\\text{J}]$"},
    {"id": "ct-2-1", "chapter": "회로이론", "topic": "2. 정현파 교류", "question": "정현파 교류 $v(t) = V_m \\sin(\\omega t + \\theta)$ 에서 실효값 $V$ 는?", "answer": "$V = \\frac{V_m}{\\sqrt{2}} \\approx 0.707 V_m$"},
    {"id": "ct-2-2", "chapter": "회로이론", "topic": "2. 정현파 교류", "question": "정현파 교류의 파고율과 파형율은?", "answer": "파고율 = $\\frac{\\text{최댓값}}{\\text{실효값}} = \\sqrt{2} \\approx 1.414$\n\n파형율 = $\\frac{\\text{실효값}}{\\text{평균값}} = \\frac{\\pi}{2\\sqrt{2}} \\approx 1.11$"},
    {"id": "ct-3-1", "chapter": "회로이론", "topic": "3. 기본 교류회로 (R, L, C)", "question": "인덕터 $L$ 과 커패시터 $C$ 의 리액턴스 $X_L, X_C$ 는?", "answer": "$X_L = \\omega L = 2\\pi f L \\quad [\\Omega]$\n\n$X_C = \\frac{1}{\\omega C} = \\frac{1}{2\\pi f C} \\quad [\\Omega]$"},
    {"id": "ct-3-2", "chapter": "회로이론", "topic": "3. 기본 교류회로 (R, L, C)", "question": "RL 직렬회로의 합성 임피던스 $Z$ 와 위상각 $\\theta$ 는?", "answer": "$Z = \\sqrt{R^2 + X_L^2} = \\sqrt{R^2 + (\\omega L)^2}$\n\n$\\theta = \\tan^{-1}\\left(\\frac{X_L}{R}\\right)$"},
    {"id": "ct-4-1", "chapter": "회로이론", "topic": "4. 교류 전력", "question": "피상전력 $P_a$, 유효전력 $P$, 무효전력 $P_r$ 의 관계식은?", "answer": "$P_a = VI = \\sqrt{P^2 + P_r^2} \\quad [\\text{VA}]$\n$P = VI \\cos\\theta \\quad [\\text{W}]$\n$P_r = VI \\sin\\theta \\quad [\\text{Var}]$"},
    {"id": "ct-4-2", "chapter": "회로이론", "topic": "4. 교류 전력", "question": "역률(Power Factor) 개선을 위해 콘덴서를 설치할 때, 필요한 콘덴서 용량 $Q_c$ 는?", "answer": "$Q_c = P(\\tan\\theta_1 - \\tan\\theta_2) \\quad [\\text{kVA}]$\n(P: 유효전력, $\\theta_1$: 개선전, $\\theta_2$: 개선후)"},
    {"id": "ct-5-1", "chapter": "회로이론", "topic": "5. 유도 결합 회로", "question": "자기 인덕턴스 $L_1, L_2$ 이고 상호 인덕턴스 $M$ 인 두 코일의 가동 접속 합성 인덕턴스는?", "answer": "$L = L_1 + L_2 + 2M$"},
    {"id": "ct-5-2", "chapter": "회로이론", "topic": "5. 유도 결합 회로", "question": "결합 계수 $k$ 와 $L_1, L_2, M$ 의 관계식은?", "answer": "$M = k\\sqrt{L_1 L_2} \\quad (0 \\le k \\le 1)$"},
    {"id": "ct-6-1", "chapter": "회로이론", "topic": "6. 다상 교류", "question": "3상 Y결선(성형 결선)에서 선간전압 $V_l$과 상전압 $V_p$, 선전류 $I_l$과 상전류 $I_p$ 의 관계는?", "answer": "$V_l = \\sqrt{3}V_p \\angle 30^\\circ$ (선간전압이 위상이 30도 앞섬)\n\n$I_l = I_p$"},
    {"id": "ct-6-2", "chapter": "회로이론", "topic": "6. 다상 교류", "question": "3상 $\\Delta$결선(삼각 결선)에서 선간전압과 상전압, 선전류와 상전류의 관계는?", "answer": "$V_l = V_p$\n\n$I_l = \\sqrt{3}I_p \\angle -30^\\circ$ (선전류가 위상이 30도 뒤짐)"},
    {"id": "ct-6-3", "chapter": "회로이론", "topic": "6. 다상 교류", "question": "V결선의 출력 $P_V$ 와 3상 출력 $P_3$ 의 관계, 그리고 이용률과 출력비는?", "answer": "$P_V = \\sqrt{3} P_1$ (단상 변압기 1대 용량의 $\\sqrt{3}$배)\n\n이용률 = $\\frac{\\sqrt{3}}{2} \\approx 86.6\\%$\n출력비 = $\\frac{1}{\\sqrt{3}} \\approx 57.7\\%$"},
    {"id": "ct-7-1", "chapter": "회로이론", "topic": "7. 대칭 좌표법", "question": "영상, 정상, 역상 전류 $I_0, I_1, I_2$ 를 상전류 $I_a, I_b, I_c$ 로 나타내는 공식은? (벡터 연산자 $a = e^{j120^\\circ}$)", "answer": "$I_0 = \\frac{1}{3}(I_a + I_b + I_c)$\n$I_1 = \\frac{1}{3}(I_a + a I_b + a^2 I_c)$\n$I_2 = \\frac{1}{3}(I_a + a^2 I_b + a I_c)$"},
    {"id": "ct-8-1", "chapter": "회로이론", "topic": "8. 비정현파 교류", "question": "비정현파의 실효값 $V_{rms}$ 구하는 방법은?", "answer": "각 고조파 실효값의 제곱의 합의 제곱근\n\n$V_{rms} = \\sqrt{V_0^2 + V_1^2 + V_2^2 + \\cdots}$"},
    {"id": "ct-8-2", "chapter": "회로이론", "topic": "8. 비정현파 교류", "question": "왜형률 (Distortion Factor) 의 정의는?", "answer": "왜형률 = $\\frac{\\text{전 고조파의 실효값}}{\\text{기본파의 실효값}} = \\frac{\\sqrt{V_2^2 + V_3^2 + \\cdots}}{V_1}$"},
    {"id": "ct-9-1", "chapter": "회로이론", "topic": "9. 2단자망", "question": "구동점 임피던스 $Z(s)$ 의 영점(Zero)과 극점(Pole)이 의미하는 것은?", "answer": "영점: $Z(s) = 0$ 이 되는 $s$ 값 (회로 단락 상태)\n\n극점: $Z(s) = \\infty$ 가 되는 $s$ 값 (회로 개방 상태)"},
    {"id": "ct-10-1", "chapter": "회로이론", "topic": "10. 4단자망", "question": "4단자 기본 방정식 (전압 $V_1, V_2$, 전류 $I_1, I_2$와 ABCD 파라미터)은?", "answer": "$\\begin{pmatrix} V_1 \\\\ I_1 \\end{pmatrix} = \\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix} \\begin{pmatrix} V_2 \\\\ I_2 \\end{pmatrix}$"},
    {"id": "ct-10-2", "chapter": "회로이론", "topic": "10. 4단자망", "question": "4단자망의 파라미터 $A, B, C, D$ 의 의미와 성질 ($AD-BC=1$)은?", "answer": "$A$: 전압비, $B$: 임피던스\n$C$: 어드미턴스, $D$: 전류비\n수동 선형 회로에서는 항상 $AD - BC = 1$ 성립"},
    {"id": "ct-10-3", "chapter": "회로이론", "topic": "10. 4단자망", "question": "영상 임피던스 $Z_{01}, Z_{02}$ 를 $A,B,C,D$ 로 표현하면?", "answer": "$Z_{01} = \\sqrt{\\frac{AB}{CD}}$\n\n$Z_{02} = \\sqrt{\\frac{BD}{AC}}$"},
    {"id": "ct-11-1", "chapter": "회로이론", "topic": "11. 분포정수회로", "question": "분포정수회로에서 특성 임피던스 $Z_0$ 와 전파 정수 $\\gamma$ 는? ($Z = R+j\\omega L, Y = G+j\\omega C$)", "answer": "$Z_0 = \\sqrt{\\frac{Z}{Y}} = \\sqrt{\\frac{R+j\\omega L}{G+j\\omega C}}$\n\n$\\gamma = \\sqrt{ZY} = \\alpha + j\\beta$ ($\\alpha$: 감쇠정수, $\\beta$: 위상정수)"},
    {"id": "ct-11-2", "chapter": "회로이론", "topic": "11. 분포정수회로", "question": "무손실 선로 ($R=0, G=0$)의 특성 임피던스 $Z_0$ 와 전파 속도 $v$ 는?", "answer": "$Z_0 = \\sqrt{\\frac{L}{C}}$\n\n$v = \\frac{\\omega}{\\beta} = \\frac{1}{\\sqrt{LC}}$"},
    {"id": "ct-11-3", "chapter": "회로이론", "topic": "11. 분포정수회로", "question": "무왜곡 선로의 조건은?", "answer": "$RC = LG$ (또는 $\\frac{R}{L} = \\frac{G}{C}$)"},
    {"id": "ct-12-1", "chapter": "회로이론", "topic": "12. 과도현상", "question": "R-L 직렬 회로의 직류 인가 시 전류 $i(t)$ 와 시정수 $\\tau$ 는?", "answer": "$i(t) = \\frac{E}{R}(1 - e^{-\\frac{R}{L}t})$\n\n시정수 $\\tau = \\frac{L}{R} \\quad [\\text{s}]$"},
    {"id": "ct-12-2", "chapter": "회로이론", "topic": "12. 과도현상", "question": "R-C 직렬 회로의 직류 인가 시 전류 $i(t)$ 와 시정수 $\\tau$ 는?", "answer": "$i(t) = \\frac{E}{R} e^{-\\frac{1}{RC}t}$\n\n시정수 $\\tau = RC \\quad [\\text{s}]$"},

    # 제어공학
    {"id": "ce-1-1", "chapter": "제어공학", "topic": "1. 자동제어계의 요소", "question": "피드백 제어계에서 '조작량'을 만들어 '제어 대상'에 가하는 요소의 이름은?", "answer": "제어 요소 (Control Element)"},
    {"id": "ce-2-1", "chapter": "제어공학", "topic": "2. 라플라스 변환", "question": "단위 계단 함수(Unit Step Function) $u(t)$ 의 라플라스 변환은?", "answer": "$\\mathscr{L}[u(t)] = \\frac{1}{s}$"},
    {"id": "ce-2-2", "chapter": "제어공학", "topic": "2. 라플라스 변환", "question": "$e^{-at}$ 의 라플라스 변환은?", "answer": "$\\mathscr{L}[e^{-at}] = \\frac{1}{s+a}$"},
    {"id": "ce-2-3", "chapter": "제어공학", "topic": "2. 라플라스 변환", "question": "$\\sin(\\omega t)$ 와 $\\cos(\\omega t)$ 의 라플라스 변환은?", "answer": "$\\mathscr{L}[\\sin\\omega t] = \\frac{\\omega}{s^2 + \\omega^2}$\n\n$\\mathscr{L}[\\cos\\omega t] = \\frac{s}{s^2 + \\omega^2}$"},
    {"id": "ce-2-4", "chapter": "제어공학", "topic": "2. 라플라스 변환", "question": "최종값 정리 (Final Value Theorem) 의 수식은?", "answer": "$\\lim_{t \\to \\infty} f(t) = \\lim_{s \\to 0} s F(s)$"},
    {"id": "ce-3-1", "chapter": "제어공학", "topic": "3. 전달함수", "question": "전달함수 $G(s)$ 의 정의는?", "answer": "$G(s) = \\frac{C(s)}{R(s)} \\quad \\text{(초기값을 0으로 한 경우)}$\n(입력의 라플라스 변환에 대한 출력의 라플라스 변환 비)"},
    {"id": "ce-3-2", "chapter": "제어공학", "topic": "3. 전달함수", "question": "폐루프 (피드백) 제어계의 전달함수 $M(s)$ 는? (전향경로 $G(s)$, 피드백 $H(s)$)", "answer": "$M(s) = \\frac{G(s)}{1 \\pm G(s)H(s)}$\n(부계환(Negative Feedback)일 때 분모는 $+$, 정계환일 때 분모는 $-$)"},
    {"id": "ce-4-1", "chapter": "제어공학", "topic": "4. 블록선도와 신호흐름선도", "question": "메이슨의 이득 공식(Mason's Gain Formula)에서 분모 $\\Delta$ 의 형태는?", "answer": "$\\Delta = 1 - \\sum (\\text{모든 개별 루프 이득}) + \\sum (\\text{서로 접촉하지 않는 2개 루프 이득의 곱}) - \\cdots$"},
    {"id": "ce-5-1", "chapter": "제어공학", "topic": "5. 제어계의 과도응답", "question": "2차 제어계의 특성 방정식 $s^2 + 2\\zeta\\omega_n s + \\omega_n^2 = 0$ 에서 감쇠비 $\\zeta$ 에 따른 응답 판별은?", "answer": "$\\zeta > 1$ : 과제동 (Overdamped)\n$\\zeta = 1$ : 임계제동 (Critically damped)\n$0 < \\zeta < 1$ : 부족제동 (Underdamped, 진동 발생)\n$\\zeta = 0$ : 무제동 (지속 진동)"},
    {"id": "ce-6-1", "chapter": "제어공학", "topic": "6. 정상상태 오차", "question": "위치 편차 상수 $K_p$, 속도 편차 상수 $K_v$, 가속도 편차 상수 $K_a$ 의 정의는?", "answer": "$K_p = \\lim_{s \\to 0} G(s)$\n$K_v = \\lim_{s \\to 0} s G(s)$\n$K_a = \\lim_{s \\to 0} s^2 G(s)$"},
    {"id": "ce-6-2", "chapter": "제어공학", "topic": "6. 정상상태 오차", "question": "제어계의 형(Type) 판별 기준은?", "answer": "개루프 전달함수 $G(s)H(s)$ 의 원점 극점 수 (즉, 분모의 $s^n$ 에서 $n$ 의 값)\n$n=0$: 0형, $n=1$: 1형, $n=2$: 2형"},
    {"id": "ce-7-1", "chapter": "제어공학", "topic": "7. 안정도 판별 (루스-후르비츠)", "question": "루스 (Routh) 안정도 판별법에서 제어계가 안정하기 위한 필요충분조건은?", "answer": "루스 배열의 제 1열의 모든 요소가 **부호 변화가 없어야(모두 양수이어야)** 한다."},
    {"id": "ce-8-1", "chapter": "제어공학", "topic": "8. 근궤적법", "question": "근궤적의 출발점과 도착점은?", "answer": "출발점 ($K=0$): 개루프 전달함수의 **극점 (Pole)**\n도착점 ($K=\\infty$): 개루프 전달함수의 **영점 (Zero)** 또는 무한대"},
    {"id": "ce-8-2", "chapter": "제어공학", "topic": "8. 근궤적법", "question": "근궤적의 점근선 각도 $\\theta$ 공식은? (극점 수 $P$, 영점 수 $Z$)", "answer": "$\\theta = \\frac{(2k + 1)\\pi}{P - Z} \\quad (k = 0, 1, 2, \\dots)$"},
    {"id": "ce-9-1", "chapter": "제어공학", "topic": "9. 주파수 응답 (보데선도)", "question": "보데 선도에서 이득(Gain)을 데시벨(dB)로 나타내는 공식은?", "answer": "$G_{dB} = 20 \\log_{10} |G(j\\omega)| \\quad [\\text{dB}]$"},
    {"id": "ce-9-2", "chapter": "제어공학", "topic": "9. 주파수 응답", "question": "이득 여유(Gain Margin, GM)와 위상 여유(Phase Margin, PM)가 안정하기 위한 조건은?", "answer": "안정 조건: $\\text{GM} > 0 \\text{ dB}$, $\\text{PM} > 0^\\circ$\n\n(불안정 시: $\\text{GM} < 0$, $\\text{PM} < 0$)"},
    {"id": "ce-10-1", "chapter": "제어공학", "topic": "10. 상태 공간법", "question": "상태 방정식 $\\dot{\\mathbf{x}}(t) = \\mathbf{A}\\mathbf{x}(t) + \\mathbf{B}u(t)$ 에서 특성 방정식은 어떻게 구하는가?", "answer": "$|s\\mathbf{I} - \\mathbf{A}| = 0$ (여기서 $\\mathbf{I}$는 단위행렬)"},
    {"id": "ce-10-2", "chapter": "제어공학", "topic": "10. 상태 공간법", "question": "상태 천이 행렬 (State Transition Matrix) $\\mathbf{\\Phi}(t)$ 의 라플라스 역변환 식은?", "answer": "$\\mathbf{\\Phi}(t) = \\mathscr{L}^{-1}[ (s\\mathbf{I} - \\mathbf{A})^{-1} ]$"},
    {"id": "ce-11-1", "chapter": "제어공학", "topic": "11. 시퀀스 제어", "question": "AND 게이트와 OR 게이트의 논리식과 기능은?", "answer": "AND (논리곱, 직렬접점): $Y = A \\cdot B$\nOR (논리합, 병렬접점): $Y = A + B$"}
]

if __name__ == "__main__":
    filepath = r"c:\Users\user\.gemini\antigravity\electric_gisa\flashcard-app\src\data\flashcards.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        existing_cards = json.load(f)
        
    # Check if we already added them to prevent duplicates on rerun
    existing_ids = {card["id"] for card in existing_cards}
    cards_to_add = [c for c in new_cards if c["id"] not in existing_ids]
    
    combined_cards = existing_cards + cards_to_add
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(combined_cards, f, indent=2, ensure_ascii=False)
        
    print(f"Added {len(cards_to_add)} cards. Total cards: {len(combined_cards)}.")
