rows = 5
for i in range(rows):
    for j in range(i + 1):
        print((i + j) % 2, end=" ")
    print()
