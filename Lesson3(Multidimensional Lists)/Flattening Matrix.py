rows_count = int(input())

matrix = []
for _ in range(rows_count):
    rows_data = [int(el) for el in input().split(", ")]
    matrix.append(rows_data)

result = []


for row in matrix:
    for el in row:
        result.append(el)

print(result)


