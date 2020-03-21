

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


def get_coordinates(name, lines):
    if handle_lists(name, lines):
        for key, line in enumerate(lines):
            start = ''.join(line).find(name)
            start = start if start > 0 else 0
            return {name: [(key, i) for i in range(start, len(name))]}


def word_search(data):
    result = {}
    rotated_lines = rotate_lines(data[1:])
    for name in data[0]:
        result[name] = []
        for count, line in enumerate(data[1:]):
            result = get_name_and_coordinates(result, name, line, count)
            if result[name]:
                break
        for count, line in enumerate(rotated_lines):
            result = get_name_and_coordinates(result, name, line, count, rotate=True)
            if result[name]:
                break
    return result

def get_name_and_coordinates(result, name, line, count, rotate=False):
    coordinates = _get_coordinates(name, line, count, rotate=rotate)
    reverse_coordinates = _get_coordinates(get_reverse_name(name), line, count, rotate=rotate)
    result[name].extend(coordinates)
    reverse_coordinates.reverse()
    result[name].extend(reverse_coordinates)
    return result

def rotate_lines(lines):
    result = []
    for i in range(len(lines[0])):
        x = [line[i] for line in lines]
        result.append(x)
    return result

def get_reverse_name(name):
    reverse_name = list(name)
    reverse_name.reverse()
    return ''.join(reverse_name)

def _get_coordinates(name, line, count, rotate=False):
    coordinates = []
    if name in ''.join(line):
        start = ''.join(line).find(name)
        if rotate:
            coordinates = [(count, i) for i in range(start, start + len(name))]
        else:
            coordinates = [(i, count) for i in range(start, start + len(name))]
    return coordinates
