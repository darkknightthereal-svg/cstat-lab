import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BankChurners.csv")
df["Attrition_Flag"].value_counts().plot(kind="bar", color=["steelblue", "tomato"])
plt.title("Attrition Flag")
plt.xlabel("Attrition Flag")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()
