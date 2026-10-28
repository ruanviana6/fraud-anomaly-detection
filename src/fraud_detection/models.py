"""Criação dos modelos supervisionados usados no projeto."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def build_logistic_baseline(max_iter: int = 1000) -> LogisticRegression:
    """Cria a Regressão Logística utilizada como baseline."""
    return LogisticRegression(max_iter=max_iter)


def build_random_forest(
    n_estimators: int = 100,
    random_state: int = 42,
    n_jobs: int = -1,
) -> RandomForestClassifier:
    """Cria a Random Forest usada como principal referência supervisionada."""
    return RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=n_jobs,
    )
