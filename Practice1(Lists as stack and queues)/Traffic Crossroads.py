from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
total_cars_passed = 0
crash = False

while True:
    command = input()
    if command == "END":
        break

    if command == "green":
        current_green_time = green_light_duration
        while cars and current_green_time > 0:
            car = cars.popleft()
            if current_green_time >= len(car):
                current_green_time -= len(car)
                total_cars_passed += 1
            else:
                remaining = len(car) - current_green_time
                if remaining <= free_window_duration:
                    total_cars_passed += 1
                    current_green_time = 0
                else:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[current_green_time + free_window_duration]}.")
                    crash = True
                    break
        if crash:
            break
    else:
        cars.append(command)

if not crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
