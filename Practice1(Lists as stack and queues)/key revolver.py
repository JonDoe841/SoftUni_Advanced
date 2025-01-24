from collections import deque

# Input
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())

bullets_used = 0
while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]
    bullets_used += 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if bullets_used % gun_barrel_size == 0 and bullets:
        print("Reloading!")

if not locks:
    money_earned = intelligence_value - (bullets_used * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")