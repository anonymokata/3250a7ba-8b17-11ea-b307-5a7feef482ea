

def is_present(word, data):
    forward = word in ''.join(data)
    data.reverse()
    backward = word in ''.join(data)
    return forward or backward


def handle_lists(word, lines):
    vertical_lines = []
    for i in range(0, len(lines)):
        vertical_lines.append([val[i] for val in lines])
    return any([check_lists(word, vals) for vals in (lines, vertical_lines)])


def check_lists(word, lines):
    for line in lines:
        if is_present(word, line):
            return True

