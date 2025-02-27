n = int(input())
pacman = []
matrix = []
health = 100
stars = 0
immunity = False
won = False
final_break = False
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            pacman = [row, col]
        if matrix[row][col] == "*":
            stars += 1
while True:
    directions = input().split()
    for direction in directions:
        if direction == "end":
            final_break = True
            break
        matrix[pacman[0]][pacman[1]] = "-"
        move = possible_moves[direction]
        row, col = pacman[0] + move[0], pacman[1] + move[1]
        if row < 0:
            row = n - 1
        elif row >= n:
            row = 0
        if col < 0:
            col = n - 1
        elif col >= n:
            col = 0
        pacman = [row, col]
        if matrix[row][col] == "F":
            matrix[row][col] = "-"
            immunity = True
        if matrix[row][col] == "G":
            if not immunity:
                matrix[row][col] = "-"
                health -= 50
                if health <= 0:
                    health = 0
                    final_break = True
                    break
            else:
                immunity = False
        if matrix[row][col] == "*":
            matrix[row][col] = "-"
            stars -= 1
            if stars == 0:
                won = True
                final_break = True
                break
    if final_break:
        break
if won:
    print("Pacman wins! All the stars are collected.")
elif health == 0:
    print(f"Game over! Pacman last coordinates [{pacman[0]},{pacman[1]}]")
else:
    print("Pacman failed to collect all the stars.")
print(f"Health: {health}")
if stars:
    print(f"Uncollected stars: {stars}")
matrix[pacman[0]][pacman[1]] = "P"
[print(''.join(map(str, row))) for row in matrix]