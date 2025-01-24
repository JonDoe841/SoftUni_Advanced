n = int(input())

ship = []
space_matrix = []
planet_B = []
fuel = 100

for row in range(n):
    space_matrix.append(input().split(" "))
    for col in range(n):
        if space_matrix[row][col] == "S":
            ship = [row, col]
        elif space_matrix[row][col] == "P":
            planet_B = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
win = True

while win:
    directions = input().split()

    for direction in directions:
        if direction not in possible_moves:
            continue

        move = possible_moves[direction]
        row, col = ship[0] + move[0], ship[1] + move[1]

        # Check if the new position is out of bounds
        if not (0 <= row < n and 0 <= col < n):
            print("Mission failed! The spaceship was lost in space.")
            space_matrix[ship[0]][ship[1]] = "S"
            [print(*row) for row in space_matrix]
            exit()

        fuel -= 5
        if space_matrix[row][col] == "R":
            fuel = min(fuel + 10, 100)

        elif space_matrix[row][col] == "M":
            fuel -= 5
            space_matrix[row][col] = "."

        if space_matrix[ship[0]][ship[1]] != "R":
            space_matrix[ship[0]][ship[1]] = "."
        ship = [row, col]
        if space_matrix[row][col] == "P":
            print(f"Mission accomplished! The spaceship reached Planet B with {fuel} resources left.")
            [print(*row) for row in space_matrix]
            win = False
            exit()
        if fuel <= 0:
            print("Mission failed! The spaceship was stranded in space.")
            space_matrix[ship[0]][ship[1]] = "S"
            [print(*row) for row in space_matrix]
            exit()


