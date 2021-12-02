import pandas as pd

with open('input.txt') as f:
    file = []
    for line in f:
        file.append(int(line))

report = pd.Series(file)
report_rs = report.rolling(3).sum().dropna().to_numpy()
diff = report_rs[0:-1] - report_rs[1:]
answer = len(diff[diff < 0])

print(answer) #1734