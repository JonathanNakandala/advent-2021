def load_data():
    with open("data/" + "10.txt") as f:
        lines = [line.strip() for line in f]
    return lines


def process_line(line):
    #print(line)
    mapping  = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }
    opened = []
    syntax_error = None
    for char in line:
        #print(f"Current Char {char}")
        if char in ['(', '[', '{', '<'  ]:
            opened.append(char)
        if char in [')', ']', '}', '>']:
            #print(opened[-1])
            if opened[-1] == mapping[char]:
                #print(opened)
                #print(char)
                opened.pop(-1)
            else:
                syntax_error = char
                print(f"Syntax Error for {syntax_error}")
                break
    return(syntax_error)

def return_score(char):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return points[char]
            
data = load_data()

total_score = 0
for line in data:
    result = process_line(line)
    if result is not None:
        total_score += return_score(result)

print(total_score)
