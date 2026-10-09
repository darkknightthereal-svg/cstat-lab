import pandas as pd

df = pd.read_csv("state.csv")
print(df.head())

for col in ["Population", "Murder.Rate"]:
    print("\n", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Variance:", df[col].var())
