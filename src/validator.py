def validate_response(answer: str, sources: list[str]):
    issues = []

    if not sources:
        issues.append("No sources retrieved")

    if "I don't have enough context" in answer and sources:
        issues.append("Answer may be overly cautious")

    confidence = 0.9
    if not sources:
        confidence = 0.2
    elif len(sources) == 1:
        confidence = 0.7

    return {
        "passed": len(issues) == 0,
        "issues": issues,
        "confidence": confidence,
    }