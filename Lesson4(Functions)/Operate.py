def operate(operators, *args):
    def sum_nums():
        return sum(args)
    def sub_nums():
        result = 0
        for el in args:
            result -= el
        return result
    def mul_nums():
        result = 1
        for el in args:
            result *= el
        return result

    def div_nums():
        result = 1
        for el in args:
            result /= el
        return result

    if operators == "+":
        return sum_nums()
    elif operators == "-":
        return sub_nums()
    elif operators == "*":
        return mul_nums()
    else:
        return div_nums()

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
