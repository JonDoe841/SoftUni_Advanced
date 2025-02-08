n = int(input())
player = []
matrix = []

for row in range(n):
    matrix.append(input().split(" "))
    for col in range(n):
        if matrix[row][col] == "P":
            player = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
won = True
stars = 2
while True:
    directions = input().split()
    for direction in directions:
        matrix[player[0]][player[1]] = "."
        move = possible_moves[direction]
        row, col = player[0] + move[0], player[1] + move[1]

        if not (0 <= row < n and 0 <= col < n):
            row, col = 0, 0
        if matrix[row][col] == "#":
            stars -= 1
            if stars == 0:
                print(f"Game over! You are out of any stars.")
                print(f"Your final position is {player}")
                matrix[player[0]][player[1]] = "P"
                [print(*row) for row in matrix]

                exit()
            continue
        player = [row , col]

        if matrix[player[0]][player[1]] == "*":
            matrix[player[0]][player[1]] = "."
            stars +=1

        if stars == 10:
            matrix[player[0]][player[1]] = "P"
            print(f"You won! You have collected {stars} stars.")
            print(f"Your final position is {player}")
            [print(*row) for row in matrix]
            exit()

        matrix[player[0]][player[1]] = "P"

#matrix[player[0]][player[1]] = "P"
#[print(*row) for row in matrix]