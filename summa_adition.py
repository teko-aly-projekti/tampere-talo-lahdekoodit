import pandas as pd

# Laita excel kansioon jonka nimi on excels
file_path = "excels/tamperetalo2024.xlsx" # <-- Vaihda oikea excel nimi jota haluat käyttää

all_sheets = pd.read_excel(file_path, sheet_name=None)

totals = {}

for sheet_name, df in all_sheets.items():
    if "Seloste" in df.columns and "Summa €" in df.columns:
        df["Summa €"] = pd.to_numeric(df["Summa €"], errors="coerce")

        for _, row in df.iterrows():
            caption = row["Seloste"]
            amount = row["Summa €"]

            if pd.notna(caption) and pd.notna(amount):
                totals[caption] = totals.get(caption, 0) + amount

result = pd.DataFrame(
    [{"Seloste": caption, "Koko summa €": total} for caption, total in totals.items()]
)

result = result.sort_values("Koko summa €", ascending=False)

result.to_excel("excels/selostesumma2024.xlsx", index=False) # <-- Vaihda oikea vuosi (älä vaihda nimeä muuten)

print(result)
