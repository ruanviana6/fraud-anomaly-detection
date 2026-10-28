"""Transformações reutilizáveis de preparação dos dados."""

import numpy as np
import pandas as pd


def add_amount_log(data: pd.DataFrame) -> pd.DataFrame:
    """Cria Amount_log sem alterar o DataFrame recebido."""
    prepared_data = data.copy()
    prepared_data["Amount_log"] = np.log1p(prepared_data["Amount"])
    return prepared_data
