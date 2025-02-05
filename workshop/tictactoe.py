p1 = input()
p2 = input()

while True:
    symbol = input()
    if symbol not in ["X", "x", "O", "o"]:
        symbol = input()
    else:
        break

p1_sym = symbol.upper()
p2_sym = "O" if p1_sym == "X" else "x"

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(f"|  {'  |  '.join([str(el) for el in row])}  |")

print(f"{p1} starts first")
while True:
    try:
        position = int(input())
    except ValueError:
        print("Out of playing ground")