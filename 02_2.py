data_file = open("data/" + "2.txt", "r")
lines = data_file.readlines()

total = {"horizontal": 0, "depth": 0, "aim": 0}

for command in lines:
    action, amount = command.split()
    amount = int(amount)

    if action == "forward":
        total["horizontal"] += amount
        total["depth"] += total["aim"] * amount
    if action == "down":
        total["aim"] += amount
    if action == "up":
        total["aim"] -= amount
print(total)

print(total["horizontal"] * total["depth"])
