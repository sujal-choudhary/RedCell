import json
from pathlib import Path


# Load intent definitions safely
INTENT_FILE = Path("config/intents.json")

with open(INTENT_FILE, "r", encoding="utf-8") as f:
    INTENTS = json.load(f)


def detect_intent(tokens: list) -> dict:
    """
    Detect user intent based on tokens.
    Returns intent name + confidence score.
    """

    joined_text = " ".join(tokens)

    best_intent = "unknown"
    best_score = 0

    for intent, keywords in INTENTS.items():
        score = 0

        for keyword in keywords:
            if keyword in joined_text:
                score += 1

        if score > best_score:
            best_score = score
            best_intent = intent

    confidence = round(best_score / max(len(tokens), 1), 2)

    return {
        "intent": best_intent,
        "confidence": confidence
    }
