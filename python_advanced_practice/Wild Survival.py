from collections import deque

bee_num = input().split(" ")
bee_eaters = deque(input().split(" "))
while bee_eaters or bee_num:
    if not bee_eaters or not bee_num:
        break
    curr_bees = int(bee_num[0])
    curr_bee_eaters = int(bee_eaters.pop())
    while True:
        curr_bees -= 7
        if curr_bees == 0:
            curr_bee_eaters -= 1
            break
        elif curr_bees < 0:
            break
        curr_bee_eaters -=1
        if curr_bee_eaters <= 0:
            break
    if curr_bees <= 0 :
        bee_num.pop(0)

    else:
        bee_num.pop(0)
        bee_num.append(str(curr_bees))
    if curr_bee_eaters <= 0 :
        pass
    else:
        bee_eaters.append(str(curr_bee_eaters))


print("The final battle is over!")

if not bee_eaters and not bee_num:
    print("But no one made it out alive!")
elif bee_num:
    print(f"Bee groups left: {', '.join(bee_num)}")
else:
    print(f"Bee-eater groups left: {', '.join(bee_eaters)}")