with open('input.txt') as f:
    file = []
    for line in f:
        file.append(line.split())

horizontal_position = 0
depth = 0
steering_input = list(file)

for action in steering_input:
    position = action[0]
    distance = int(action[1])

    if position == "forward":
        horizontal_position += distance
    elif position == "up":
        depth -= distance
    else:
        depth += distance

answer = depth*horizontal_position

print(answer) # 2117664