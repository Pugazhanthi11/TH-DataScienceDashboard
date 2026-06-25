import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_covid_data.csv")

# Create new features
df["death_rate"] = (df["deaths"] / df["cases"]) * 100
df["recovery_rate"] = (df["recovered"] / df["cases"]) * 100
df["active_rate"] = (df["active"] / df["cases"]) * 100

# Replace infinity values if any
df = df.fillna(0)

# Save new dataset
df.to_csv("featured_covid_data.csv", index=False)

print("Feature engineering completed successfully!")
print(df[["country", "death_rate", "recovery_rate", "active_rate"]].head())