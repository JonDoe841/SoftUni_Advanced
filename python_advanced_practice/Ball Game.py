from collections import deque
strength = deque(input().split(" "))
accuracy = input().split(" ")
strike = 0
while len(accuracy) > 0 and len(strength) > 0 :
    math = int(strength[-1]) + int(accuracy[0])
    if math == 100:
        strike += 1
        strength.pop()
        accuracy.pop(0)
    if math < 100:
        if int(strength[-1]) < int(accuracy[0]):
            strength.pop()
        elif int(strength[-1]) > int(accuracy[0]):
            accuracy.pop(0)
        else:
            strength.pop()
            strength.append(str(math))
            accuracy.pop(0)
    if math > 100:
        strength[-1] = int(strength[-1]) - 10
        curr_acc = accuracy.pop(0)
        accuracy.append(curr_acc)


if strike == 3:
    print("Paul scored a hat-trick!")
if strike == 0:
    print("Paul failed to score a single goal.")
if strike > 3:
    print("Paul performed remarkably well!")
if 0 < strike < 3:
    print("Paul failed to make a hat-trick.")

if strike > 0:
    print(f"Goals scored: {strike}")

if len(strength) > 0:
    print(f"Strength values left: {', '.join(strength)}")
if len(accuracy) > 0:
    print(f"Accuracy values left: {', '.join(accuracy)}")