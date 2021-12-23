import numpy as np


def load_data():
    data_file = open("data/" + "5.txt", "r")
    lines = data_file.readlines()

    return lines


def parse_line(line):
    line = line.strip().split(" -> ")
    x1, y1 = [int(s) for s in line[0].split(",")]
    x2, y2 = [int(s) for s in line[1].split(",")]
    data = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
    return data


def points_between(co):
    x1 = co["x1"]
    x2 = co["x2"]
    y1 = co["y1"]
    y2 = co["y2"]
    dx = np.abs(x2 - x1)
    dy = np.abs(y2 - y1)
    if x1 == x2 or y1 == y2:
        # print(dx, dy)
        if dx > dy:
            points = zip(
                np.linspace(x1, x2, dx + 1, dtype=np.int16),
                np.linspace(y1, y2, dx + 1, dtype=np.int16),
            )
        elif dy > dx:
            points = zip(
                np.linspace(x1, x2, dy + 1, dtype=np.int16),
                np.linspace(y1, y2, dy + 1, dtype=np.int16),
            )
        return list(points)
    else:
        points = zip(
            np.linspace(x1, x2, dx + 1, dtype=np.int16),
            np.linspace(y1, y2, dy + 1, dtype=np.int16),
        )
        return list(points)


def apply_points(chart_data, points):
    # print(points)
    for point in points:
        chart_data[point[0], point[1]] += 1
    return chart_data


chart = np.zeros((1000, 1000), np.int16)
lines = load_data()
for line in lines:
    parsed_line = parse_line(line)
    points = points_between(parsed_line)
    chart = apply_points(chart, points)


np.set_printoptions(threshold=np.inf)
# print(f"{chart.ndim} {chart.size} {chart.shape}")
# print(chart)

# print(np.count_nonzero(chart))
# print((chart > 1).sum())
print(np.count_nonzero(chart > 1))
