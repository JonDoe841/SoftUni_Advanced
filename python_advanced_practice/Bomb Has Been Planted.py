data = input().split(", ")
rows, cols = int(data[0]), int(data[1])
#matrix = []
bomb = []
counter_terrorist = []
TIME = 16
matrix = [list(input()) for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "B":
            bomb = [row, col]
        if matrix[row][col] == "C":
            counter_terrorist = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), "defuse": (0, 0)}
lose = True
while lose:
    if TIME == 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {TIME} second/s.")
        # matrix[bomb[0]][bomb[1]] = "X"
        [print(''.join(map(str, row))) for row in matrix]
        lose = False
        break
    directions = input().split()
    for direction in directions:
        if direction not in possible_moves:
            continue

        move = possible_moves[direction]
        row, col = int(counter_terrorist[0] + move[0]), int(counter_terrorist[1] + move[1])
        #counter_terrorist = [row, col]
        if not (0 <= row < rows and 0 <= col < cols):
            TIME -= 1
            continue
        else:
            counter_terrorist = [row, col]
        if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == "T":
            print("Terrorists win!")
            matrix[row][col] = "*"
            [print(''.join(map(str, row))) for row in matrix]
            lose = False
            break

        if direction == "defuse":
            if bomb == counter_terrorist:
                TIME -= 4
                if TIME >= 0:
                    print("Counter-terrorist wins!")
                    print(f"Bomb has been defused: {TIME} second/s remaining.")
                    matrix[row][col] = "D"
                else:
                    print("Terrorists win!")
                    print("Bomb was not defused successfully!")
                    print(f"Time needed: {abs(TIME)} second/s.")
                    matrix[bomb[0]][bomb[1]] = "X"
                [print(''.join(map(str, row))) for row in matrix]
                lose = False
                break
            else:
                TIME -= 2
        else:
            TIME -= 1

