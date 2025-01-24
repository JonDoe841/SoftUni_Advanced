first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])


for _ in range(int(input())):
    line = input().split()
    command = line[0] + " " + line[1]
    numbers = [int(x) for x in line[2:]]

    if command == "Add First":
        first_seq.update(numbers)
    elif command == "Add Second":
        second_seq.update(numbers)
    elif command == "Remove First":
        first_seq.difference_update(numbers)
    elif command == "Remove Second":
        second_seq.difference_update(numbers)
    elif command == "Check Subset":
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))

print(*sorted(first_seq), sep= ", ")
print(*sorted(second_seq), sep= ", ")












"""
string_one = set(input())
string_two = set(input())

#removes the empty el in the sets ask proff why does the set create that
string_one.remove(" ")
string_two.remove(" ")


num_commands = int(input())
for _ in range(num_commands):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            #this removes the first 2 el add first for example then adds it to the sets
            curr_command = command.pop(0)
            curr_command = command.pop(0)
            string_one.update(command)
        elif command[1] == "Second":
            curr_command = command.pop(0)
            curr_command = command.pop(0)
            string_two.update(command)
    elif command[0] == "Remove":
        if command[1] == "First":
            curr_command = command.pop(0)
            curr_command = command.pop(0)
            string_one.difference_update(command)
        elif command[1] == "Second":
            curr_command = command.pop(0)
            curr_command = command.pop(0)
            string_two.difference_update(command)
    elif command[0] == "Check":
        if string_one.issubset(string_two) or string_two.issubset(string_one):
            print("True")
        else:
            print("False")

set_to_list_one = sorted(list(string_one))
set_to_list_two = sorted(list(string_two))
print(', '.join(set_to_list_one))
print(', '.join(set_to_list_two))

#63/100 in judge
"""