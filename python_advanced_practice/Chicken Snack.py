from collections import deque

money = deque(map(int, input().split()))
price = deque(map(int, input().split()))
food = 0
while True:
    if not money or not price:
        break
    curr_money = money.pop()
    curr_price = price[0]
    if curr_money == curr_price:
        food += 1
        price.popleft()
    elif curr_money > curr_price:
        food += 1
        if not money:
            break
        money[-1] += abs(curr_money - curr_price)
        price.popleft()
    else:
        price.popleft()

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
elif food != 0:
    if food == 1:
        print(f"Henry ate: {food} food.")
    else:
        print(f"Henry ate: {food} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")