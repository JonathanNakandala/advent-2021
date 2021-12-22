data_file = open("data/" + "1.txt", "r")
lines = data_file.readlines()
lines = list(map(int, lines))
print(len(lines))

increased = 0
decreased = 0
equal = 0

for index, val in enumerate(lines):
    if index == 0:
        continue
    if lines[index] > lines[index - 1]:
        increased += 1
    elif lines[index - 1] > lines[index]:
        decreased += 1
    elif lines[index - 1] == lines[index]:
        equal += 1

print(f"Increased: {increased} Decreased: {decreased} Equal: {equal}")
