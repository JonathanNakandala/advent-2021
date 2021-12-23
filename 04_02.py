from textwrap import wrap

data_file = open("data/" + "4.txt", "r")
lines = data_file.readlines()

numbers = lines[0].strip().split(",")
numbers = [int(i) for i in numbers]

lines.pop(0)
lines.pop(0)


class BingoBoard:
    def __init__(self, data):
        self.playboard = [
            [
                {"value": data[0][0], "hit": False},
                {"value": data[1][0], "hit": False},
                {"value": data[2][0], "hit": False},
                {"value": data[3][0], "hit": False},
                {"value": data[4][0], "hit": False},
            ],
            [
                {"value": data[0][1], "hit": False},
                {"value": data[1][1], "hit": False},
                {"value": data[2][1], "hit": False},
                {"value": data[3][1], "hit": False},
                {"value": data[4][1], "hit": False},
            ],
            [
                {"value": data[0][2], "hit": False},
                {"value": data[1][2], "hit": False},
                {"value": data[2][2], "hit": False},
                {"value": data[3][2], "hit": False},
                {"value": data[4][2], "hit": False},
            ],
            [
                {"value": data[0][3], "hit": False},
                {"value": data[1][3], "hit": False},
                {"value": data[2][3], "hit": False},
                {"value": data[3][3], "hit": False},
                {"value": data[4][3], "hit": False},
            ],
            [
                {"value": data[0][4], "hit": False},
                {"value": data[1][4], "hit": False},
                {"value": data[2][4], "hit": False},
                {"value": data[3][4], "hit": False},
                {"value": data[4][4], "hit": False},
            ],
        ]

    def get_value(self, x, y):
        return self.playboard[x][y]["value"]

    def get_data(self):
        return self.playboard

    def set_hit(self, x, y):
        self.playboard[x][y]["hit"] = True

    def set_number(self, number):
        for y_idx, y in enumerate(self.playboard):
            for x_idx, x in enumerate(y):
                if self.playboard[x_idx][y_idx]["value"] == number:
                    # print(f'x Val: {x["value"]} number:{number} and {self.playboard[x_idx][y_idx]["value"]} ')
                    self.playboard[x_idx][y_idx]["hit"] = True

    def __check_win_column(self):
        for x in range(5):
            if (
                self.playboard[0][x]["hit"]
                and self.playboard[1][x]["hit"]
                and self.playboard[2][x]["hit"]
                and self.playboard[3][x]["hit"]
                and self.playboard[4][x]["hit"]
            ):
                # print(f"Winning Row number: {x}")
                return True
        return False

    def __check_win_row(self):
        for x in range(5):
            if (
                self.playboard[x][0]["hit"]
                and self.playboard[x][1]["hit"]
                and self.playboard[x][2]["hit"]
                and self.playboard[x][3]["hit"]
                and self.playboard[x][4]["hit"]
            ):
                # print(f"winning Row number: {x}")
                return True
        return False

    def check_win(self):
        return self.__check_win_column() or self.__check_win_row()

    def sum_of_unmarked(self):
        sum = 0
        for y_idx, y in enumerate(self.playboard):
            for x_idx, x in enumerate(y):
                if self.playboard[x_idx][y_idx]["hit"] == False:
                    sum += self.playboard[x_idx][y_idx]["value"]
        return sum


boards = []

board_data = []

for line in lines:
    if line == "\n":
        boards.append(BingoBoard(board_data))
        board_data = []
        continue
    line = line.strip()
    line = wrap(line, 2)
    line = [int(i) for i in line]
    board_data.append(line)

winning_board_index = None
winning_number = None
winning_boards_list = []
print(f"Total Boards: {len(boards)}")

for number_index, number in enumerate(numbers):
    for board_index, board in enumerate(boards):
        board.set_number(number)

    for check_board_index, check_board in enumerate(boards):
        if check_board_index not in winning_boards_list:
            if check_board.check_win() == True:
                winning_board_index = check_board_index
                winning_number = number
                print(
                    f"Winning Number: {number} and Board index: {winning_board_index}"
                )
                winning_sum = boards[check_board_index].sum_of_unmarked()
                print(
                    f"Winning Sum: {winning_sum} Answer: {winning_sum*winning_number}"
                )
                winning_boards_list.append(check_board_index)


# print(boards[winning_board_index].get_data())
