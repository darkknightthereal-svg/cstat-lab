import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BankChurners.csv")
categorical = ["Gender", "Education_Level", "Marital_Status", "Income_Category", "Card_Category"]
fig, axes = plt.subplots(2, 3, figsize=(18, 9))
for ax, col in zip(axes.flatten(), categorical):
    df[col].value_counts().plot(kind="bar", ax=ax, title=col)
    ax.set_xlabel("")
axes.flatten()[-1].axis("off")
plt.tight_layout()
plt.show()
