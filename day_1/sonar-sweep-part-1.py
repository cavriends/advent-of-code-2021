import numpy as np

with open('input.txt') as f:
    file = []
    for line in f:
        file.append(int(line))

report = np.array(file)
diff = report[0:-1] - report[1:]
answer = len(diff[diff < 0])

print(answer) # 1713