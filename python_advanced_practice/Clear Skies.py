n = int(input())
matrix = []
plane = [0,0]
armor = 300
enemy = 0
possible_moves = {"up": (-1, 0), "down": (1,0), "left": (0,-1),"right": (0,1)}
end = False
for row in range(n):
    matrix.append(list(input().strip()))
    for col in range(n):
        if matrix[row][col] == "J":
            plane = [row, col]
        if matrix[row][col] == "E":
            enemy += 1

while True:
    commands = input().split()
    for command in commands:
        if command not in possible_moves:
            continue
        move = possible_moves[command]
        row, col = int(plane[0] + move[0]), int(plane[1] + move[1])
        matrix[plane[0]][plane[1]] = "-"
        plane = [row, col]
        if matrix[row][col] == "R":
            armor = 300
            matrix[row][col] = "-"
        if matrix[row][col] == "E":
            matrix[row][col] = "-"
            enemy -= 1
            if enemy == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                end = True
                break
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates {plane}!")
                end = True
                break
    if end:
        break



matrix[plane[0]][plane[1]] = "J"
[print(''.join(map(str, row))) for row in matrix]