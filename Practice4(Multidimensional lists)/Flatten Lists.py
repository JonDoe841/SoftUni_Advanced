str = input().split("|")

matrix = []


for i in range(len(str) -1, -1, -1):
    row = str[i].split()
    if row:
        matrix.append(row)


for row in matrix:
    print(*row, end=" ")