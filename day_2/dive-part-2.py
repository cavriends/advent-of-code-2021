with open('input.txt') as f:
    file = []
    for line in f:
        file.append(line.split())

horizontal_position = 0
depth = 0
aim = 0
steering_input = list(file)

for action in steering_input:
    position = action[0]
    value = int(action[1])

    if position == "forward":
        horizontal_position += value
        depth += aim*value
    elif position == "up":
        aim -= value
    else:
        aim += value

answer = depth*horizontal_position

print(answer) # 2073416724