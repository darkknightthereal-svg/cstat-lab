import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
plt.bar(df["month_number"], df["facecream"], label="Face cream", width=0.25)
plt.bar(df["month_number"] + 0.25, df["facewash"], label="Face wash", width=0.25)
plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales units")
plt.xticks(df["month_number"])
plt.legend(loc="upper left")
plt.show()
