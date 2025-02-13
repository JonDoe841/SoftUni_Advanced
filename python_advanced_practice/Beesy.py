n = int(input())
matrix = []
bee = []
energy = 15
collected_nectar = 0
one_time = True
for row in range(n):
    row_data = list(input().strip())
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == "B":
            bee = [row, col]
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
while True:
    directions = input().split()
    for direction in directions:
        if direction not in possible_moves:
            continue
        matrix[bee[0]][bee[1]] = "-"
        move = possible_moves[direction]
        row, col = int(bee[0] + move[0]), int(bee[1] + move[1])
        if row < 0:
            row = n - 1
        elif row >= n:
            row = 0
        if col < 0:
            col = n - 1
        elif col >= n:
            col = 0
        bee = [row, col]
        energy -= 1

        if matrix[row][col].isdigit():
            collected_nectar += int(matrix[row][col])
            matrix[row][col] = "-"
        if matrix[row][col] == "H":
            matrix[bee[0]][bee[1]] = "B"
            if collected_nectar < 30:
                print("Beesy did not manage to collect enough nectar.")
                [print(''.join(map(str, row))) for row in matrix]
                exit()
            elif collected_nectar >= 30:
                print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
                [print(''.join(map(str, row))) for row in matrix]
                exit()
        if energy <= 0:
            matrix[bee[0]][bee[1]] = "B"
            if collected_nectar < 30:
                print("This is the end! Beesy ran out of energy.")
                matrix[bee[0]][bee[1]] = "B"
                [print(''.join(map(str, row))) for row in matrix]
                exit()
            elif collected_nectar >= 30 and one_time:
                energy += (collected_nectar - 30)
                collected_nectar = 30
                one_time = False
                if energy <= 0:
                    print("This is the end! Beesy ran out of energy.")
                    matrix[bee[0]][bee[1]] = "B"
                    [print(''.join(map(str, row))) for row in matrix]
                    exit()
