import numpy as np

with open("input.txt") as f:
    initial_state = list(map(int, f.read().split(",")))

input = np.array(initial_state)
state_array = np.zeros(9, dtype=int)

for i in range(9):
    state_array[i] = len(input[input == i])

days = 256

for day in range(days):

    fish_born = state_array[0]

    for i in range(9):

        if i != 0:
            state_array[i-1] = state_array[i]

    state_array[8] = fish_born
    state_array[6] += fish_born

answer = state_array.sum()

print(answer) # 1613415325809