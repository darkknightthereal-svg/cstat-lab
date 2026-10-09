import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BankChurners.csv")
num_df = df.select_dtypes(include="number")
plt.figure(figsize=(14, 10))
sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
