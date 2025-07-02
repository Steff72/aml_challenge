import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "xselling_banking_data")


def test_csv_files_present():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    assert len(files) == 8


def test_account_columns_and_uniqueness():
    df = pd.read_csv(os.path.join(DATA_DIR, "account.csv"), sep=";")
    expected_columns = ["account_id", "district_id", "frequency", "date"]
    assert df.columns.tolist() == expected_columns
    assert df["account_id"].is_unique
    assert len(df) > 0


def test_card_types():
    df = pd.read_csv(os.path.join(DATA_DIR, "card.csv"), sep=";")
    assert "classic" in df["type"].unique()
    assert df["type"].nunique() >= 2
    assert len(df) > 0
