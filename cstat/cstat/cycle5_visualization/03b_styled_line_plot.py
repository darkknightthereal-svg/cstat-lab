import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
plt.plot(df["month_number"], df["total_profit"], label="Profit data of last year",
         color="r", marker="o", markerfacecolor="k", linestyle="--", linewidth=3)
plt.title("Company Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Profit in dollars")
plt.xticks(df["month_number"])
plt.legend(loc="lower right")
plt.show()
