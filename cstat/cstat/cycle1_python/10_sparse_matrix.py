rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
count = int(input("Enter number of non-zero elements: "))
sparse = {}
for _ in range(count):
    i = int(input("Row index: "))
    j = int(input("Column index: "))
    v = int(input("Value: "))
    sparse[(i, j)] = v
print("Sparse representation:", sparse)
print("Matrix:")
for i in range(rows):
    print([sparse.get((i, j), 0) for j in range(cols)])
