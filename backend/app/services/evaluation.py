def evaluate(answer: str, context: str):
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    overlap = answer_words.intersection(context_words)

    relevance = len(overlap) / max(len(answer_words), 1)

    return {
        "answer_relevance": round(relevance, 2),
        "context_coverage": round(len(overlap) / max(len(context_words), 1), 2),
        "confidence_score": round(min(0.95, relevance + 0.25), 2)
    }
