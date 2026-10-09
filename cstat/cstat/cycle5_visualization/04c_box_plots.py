import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BankChurners.csv")
numeric = ["Customer_Age", "Credit_Limit", "Total_Trans_Amt", "Total_Trans_Ct"]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for ax, col in zip(axes.flatten(), numeric):
    sns.boxplot(x="Attrition_Flag", y=col, data=df, ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.show()
