fruits = ("apple", "banana", "mango", "orange", "grapes", "pineapple")
name = input("Enter a fruit to search: ").strip().lower()
if name in fruits:
    print(name, "found at position", fruits.index(name) + 1)
else:
    print(name, "not found")
