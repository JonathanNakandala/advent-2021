import numpy as np


def load_data():
    with open("data/" + "9.txt") as f:
        lines = [line.strip() for line in f]
    return lines

def generate_array(data, heightmap):
    for y_index, row in enumerate(data):
        for x_index, column in enumerate(row):
            #print(column)
            heightmap[y_index][x_index] = int(column)
    return heightmap


def find_lowpoints(heightmap):
    lowest_points = []
    for y_index, row in enumerate(heightmap):
        for x_index, column in enumerate(row):
            lowest_point = True
            try: 
                above = heightmap[y_index][x_index - 1]
                if column > above:
                    lowest_point = False

            except:
                above = None
            try:
                below = heightmap[y_index][x_index + 1]
                if column > below:
                    lowest_point = False
            except:
                below = None
            try:
                left = heightmap[y_index - 1][x_index]
                if column > left:
                    lowest_point = False
            except:
                left = None
            try:
                right = heightmap[y_index + 1][x_index]
                if column > right:
                    lowest_point = False
            except:
                right = None
            
            if lowest_point == True:
                lowest_points.append((y_index, x_index))

    return lowest_points

def calculate_risk_level(heightmap, points):
    risk_total = 0
    for point in points:
        risk_total += heightmap[point[0]][point[1]]
        risk_total += 1
        
    return risk_total
            #print()

data = load_data()

x_length = len(data[0])
y_length = len(data)

print(f'{x_length} {y_length}')

heightmap = np.empty((y_length,x_length), np.int8)

heightmap = generate_array(data, heightmap)

print(heightmap)

lowpoints = find_lowpoints(heightmap)

print(lowpoints)

risk_level = calculate_risk_level(heightmap, lowpoints)

print(risk_level)