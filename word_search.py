

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
    for name in data[0]:
        for count, line in enumerate(data[1:]):
            coordinates = _get_coordinates(name, line, count)
            if coordinates:
                result[name] = coordinates
            reverse_name = list(name)
            reverse_name.reverse()
            reverse_name = ''.join(reverse_name)
            coordinates = _get_coordinates(reverse_name, line, count)
            coordinates.reverse()
            if coordinates:
                result[name] = coordinates
    return result

def _get_coordinates(name, line, count):
    coordinates = []
    if name in ''.join(line):
        start = ''.join(line).find(name)
        coordinates = [(i, count) for i in range(start, start + len(name))]
    return coordinates
