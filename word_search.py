import numpy

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
        result = find_word(data[1:], name, result)
        result = find_word(rotated_lines, name, result, rotate=True)
    return result


def find_word(lines, name, result, rotate=False):
    for count, line in enumerate(lines):
        result = get_name_and_coordinates(result, name, line, count, rotate=rotate)
        if result[name]:
            return result
        result = _get_diagonals(name, lines, result)
    return result

def _get_diagonals(name, lines, result):
    diagonals = get_diagonals(lines)
    for diagonal in diagonals:
        for count_l, line in enumerate(diagonal):
            x = _get_coordinates(name, line, count_l)
            if name in ''.join(line):
                if count_l > len(line[0]):
                    start_column = count_l - (len(lines) - 1)
                else:
                    start_column = count_l
                start = ''.join(line).find(name)
                real_start = start_column + start
                beginning_of_word = (real_start, start)
                coordinates = [(beginning_of_word[0] + i, beginning_of_word[1] + i) for i in range(len(name))]
                result[name] = coordinates
                return result
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


def _get_coordinates(name, line, count, rotate=False, diagonal=False):
    coordinates = []
    if name in ''.join(line):
        start = ''.join(line).find(name)
        if rotate:
            coordinates = [(count, i) for i in range(start, start + len(name))]
        else:
            coordinates = [(i, count) for i in range(start, start + len(name))]
    return coordinates


def get_diagonals(lines):
    matrix = numpy.array(lines)
    shape = matrix.shape[0]
    left_to_right = [numpy.diag(matrix, k=i).tolist() for i in range(-shape + 1, shape)]
    matrix = numpy.flipud(matrix)
    right_to_left = [numpy.diag(matrix, k=i).tolist() for i in range(-shape + 1, shape)]
    return [right_to_left, left_to_right]
