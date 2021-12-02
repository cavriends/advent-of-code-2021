with open('input.txt') as f:
    steering_input = []
    for line in f:
        steering_input.append(line.split())

horizontal_position = 0
depth = 0

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