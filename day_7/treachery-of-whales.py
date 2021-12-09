import numpy as np

with open("input.txt") as f:
    file = list(map(int, f.read().split(",")))

crab_position = np.array(file)

fuel = np.zeros(np.max(crab_position)+1, dtype=int)

positions = np.arange(0, np.max(crab_position)+1)

for position in positions:
    for crab in crab_position:
        position_change_inclusive = abs(crab - position) + 1
        fuel[position] += position_change_inclusive*(position_change_inclusive-1)/2

print(np.min(fuel))
