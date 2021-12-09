with open("input.txt") as f:
    file_input = []
    file_output = []
    for line in f.readlines():
        txt_input, txt_output = line.replace("\n", "").split("|")
        file_input.append(txt_input.split(" "))
        file_output.append(txt_output.split(" "))

print(file_output)

mapping = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

length = list(map(len, mapping))

print(length)

occurence = 0

for i in file_output:
    length_per_string = list(map(len, i))
    for number in [length[1], length[4], length[7], length[8]]:
        if length_per_string.count(number) >= 1:
            occurence += length_per_string.count(number)

print(occurence) # 530
