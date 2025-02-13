n = int(input())
curr_pos = [0, 0]
matrix = []

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "P":
            curr_pos = [r, c]
            matrix[r][c] = "."
            break

stars = 2
collected_stars = 0
moves = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

while 10 > stars > 0:

    command = input().split()

    move = moves[command]
    new_r = curr_pos[0] + move[0]
    new_c = curr_pos[1] + move[1]

    if 0 <= new_r < n and 0 <= new_c < n:
        curr_pos = [0, 0]

        if matrix[new_r][new_c] == "*":
            stars += 1
            matrix[new_r][new_c] = "."

        elif matrix[new_r][new_c] == "#":
            stars -= 1

        elif matrix[new_r][new_c] == ".":
            matrix[new_r][new_c] = [new_r - 1][new_c - 1]

    curr_pos = [new_r, new_c]

if stars >= 10:
    print(f"You won! You have collected {stars} stars.")
elif stars <= 0:
    print("Game over! You are out of any stars.")

print(f"Your final position is {curr_pos}")

[print(*row) for row in matrix]