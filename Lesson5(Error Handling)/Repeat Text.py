txt = input()


try:
    num = int(input())
    print(txt * num)

except ValueError:
    print("Variable times must be an integer")