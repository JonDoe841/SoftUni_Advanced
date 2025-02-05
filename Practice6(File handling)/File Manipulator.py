import os

while True:
    command = input().strip()
    if command == "End":
        break

    if command.startswith("Create-"):

        file_name = command.split("-", 1)[1]

        with open(file_name, 'w') as file:
            pass

    elif command.startswith("Add-"):

        parts = command.split("-", 2)
        file_name = parts[1]
        content = parts[2]

        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command.startswith("Replace-"):

        parts = command.split("-", 3)
        file_name = parts[1]
        old_string = parts[2]
        new_string = parts[3]

        if not os.path.exists(file_name):
            print("An error occurred")
        else:

            with open(file_name, 'r') as file:
                content = file.read()
            content = content.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(content)

    elif command.startswith("Delete-"):

        file_name = command.split("-", 1)[1]

        if not os.path.exists(file_name):
            print("An error occurred")
        else:

            os.remove(file_name)

    else:
        print("Invalid command")