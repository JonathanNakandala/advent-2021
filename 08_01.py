

ZERO = 6
ONE = 2
TWO = 5
THREE = 5
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 3
EIGHT = 7
NINE = 6



def load_data():
    data_file = open("data/" + "8.txt", "r")
    lines = data_file.readlines()
    return lines

def process_data(lines):
    new_lines = []
    for line in lines:
        new_lines.append((line.strip().split("|")))
    #print(new_lines)
    
    processed_data = []
    for group in new_lines:
        input = group[0].strip().split(" ")
        output = group[1].strip().split(" ")
        #print(output)
        data = {
            "input": input,
            "output": output
        }
        processed_data.append(data)
    return processed_data

def count_uniques(lines):
    uniques = 0
    #print(lines)
    for line in lines:
        print(line)
        for value in line['output']:
            if len(value) in [ONE, FOUR, SEVEN, EIGHT]:
                uniques += 1
    return uniques

data = load_data()

output = process_data(data)
result = count_uniques(output)
print (result)