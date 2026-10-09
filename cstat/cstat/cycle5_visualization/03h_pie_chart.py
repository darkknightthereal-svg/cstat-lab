import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
products = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
totals = [df[p].sum() for p in products]
plt.pie(totals, labels=products, autopct="%1.1f%%", startangle=90)
plt.title("Sales Data of Last Year")
plt.show()
