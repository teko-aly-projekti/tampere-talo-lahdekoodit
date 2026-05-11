import pandas as pd
import matplotlib.pyplot as plt

def load_year_totals(path, year):
    excel = pd.ExcelFile(path)
    totals = {}

    for sheet in excel.sheet_names:
        df = pd.read_excel(path, sheet_name=sheet)
        df["Summa €"] = pd.to_numeric(df["Summa €"], errors="coerce")

        month = sheet.split()[0].lower()
        totals[month] = totals.get(month, 0) + df["Summa €"].sum()

    return pd.DataFrame({"Kuukausi": totals.keys(), year: totals.values()})

years = [2023, 2024, 2025] # <-- Lisää vuosi tähän.
dfs = [load_year_totals(f"excels/tamperetalo{y}.xlsx", str(y)) for y in years]

merged = dfs[0]
for df in dfs[1:]:
    merged = merged.merge(df, on="Kuukausi")

plt.figure(figsize=(12,6))

for y in years:
    plt.plot(merged["Kuukausi"], merged[str(y)], marker="o", label=str(y))

plt.title("Kulutus")
plt.xlabel("Kuukausi")
plt.ylabel("Koko Summa €")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
