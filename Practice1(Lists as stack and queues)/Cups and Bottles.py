from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    curr_cup = cups[0]
    while curr_cup > 0:
        curr_bottle = bottles.pop()
        curr_cup -= curr_bottle
    wasted_water -= curr_cup
    cups.popleft()

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")

