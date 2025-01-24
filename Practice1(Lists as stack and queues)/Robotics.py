"""from collections import deque
from datetime import datetime, timedelta

robots_input = input()
start_time_input = input()

robots = []
for robot in robots_input.split(";"):
    name, process_time = robot.split("-")
    robots.append((name, int(process_time), None))

current_time = datetime.strptime(start_time_input, "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    current_time += timedelta(seconds=1)
    product = products.popleft()

    for i in range(len(robots)):
        name, process_time, busy_until = robots[i]
        if busy_until is None or busy_until <= current_time:
            robots[i] = (name, process_time, current_time + timedelta(seconds=process_time))
            print(f"{name} - {product} [{current_time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(product)
"""
from collections import deque


robots_data = input().split(";")
robots_list = []
for robot in robots_data:
    robot_name, process_time = robot.split("-")
    robots_list.append({"name": robot_name, "process_time": int(process_time), "busy_until": 0})

hours, minutes, seconds, = [int(x) for x in input().split(":")]
start_time_seconds = hours * 3600 + minutes * 60 + seconds

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    curr_product = products.popleft()
    start_time_seconds += 1
    is_taken = False

    for robot in robots_list:
        if robot["busy_until"] <= start_time_seconds:
            robot["busy_until"] = start_time_seconds + robot["process_time"]
            h = start_time_seconds // 3600
            m = (start_time_seconds % 3600) // 60
            s = (start_time_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {curr_product} [{h:02d}:{m:02d}:{s:02}]")
            is_taken = True
            break

    if not is_taken:
        products.append(curr_product)


