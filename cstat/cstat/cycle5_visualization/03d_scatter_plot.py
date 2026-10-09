import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
plt.scatter(df["month_number"], df["toothpaste"], label="Toothpaste sales data")
plt.title("Toothpaste Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Number of units sold")
plt.xticks(df["month_number"])
plt.grid(True, linestyle="--")
plt.legend(loc="upper left")
plt.show()
