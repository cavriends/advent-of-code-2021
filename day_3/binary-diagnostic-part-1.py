import numpy as np

with open('input.txt') as f:
    file = []
    for line in f:
        file.append(line.split())

file = [item for sublist in file for item in sublist]

binary_matrix = np.empty((len(file), len(file[0])), dtype=int)

for index, number in enumerate(file):
    values = list(number)
    binary_matrix[index] = values

gamma_rate_binary = (binary_matrix.sum(0) > len(file)//2).astype(int)
epsilon_rate_binary = abs(gamma_rate_binary - 1)

def binary_to_decimal(binary):

    decimal = 0
    for idx, element in enumerate(binary):
        decimal += element*pow(2, abs(len(binary)-1-idx))

    return decimal

gamma_rate = binary_to_decimal(gamma_rate_binary)
epsilon_rate = binary_to_decimal(epsilon_rate_binary)

power_consumption = gamma_rate*epsilon_rate

print(power_consumption) # 3429254