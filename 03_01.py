data_file = open("data/" + "3.txt", "r")
lines = data_file.readlines()


def is_set(value, bit):
    return value & 1 << bit != 0


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


gamma = 0
epsilon = 0

for x in range(12):
    ones = 0
    zeroes = 0
    for line in lines:
        line = int(line, 2)
        value = is_set(line, x)
        if value == True:
            ones += 1
        else:
            zeroes += 1
    # print(f"Ones: {ones} Zeroes: {zeroes}")
    if ones > zeroes:
        gamma = set_bit(gamma, x)
        epsilon = clear_bit(epsilon, x)
    if zeroes > ones:
        gamma = clear_bit(gamma, x)
        epsilon = set_bit(epsilon, x)

print(f"Gamma: {gamma} Epsilon: {epsilon}")
print(f"Power Consumption: {gamma*epsilon}")
