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
                #print(f"Syntax Error for {syntax_error}")
                return(None)
    return(line)

def calculate_completion(line):
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
            if opened[-1] == mapping[char]:
                #print(opened)
                #print(char)
                opened.pop(-1)
    #print(opened)
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    score = 0
    for opener in reversed(opened):
        score = score * 5
        score += points[opener]
    #print(score)
    return score
def return_score(char):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return points[char]
            
data = load_data()

incomplete_lines = []
for line in data:
    result = process_line(line)
    if result is not None:
        incomplete_lines.append(result)

#print(incomplete_lines)
scores = []
for incomplete in incomplete_lines:
    scores.append(calculate_completion(incomplete))

scores.sort()

print (scores[int(len(scores) /2)])