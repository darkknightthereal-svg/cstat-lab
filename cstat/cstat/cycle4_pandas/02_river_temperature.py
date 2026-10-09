import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("river_temperature.csv")
print(df.head())
print(df.columns.tolist())


def find_col(keyword):
    for c in df.columns:
        if keyword in c.lower():
            return c


site_col = find_col("site") or find_col("name") or find_col("location")
temp_col = find_col("temp")
oxygen_col = find_col("oxygen")

swale = df[df[site_col] == "Swale at Catterick Bridge"]
print("\nRecords for Swale at Catterick Bridge:", len(swale))
print(swale.head())

print("\nMean temperature:", swale[temp_col].mean())
print("Median dissolved oxygen:", swale[oxygen_col].median())

plt.hist(swale[temp_col].dropna(), bins=15, edgecolor="black")
plt.title("Temperature - Swale at Catterick Bridge")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()
