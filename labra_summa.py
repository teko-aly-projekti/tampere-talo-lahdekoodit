import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

years = [2023, 2024, 2025] # <-- Lisää vuosi tähän.
dfs = {}

def filter_df(df):
    mask = (df["Seloste"].str.contains("-")) & (df["Seloste"].str.len() < 20)
    return df[mask]

for y in years:
    df = pd.read_excel(f"excels/selostesumma{y}.xlsx")
    df = filter_df(df).rename(columns={"Koko summa €": f"Summa{y}"})
    dfs[y] = df

merged = dfs[years[0]]
for y in years[1:]:
    merged = merged.merge(dfs[y], on="Seloste", how="inner")

x = np.arange(len(merged["Seloste"]))
width = 0.25

plt.figure(figsize=(14,7))

offsets = [-width, 0, width]
bars = []

for i, y in enumerate(years):
    bars.append(
        plt.bar(x + offsets[i], merged[f"Summa{y}"], width, label=str(y))
    )

for bar_group in bars:
    for bar in bar_group:
        value = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.2f} €",
            ha="center",
            va="bottom",
            fontsize=8,
            rotation=90
        )

plt.xticks(x, merged["Seloste"], rotation=90)
plt.ylabel("Koko summa €")
plt.title("2023 vs 2024 vs 2025")
plt.legend()
plt.tight_layout()
plt.show()
