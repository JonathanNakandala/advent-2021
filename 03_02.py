data_file = open("data/" + "3.txt", "r")
lines = data_file.readlines()


def is_set(value, bit):
    return value & 1 << bit != 0


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def convert_binary(lines):
    new_lines = []
    for line in lines:
        new_lines.append(int(line, 2))

    return new_lines


def filter_values(data, position):
    lines_true = []
    lines_false = []

    for datum in data:
        value = is_set(datum, position)
        if value == True:
            lines_true.append(datum)
        else:
            lines_false.append(datum)

    response = {
        "True": {"data": lines_true, "total": len(lines_true)},
        "False": {"data": lines_false, "total": len(lines_false)},
    }
    return response


def find_commons(data):
    most_common = None
    least_common = None
    if data["True"]["total"] > data["False"]["total"]:
        most_common = True
        least_common = False
    if data["False"]["total"] > data["True"]["total"]:
        most_common = False
        least_common = True
    if data["False"]["total"] == data["True"]["total"]:
        most_common = True
        least_common = False

    return most_common, least_common


lines = convert_binary(lines)
oxygen_set = None
co2_set = None
oxygen_value = None
co2_value = None
for x in reversed(range(12)):
    if not oxygen_set and not co2_set:
        result = filter_values(lines, x)
        most_common, least_common = find_commons(result)

        oxygen_set = result[str(most_common)]["data"]
        co2_set = result[str(least_common)]["data"]
    else:
        new_oxygen_set = filter_values(oxygen_set, x)
        most_common, _ = find_commons(new_oxygen_set)
        if new_oxygen_set[str(most_common)]["total"] == 1:
            oxygen_value = new_oxygen_set[str(most_common)]["data"][0]
            print(f"Oxygen Set value is: {oxygen_value}")
        oxygen_set = new_oxygen_set[str(most_common)]["data"]

        new_co2_set = filter_values(co2_set, x)
        _, least_common = find_commons(new_co2_set)
        if new_co2_set[str(least_common)]["total"] == 1:
            co2_value = new_co2_set[str(least_common)]["data"][0]
            print(f"CO2 Set value is: {co2_value}")
        co2_set = new_co2_set[str(least_common)]["data"]

print(f"Life Support Rating: {oxygen_value*co2_value}")
