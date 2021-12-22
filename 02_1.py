data_file = open("data/" + "2.txt", "r")
lines = data_file.readlines()


total = {"horizontal": 0, "depth": 0}

for command in lines:
    action, amount = command.split()
    amount = int(amount)

    if action == "forward":
        total["horizontal"] += amount
    if action == "down":
        total["depth"] += amount
    if action == "up":
        total["depth"] -= amount

print(total)

print(total["horizontal"] * total["depth"])
