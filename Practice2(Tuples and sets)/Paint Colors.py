from collections import deque


colors_strings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"]
}
collected_colors = []

while colors_strings:
    first_str = colors_strings.popleft()
    last_str = colors_strings.pop() if colors_strings else ""
    for color in (first_str + last_str, last_str + first_str):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_str) > 1:
            colors_strings.insert(len(colors_strings) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_strings.insert(len(colors_strings) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)


