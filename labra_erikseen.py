import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_2023 = pd.read_excel("excels/selostesumma2023.xlsx")
df_2024 = pd.read_excel("excels/selostesumma2024.xlsx")
df_2025 = pd.read_excel("excels/selostesumma2025.xlsx")

mask_2023 = (df_2023["Seloste"].str.contains("-")) & (df_2023["Seloste"].str.len() < 20)
mask_2024 = (df_2024["Seloste"].str.contains("-")) & (df_2024["Seloste"].str.len() < 20)
mask_2025 = (df_2025["Seloste"].str.contains("-")) & (df_2025["Seloste"].str.len() < 20)

df_2023 = df_2023[mask_2023].rename(columns={"Koko summa €": "Summa2023"})
df_2024 = df_2024[mask_2024].rename(columns={"Koko summa €": "Summa2024"})
df_2025 = df_2025[mask_2025].rename(columns={"Koko summa €": "Summa2025"})

fig, axes = plt.subplots(3, 1, figsize=(16, 18))

def add_labels(ax, bars):
    for bar in bars:
        value = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            value,
            f"{value:,.2f} €",
            ha="center",
            va="bottom",
            fontsize=8,
            rotation=90
        )

# ------------
# 2023 chart
# ------------
ax = axes[0]
bars = ax.bar(df_2023["Seloste"], df_2023["Summa2023"], color="blue")
add_labels(ax, bars)
ax.set_title("Seloste 2023")
ax.set_xticklabels(df_2023["Seloste"], rotation=90)

# -------------
# 2024 chart
# -------------
ax = axes[1]
bars = ax.bar(df_2024["Seloste"], df_2024["Summa2024"], color="orange")
add_labels(ax, bars)
ax.set_title("Seloste 2024")
ax.set_xticklabels(df_2024["Seloste"], rotation=90)

# -------------
# 2025 chart
# -------------
ax = axes[2]
bars = ax.bar(df_2025["Seloste"], df_2025["Summa2025"], color="green")
add_labels(ax, bars)
ax.set_title("Seloste 2025")
ax.set_xticklabels(df_2025["Seloste"], rotation=90)

plt.tight_layout()
plt.show()
