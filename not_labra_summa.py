import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

years = [2023, 2024, 2025] # <-- Lisää vuosi tähän
merged = None

def filter_df(df):
    mask = ~((df["Seloste"].str.contains("-")) & (df["Seloste"].str.len() < 20))
    return df[mask]

for y in years:
    df = pd.read_excel(f"excels/selostesumma{y}.xlsx")
    df = filter_df(df).rename(columns={"Koko summa €": f"Summa{y}"})

    if merged is None:
        merged = df
    else:
        merged = merged.merge(df, on="Seloste", how="inner")

x = np.arange(len(merged["Seloste"]))
width = 0.25

plt.figure(figsize=(14,7))

bars = [
    plt.bar(x - width, merged["Summa2023"], width, label="2023"),
    plt.bar(x, merged["Summa2024"], width, label="2024"),
    plt.bar(x + width, merged["Summa2025"], width, label="2025"),
    # Lisää vuosi tähän, esim. plt.bar(x + width * 2, merged["Summa2026"], width, label="2026")
]

# Poista #, jos haluat nähdä summat.

# for bar_group in bars:
#    for bar in bar_group:
#        value = bar.get_height()
#        plt.text(
#            bar.get_x() + bar.get_width() / 2,
#            value,
#            f"{value}",
#            ha="center",
#            va="bottom",
#            fontsize=8
#        )

plt.xticks(x, merged["Seloste"], rotation=90)
plt.ylabel("Koko summa €")
plt.title("2023 vs 2024 vs 2025") # <-- Lisää vuosi tähän
plt.legend()
plt.tight_layout()
plt.show()
