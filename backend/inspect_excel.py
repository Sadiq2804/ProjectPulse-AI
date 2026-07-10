import pandas as pd

xls = pd.ExcelFile("uploads/S2P Project.xlsx")

for sheet in xls.sheet_names:
    print("=" * 60)
    print("Sheet:", sheet)

    df = pd.read_excel(xls, sheet_name=sheet)

    print("Columns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print()