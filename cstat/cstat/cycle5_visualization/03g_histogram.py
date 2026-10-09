import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
bins = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(df["total_profit"], bins=bins, edgecolor="black")
plt.title("Profit Data Histogram")
plt.xlabel("Profit range")
plt.ylabel("Number of months")
plt.show()
