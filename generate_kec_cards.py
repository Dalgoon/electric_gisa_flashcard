import json
import os

new_cards = [
    # 전기설비기술기준 (KEC)
    {"id": "kec-1-1", "chapter": "전기설비기술기준", "topic": "1. 절연저항", "question": "SELV 및 PELV 전로의 절연저항 기준값은?", "answer": "$0.5 \\text{ M}\\Omega \\text{ 이상}$ (시험전압 DC 250V)"},
    {"id": "kec-1-2", "chapter": "전기설비기술기준", "topic": "1. 절연저항", "question": "FELV 및 500V 이하 전로의 절연저항 기준값은?", "answer": "$1.0 \\text{ M}\\Omega \\text{ 이상}$ (시험전압 DC 500V)"},
    {"id": "kec-1-3", "chapter": "전기설비기술기준", "topic": "1. 절연저항", "question": "500V 초과 전로의 절연저항 기준값은?", "answer": "$1.0 \\text{ M}\\Omega \\text{ 이상}$ (시험전압 DC 1000V)"},
    
    {"id": "kec-2-1", "chapter": "전기설비기술기준", "topic": "2. 접지시스템", "question": "KEC 규정에 따른 접지방식의 종류 3가지는?", "answer": "1. TN 계통 (TN-S, TN-C, TN-C-S)\n2. TT 계통\n3. IT 계통"},
    {"id": "kec-2-2", "chapter": "전기설비기술기준", "topic": "2. 접지시스템", "question": "보호도체(PE)의 단면적 산정 기준 중, 상도체 단면적 $S$ 가 $16\\text{mm}^2$ 이하일 때 보호도체의 최소 단면적은?", "answer": "$S$ (상도체 단면적과 동일)"},
    {"id": "kec-2-3", "chapter": "전기설비기술기준", "topic": "2. 접지시스템", "question": "상도체 단면적 $S$ 가 $16\\text{mm}^2$ 초과 $35\\text{mm}^2$ 이하일 때 보호도체의 최소 단면적은?", "answer": "$16\\text{ mm}^2$"},
    {"id": "kec-2-4", "chapter": "전기설비기술기준", "topic": "2. 접지시스템", "question": "접지극의 매설 깊이 기준은?", "answer": "지표면으로부터 **0.75m** 이상 깊이"},

    {"id": "kec-3-1", "chapter": "전기설비기술기준", "topic": "3. 이격거리", "question": "저압 가공전선로의 도로 횡단 시 최소 지표상 높이는?", "answer": "**6m** 이상"},
    {"id": "kec-3-2", "chapter": "전기설비기술기준", "topic": "3. 이격거리", "question": "저압 가공전선로의 철도 횡단 시 레일면상 높이는?", "answer": "**6.5m** 이상"},
    {"id": "kec-3-3", "chapter": "전기설비기술기준", "topic": "3. 이격거리", "question": "고압 가공전선로와 식물 사이의 최소 이격거리는?", "answer": "**1.5m** 이상"},
    {"id": "kec-3-4", "chapter": "전기설비기술기준", "topic": "3. 이격거리", "question": "특고압(35kV 이하) 가공전선과 건조물 상부의 이격거리는?", "answer": "절연전선 사용 시 **2.5m** 이상\n나전선 사용 시 **3m** 이상"},

    {"id": "kec-4-1", "chapter": "전기설비기술기준", "topic": "4. 전선", "question": "절연전선의 식별 색상 기준 중 L1, L2, L3, N, PE 도체의 색상은?", "answer": "L1: 갈색\nL2: 흑색\nL3: 회색\nN(중성선): 청색\nPE(보호도체): 녹색-노란색 교차"},

    {"id": "kec-5-1", "chapter": "전기설비기술기준", "topic": "5. 배선설비", "question": "금속관 공사에서 절연전선을 동일 관 내에 넣을 때 관내 단면적의 몇 % 이하로 해야 하는가?", "answer": "전선 피복을 포함한 단면적 총합이 관내 단면적의 **32%** 이하 (서로 다른 굵기)\n\n(단, 동일한 굵기일 경우 **48%** 이하)"},
    {"id": "kec-5-2", "chapter": "전기설비기술기준", "topic": "5. 배선설비", "question": "합성수지관 공사에서 관의 지지점 간의 거리는?", "answer": "**1.5m** 이하"},
    {"id": "kec-5-3", "chapter": "전기설비기술기준", "topic": "5. 배선설비", "question": "가요전선관 공사에서 1종 가요전선관의 곡률 반경은 관 안지름의 몇 배 이상이어야 하는가?", "answer": "**6배** 이상"},

    {"id": "kec-6-1", "chapter": "전기설비기술기준", "topic": "6. 보호장치", "question": "과전류 차단기로 저압 전로에 사용하는 퓨즈(gG)의 63A 이하 규격에서 용단시간 기준은?", "answer": "정격전류의 1.25배에서 60분 이내에 용단되지 않아야 하며,\n1.6배 전류에서 60분 이내에 용단되어야 함."},
    {"id": "kec-6-2", "chapter": "전기설비기술기준", "topic": "6. 보호장치", "question": "배선용 차단기(MCCB)의 63A 이하 산업용 규격 동작시간은?", "answer": "정격전류의 1.05배에서 부동작(60분),\n1.3배에서 동작(60분 이내)"},
    {"id": "kec-6-3", "chapter": "전기설비기술기준", "topic": "6. 보호장치", "question": "누전차단기(RCD)의 인체보호용 고감도 고속형의 정격 감도전류와 동작시간 기준은?", "answer": "감도전류: **30mA** 이하\n동작시간: **0.03초** 이내"},

    {"id": "kec-7-1", "chapter": "전기설비기술기준", "topic": "7. 피뢰설비", "question": "수뢰부 시스템의 보호방식 3가지는?", "answer": "1. 보호각법\n2. 회전구체법\n3. 메시법(망상법)"},
    {"id": "kec-7-2", "chapter": "전기설비기술기준", "topic": "7. 피뢰설비", "question": "피뢰설비의 인하도선은 1등급 기준 몇 개 이상 설치해야 하는가?", "answer": "**2개** 이상"},

    {"id": "kec-8-1", "chapter": "전기설비기술기준", "topic": "8. 지중전선로", "question": "지중전선로를 직접매설식으로 시설할 때 매설 깊이는?", "answer": "차량 등 중량물 압력 우려 장소: **1.0m** 이상\n그 밖의 장소: **0.6m** 이상\n(※ KEC 개정으로 1.2m에서 1.0m로 완화)"},
    {"id": "kec-8-2", "chapter": "전기설비기술기준", "topic": "8. 지중전선로", "question": "지중전선로에 사용되는 전선의 종류는?", "answer": "반드시 **케이블**을 사용해야 함"},

    {"id": "kec-9-1", "chapter": "전기설비기술기준", "topic": "9. 풍압하중", "question": "가공전선로 지지물에 작용하는 갑종 풍압하중에서 목주나 원형 철근콘크리트주의 기준 면적당 하중은?", "answer": "**588 Pa** ($588\\text{N/m}^2$)"},
    {"id": "kec-9-2", "chapter": "전기설비기술기준", "topic": "9. 풍압하중", "question": "빙설이 많은 지방에서 을종 풍압하중을 적용할 때 빙설의 두께와 비중 기준은?", "answer": "두께 **6mm**, 비중 **0.9**"},

    {"id": "kec-10-1", "chapter": "전기설비기술기준", "topic": "10. 전로의 절연내력 시험", "question": "최대사용전압이 7kV 이하인 전로의 절연내력 시험전압은?", "answer": "최대사용전압의 **1.5배** (최저 500V)\n\n※ 시험 방법: 10분간 가하여 견뎌야 함"},
    {"id": "kec-10-2", "chapter": "전기설비기술기준", "topic": "10. 전로의 절연내력 시험", "question": "최대사용전압이 7kV 초과 60kV 이하인 중성점 비접지식 전로의 시험전압은?", "answer": "최대사용전압의 **1.25배** (최저 10500V)"},
    {"id": "kec-10-3", "chapter": "전기설비기술기준", "topic": "10. 전로의 절연내력 시험", "question": "중성점 다중접지식 (22.9kV 등) 전로의 절연내력 시험전압은?", "answer": "최대사용전압의 **0.92배**"}
]

if __name__ == "__main__":
    filepath = r"c:\Users\user\.gemini\antigravity\electric_gisa\flashcard-app\src\data\flashcards.json"
    
    with open(filepath, "r", encoding="utf-8") as f:
        existing_cards = json.load(f)
        
    existing_ids = {card["id"] for card in existing_cards}
    cards_to_add = [c for c in new_cards if c["id"] not in existing_ids]
    
    combined_cards = existing_cards + cards_to_add
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(combined_cards, f, indent=2, ensure_ascii=False)
        
    print(f"Added {len(cards_to_add)} cards. Total cards: {len(combined_cards)}.")
