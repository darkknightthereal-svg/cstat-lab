import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
for p in products:
    plt.plot(df["month_number"], df[p], marker="o", label=p)
plt.title("Sales Data of All Products")
plt.xlabel("Month Number")
plt.ylabel("Sales units")
plt.xticks(df["month_number"])
plt.legend(loc="upper left")
plt.show()
