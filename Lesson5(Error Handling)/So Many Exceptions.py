number_list = [int(el) for el in input().split(", ")]
result = 1

for i in range(len(number_list)):
    number = number_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number


print(result)