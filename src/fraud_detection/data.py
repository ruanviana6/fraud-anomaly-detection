"""Carregamento de dados utilizados no projeto."""

import pandas as pd

DATASET_URL = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"


def load_data(url: str = DATASET_URL) -> pd.DataFrame:
    """Carrega o dataset de transações financeiras."""
    return pd.read_csv(url)
