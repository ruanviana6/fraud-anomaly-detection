"""Regras simples de inferência e decisão de risco."""


def classify_probability(probability: float, threshold: float = 0.40) -> int:
    """Converte uma probabilidade de fraude em classe 0 ou 1."""
    return int(probability >= threshold)
