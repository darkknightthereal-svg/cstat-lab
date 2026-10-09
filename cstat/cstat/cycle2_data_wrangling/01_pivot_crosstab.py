import pandas as pd

data = pd.DataFrame({
    "Region": ["North", "South", "North", "East", "South", "East", "North", "South"],
    "Product": ["A", "B", "B", "A", "A", "B", "A", "B"],
    "Quarter": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3", "Q4", "Q4"],
    "Sales": [200, 150, 300, 250, 400, 180, 220, 310],
    "Units": [20, 15, 30, 25, 40, 18, 22, 31],
})
print("Data:")
print(data)

pivot = pd.pivot_table(data, values="Sales", index="Region", columns="Product", aggfunc="sum", fill_value=0)
print("\nPivot table:")
print(pivot)

multi = pd.pivot_table(data, values=["Sales", "Units"], index="Region", aggfunc=["sum", "mean"])
print("\nPivot table with multiple values:")
print(multi)

cross = pd.crosstab(data["Region"], data["Product"])
print("\nCross tabulation:")
print(cross)

cross_total = pd.crosstab(data["Region"], data["Product"], margins=True)
print("\nCross tabulation with totals:")
print(cross_total)
