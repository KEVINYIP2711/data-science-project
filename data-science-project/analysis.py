"""Automobile Sales During Recession Analysis - CISC7204 portfolio project."""
from pathlib import Path
import io
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "d51iMGfp_t0QpO30Lym-dw/automobile-sales.csv"
)
OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(exist_ok=True)
response = requests.get(DATA_URL, timeout=30)
response.raise_for_status()
df = pd.read_csv(io.StringIO(response.text))

annual = df.groupby("Year", as_index=True)["Automobile_Sales"].mean()
plt.figure(figsize=(10, 6))
annual.plot(kind="line")
plt.xlabel("Year")
plt.ylabel("Average Automobile Sales")
plt.title("Average Automobile Sales by Year")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "annual_automobile_sales.png", dpi=160)
plt.close()

gdp = df.groupby(["Year", "Recession"], as_index=False)["GDP"].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(data=gdp, x="Year", y="GDP", hue="Recession", marker="o")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.title("GDP Variation by Recession Status")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "gdp_recession_status.png", dpi=160)
plt.close()
print(f"Loaded {len(df):,} rows.")
print("Created two visualizations in visualizations/.")
