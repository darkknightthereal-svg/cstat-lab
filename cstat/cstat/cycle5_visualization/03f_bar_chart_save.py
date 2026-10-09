import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
plt.bar(df["month_number"], df["bathingsoap"], color="green")
plt.title("Bathing Soap Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales units")
plt.xticks(df["month_number"])
plt.savefig("bathingsoap_sales.png")
print("Figure saved as bathingsoap_sales.png")
plt.show()
