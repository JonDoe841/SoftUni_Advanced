from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

starting_position = 0
stops = 0

while stops < pumps_num:
    fuel = 0
    for i in range(pumps_num):
        fuel += pumps[i][0]
        distance = pumps[i][1]
        if fuel < distance:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(starting_position)

