def load_data():
    data_file = open("data/" + "7.txt", "r")
    lines = data_file.readlines()
    crabs = [int(s) for s in lines[0].split(",")]
    return crabs


def check_fuel(position):
    fuel_usage = 0
    for crab in crab_data:
        fuel_usage += abs(position - crab)
    return fuel_usage
    


crab_data = load_data()

crab_data.sort()

max_value = max(crab_data)
min_value = min(crab_data)

print(f'There are {len(crab_data)}. The Highest: {max_value} The Lowest: {min_value}')

best_position = None
best_fuel = None
for i in range(min_value, max_value + 1):
    calculated_fuel = check_fuel(i)
    #print(calculated_fuel)
    if best_fuel == None:
        best_position = i
        best_fuel = calculated_fuel
    else:
        if best_fuel > calculated_fuel:
            best_position = i
            best_fuel = calculated_fuel

print(f'The Best Position is {best_position} with {best_fuel}')
    