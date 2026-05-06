import random

def compute_confidence(answer, verification):
    score = 0.5

    if "false" in verification.lower():
        score -= 0.2
    else:
        score += 0.2

    return max(0, min(1, score))
