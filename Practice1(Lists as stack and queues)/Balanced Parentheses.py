expression= input()

opening_parentheses = "([{"
closing_parentheses = ")]}"
stack = []

for char in expression:
    if char in opening_parentheses:
        stack.append(char)
    elif char in closing_parentheses:
        if not stack:
            print("NO")
            break
        last_parenthesis = stack.pop()
        if opening_parentheses.index(last_parenthesis) != closing_parentheses.index(char):
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")
