import pandas as pd

# Laita excel kansioon jonka nimi on excels
file_path = "excels/tamperetalo2025.xlsx" # <-- Vaihda oikea excel nimi jota haluat käyttää

all_sheets = pd.read_excel(file_path, sheet_name=None)

totals = {}

for sheet_name, df in all_sheets.items():
    if "Seloste" in df.columns and "Lkm" in df.columns:
        df["Lkm"] = pd.to_numeric(df["Lkm"], errors="coerce")

        for _, row in df.iterrows():
            caption = row["Seloste"]
            amount = row["Lkm"]

            if pd.notna(caption) and pd.notna(amount):
                totals[caption] = totals.get(caption, 0) + amount

result = pd.DataFrame(
    [{"Seloste": caption, "Lkm": total} for caption, total in totals.items()]
)

result = result.sort_values("Lkm", ascending=False)

result.to_excel("excels/selostelkm2025.xlsx", index=False) # <-- Vaihda oikea vuosi (älä vaihda nimeä muuten)

print(result)