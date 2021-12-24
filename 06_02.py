def load_data():
    data_file = open("data/" + "6.txt", "r")
    lines = data_file.readlines()
    fish = [int(s) for s in lines[0].split(",")]
    return fish


def convert_initial(data):
    buckets = [0] * 9
    for fish in data:
        buckets[fish] += 1
    return buckets


def progress_day(fishes):
    new_fishes = fishes[:]

    new_fishes[0] = fishes[1]
    new_fishes[1] = fishes[2]
    new_fishes[2] = fishes[3]
    new_fishes[3] = fishes[4]
    new_fishes[4] = fishes[5]
    new_fishes[5] = fishes[6]
    new_fishes[6] = fishes[7]
    new_fishes[7] = fishes[8]

    new_fishes[6] += fishes[0]
    new_fishes[8] = fishes[0]

    # print(new_fishes)
    return new_fishes


fish_data = load_data()


buckets = convert_initial(fish_data)

print(f"There are intially {sum(buckets)} fish")
print(buckets)


for day in range(256):
    buckets = progress_day(buckets)
    print(f"On day {day+1} there are {sum(buckets)} fish")
