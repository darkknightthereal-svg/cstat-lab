import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BankChurners.csv")
print("Shape:", df.shape)
print(df.head())
df.info()

df = df.replace("Unknown", np.nan)
print("\nMissing values before handling:")
print(df.isnull().sum())

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
print("\nMissing values after handling:")
print(df.isnull().sum().sum())

counts = df["Attrition_Flag"].value_counts()
print("\nAttrition Flag ratio:")
print(counts / len(df))
plt.figure(figsize=(6, 6))
plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Attrition Flag Ratio")
plt.show()

categorical = ["Gender", "Education_Level", "Marital_Status", "Income_Category", "Card_Category"]
fig, axes = plt.subplots(2, 3, figsize=(18, 9))
for ax, col in zip(axes.flatten(), categorical):
    df[col].value_counts().plot(kind="bar", ax=ax, title=col)
    ax.set_xlabel("")
axes.flatten()[-1].axis("off")
plt.tight_layout()
plt.show()

numeric = ["Customer_Age", "Credit_Limit", "Total_Trans_Amt", "Total_Trans_Ct"]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for ax, col in zip(axes.flatten(), numeric):
    sns.boxplot(x="Attrition_Flag", y=col, data=df, ax=ax)
    ax.set_title(col)
plt.tight_layout()
plt.show()

print("\nDescriptive statistics:")
print(df.describe())

num_df = df.select_dtypes(include="number")
plt.figure(figsize=(14, 10))
sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

drop_cols = [c for c in df.columns if c == "CLIENTNUM" or c.startswith("Naive_Bayes")]
df = df.drop(columns=drop_cols)
print("\nDropped columns:", drop_cols)
print("Shape after dropping:", df.shape)
