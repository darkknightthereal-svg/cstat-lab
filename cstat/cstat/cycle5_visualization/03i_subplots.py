import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(df["month_number"], df["bathingsoap"], color="k", marker="o")
ax1.set_title("Sales data of a Bathing Soap")
ax1.set_ylabel("Sales units")
ax2.plot(df["month_number"], df["facewash"], color="r", marker="o")
ax2.set_title("Sales data of a Face Wash")
ax2.set_xlabel("Month Number")
ax2.set_ylabel("Sales units")
plt.xticks(df["month_number"])
plt.tight_layout()
plt.show()
