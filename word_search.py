

def is_present(word, data):
    forward = word in ''.join(data)
    data.reverse()
    backward = word in ''.join(data)
    return forward or backward


def handle_lists(word, lines):
    if check_lists(word, lines):
        return True
    vertical_lines = []
    for i in range(0, len(lines)):
        vertical_lines.append([val[i] for val in lines])
    if check_lists(word, vertical_lines):
        return True

def check_lists(word, lines):
    for line in lines:
        if is_present(word, line):
            return True

