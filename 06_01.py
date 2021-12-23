def load_data():
    data_file = open("data/" + "6.txt", "r")
    lines = data_file.readlines()
    fish = [int(s) for s in lines[0].split(",")]
    return fish


def progress_day(fishes):
    new_fish = []
    for idx, fish in enumerate(fishes):
        if fish == 0:
            new_fish.append(8)
            fishes[idx] = 6
        else:
            fishes[idx] -= 1
    return fishes + new_fish


fish_data = load_data()

print(f"There are intially {len(fish_data)} fish")


for day in range(256):
    fish_data = progress_day(fish_data)
    print(f"On day {day+1} there are {len(fish_data)} fish")
