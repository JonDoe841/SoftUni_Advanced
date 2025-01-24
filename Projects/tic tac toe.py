list1 = [""]

symbol = ""
matrix = []
#THIS MAKES THE GRID
for i in range(9):
    matrix.append(list1)

points_for_O = int()
point_for_X = int()
#Win conditions
win_patterns = [
    [2, 4, 6],  # Diagonal
    [0, 4, 8],  # D
    [0, 1, 2],  # Horizontal
    [3, 4, 5],  # H
    [6, 7, 8],  # H
    [0, 3, 6],  # Vertical
    [1, 4, 7],  # V
    [2, 5, 8],  # V
]

player_turn = 0

print("HELLO TO TIC TAC TOE PLAYER ONE IS X, PLAYER TWO IS O, GOOD LUCK!!!")
print("to play the input should be just the number from 0-8 on the grid and to end type END")
print(f" {matrix[0:3]}\n {matrix[3:6]}\n {matrix[6:9]}")
while symbol != "END":
    if player_turn % 2 == 0:
        symbol = "X"
        place = input("Player 1:")
        if place == "END":
            exit()
        matrix[int(place)] = symbol
        print(f" {matrix[0:3]}\n {matrix[3:6]}\n {matrix[6:9]}")
        player_turn += 1
    elif player_turn % 2 != 0:
        symbol = "O"
        place = input("Player 2:")
        if place == "END":
            exit()
        matrix[int(place)] = symbol
        print(f" {matrix[0:3]}\n {matrix[3:6]}\n {matrix[6:9]}")
        player_turn += 1



    if any(matrix[a] == "X" and matrix[b] == "X" and matrix[c] == "X" for a, b, c in win_patterns):
        print("Player 1 WON!!!")
        point_for_X += 1
        # in case of a win it clears and remakes the grid so the game can continue
        matrix.clear()
        for i in range(9):
            matrix.append(list1)
        print(f" {matrix[0:3]}\n {matrix[3:6]}\n {matrix[6:9]}")
        continue
    elif any(matrix[a] == "O" and matrix[b] == "O" and matrix[c] == "O" for a, b, c in win_patterns):
        print("Player 2 WON!!!")
        points_for_O += 1
        matrix.clear()
        for i in range(9):
            matrix.append(list1)
        print(f" {matrix[0:3]}\n {matrix[3:6]}\n {matrix[6:9]}")
        continue

print(f"Player 1 has {point_for_X} points!")
print(f"Player 2 has {points_for_O} points!")

