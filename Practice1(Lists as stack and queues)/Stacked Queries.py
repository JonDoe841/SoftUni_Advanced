"""my_stack = []
n = int(input())

for _ in range(n):
    query = input().split()
    if query[0] == "1":
        my_stack.append(int(query[1]))
    elif my_stack:
        if query[0] == "2":
            my_stack.pop()
        elif query[0] == "3":
            print(max(my_stack))
        elif query[0] == "4":
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end="")
    if my_stack:
        print(", ", end="")
"""


my_stack = []
n = int(input())

functions = {
    "1": lambda x: my_stack.append(int(x)),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: print(max(my_stack)) if my_stack else None,
    "4": lambda: print(min(my_stack)) if my_stack else None
}

for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:])


