import json

filepath = r"c:\Users\user\.gemini\antigravity\electric_gisa\flashcard-app\src\data\flashcards.json"

with open(filepath, "r", encoding="utf-8") as f:
    cards = json.load(f)

# The user wants strict separation.
# ct-1-2 (도전율, 고유저항) overlaps with em-21-1.
# ct-5-2 (결합계수) overlaps with em-35-1.
# We will remove these two from Circuit Theory to keep it strictly circuit analysis.

ids_to_remove = ["ct-1-2", "ct-5-2"]

new_cards = [c for c in cards if c["id"] not in ids_to_remove]

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(new_cards, f, indent=2, ensure_ascii=False)

print(f"Removed {len(cards) - len(new_cards)} overlapping cards.")
print(f"Total cards now: {len(new_cards)}")
