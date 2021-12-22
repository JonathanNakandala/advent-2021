data_file = open("data/" + "1.txt", "r")
lines = data_file.readlines()
lines = list(map(int, lines))
print(len(lines))

increased = 0
previous_measurement = None
new_measurement = None

for index, val in enumerate(lines):
    if index in (0, 1):
        continue
    if previous_measurement == None:
        previous_measurement = lines[index] + lines[index - 1] + lines[index - 2]
    else:
        new_measurement = lines[index] + lines[index - 1] + lines[index - 2]
        if new_measurement > previous_measurement:
            increased = increased + 1
        previous_measurement = new_measurement

print(f"Increased: {increased}")
