def load_data():
    data_file = open("data/" + "6.txt", "r")
    lines = data_file.readlines()
    fish = [int(s) for s in lines[0].split(",")]
    return fish


def process_fish(fish):
    if fish == 0:
        return 6
    else:
        return fish - 1


def progress_day(fishes):
    new_fish = []
    new_fish.extend([8 for i in range(sum(map(lambda x: x == 0, fishes)))])

    updated = list(map(process_fish, fishes))
    return updated + new_fish


fish_data = load_data()

print(f"There are intially {len(fish_data)} fish")


for day in range(256):
    fish_data = progress_day(fish_data)
    print(f"On day {day+1} there are {len(fish_data)} fish")
