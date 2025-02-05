from string import punctuation

with open("file.txt") as file:
    lines = file.readlines()


result = ""
for index in range(len(lines)):
    n_chars = 0
    n_punc = 0
    for char in lines[index]:
        if char in punctuation:
            n_punc += 1
        if char.isalpha():
            n_chars += 1


    result += f"Line {index+1}: {lines[index]} ({n_chars})({n_punc})\n"

with open("file.txt", "w") as file:
    file.write(result)