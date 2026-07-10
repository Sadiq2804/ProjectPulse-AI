from pathlib import Path
from typing import Dict

import pandas as pd


class ExcelParser:
    """
    Reads an Excel workbook and converts all sheets into cleaned DataFrames.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def parse(self) -> Dict[str, pd.DataFrame]:
        workbook = pd.read_excel(
            self.file_path,
            sheet_name=None,
            engine="openpyxl",
        )

        cleaned_data = {}

        for sheet_name, df in workbook.items():
            df = self.clean_dataframe(df)
            cleaned_data[sheet_name] = df

        return cleaned_data

    @staticmethod
    def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna(how="all")
        df = df.dropna(axis=1, how="all")

        df.columns = (
            df.columns.astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df.reset_index(drop=True)