

def is_present(word, data):
    forward = word in ''.join(data)
    data.reverse()
    backward = word in ''.join(data)
    return forward or backward


def handle_lists(word, lines):
    vertical_lines = []
    if len(lines) > 1:
        for i in range(0, len(lines)):
            vertical_lines.append([val[i] for val in lines])
    return any([check_lists(word, vals) for vals in (lines, vertical_lines)])


def check_lists(word, lines):
    for line in lines:
        if is_present(word, line):
            return True


def get_names(names, lines):
    result = []
    for name in names:
        if handle_lists(name, lines):
            result.append(name)
    return result


def get_coordinates(name, line):
    print(line)
    print(''.join(line))
    print(''.join(line).find(name))
    return None
