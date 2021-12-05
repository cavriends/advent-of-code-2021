import numpy as np

with open('input.txt') as f:
    file = []
    for line in f:
        file.append(line.split())

file = [item for sublist in file for item in sublist]

number_of_bits = len(file[0])
number_of_numbers = len(file)
binary_matrix = np.empty((number_of_numbers, number_of_bits), dtype=int)

for index, number in enumerate(file):
    values = list(number)
    binary_matrix[index] = values

def most_occuring(binary_matrix):

    occuring_pattern = (binary_matrix.sum(0) > len(binary_matrix)//2).astype(int)
    if len(binary_matrix) % 2 == 0:
        equal_pattern = (binary_matrix.sum(0) == len(binary_matrix)//2).astype(int)
    else:
        equal_pattern = np.zeros(binary_matrix.shape[1], dtype=int)

    return occuring_pattern, equal_pattern

def binary_to_decimal(binary):

    decimal = 0
    for idx, element in enumerate(binary):
        decimal += element*pow(2, abs(len(binary)-1-idx))

    return decimal

temporary_matrix = binary_matrix

def get_rating(binary_matrix, rating=0):
    # 1: oxygen generator, 0: CO2 scrubber
    temporary_matrix = binary_matrix
    number_of_bits = binary_matrix.shape[0]

    for i in range(number_of_bits):

        if temporary_matrix.shape[0] != 1:
            occuring_pattern, equal_pattern = most_occuring(temporary_matrix)
            occuring_pattern = abs(occuring_pattern - (1-rating))
            if equal_pattern[i] == 1:
                temporary_matrix = temporary_matrix[temporary_matrix[:,i] == rating]
            else:
                temporary_matrix = temporary_matrix[temporary_matrix[:,i] == occuring_pattern[i]]

    return binary_to_decimal(temporary_matrix[0])

oxygen_rating = get_rating(binary_matrix, 1)
co2_scrubber_rating = get_rating(binary_matrix, 0)

life_support_rating = oxygen_rating*co2_scrubber_rating

print(life_support_rating) # 5410338