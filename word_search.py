import numpy
from math import sqrt

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
            if name in ''.join(line):
                if count_l > len(line[0]):
                    start_column = count_l - (len(lines) - 1)
                else:
                    start_column = count_l + len(lines)
                start = ''.join(line).find(name)
                real_start = start_column + start
                if real_start < 0:
                    real_start = (len(lines) - 1) + real_start
                    beginning_of_word = (real_start, start)
                    coordinates = [(beginning_of_word[0] - i, beginning_of_word[1] + i) for i in range(len(name))]
                    result[name] = coordinates
                else:
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


def new_word_search(data):
    names = data[0]
    lines = data[1:]
    result = {name: {letter: [] for letter in name} for name in names}
    answers = []
    for name in names:
        for key, line in enumerate(lines):
            for index, letter in enumerate(line):
                if letter in name:
                    result[name][letter].append((index, key))
    x = {letter: [] for letter in name}
    for key, val in result.items():
        for index, letter in enumerate(name):
            for c in val[letter]:
                try:
                    for i in val[name[index + 1]]:
                        if ((c[0] - i[0])**2 + (c[1] - i[1])**2)**0.5 == 1:
                            x[letter].append(c)
                            x[name[index + 1]].append(i)
                            # x.update({letter: c, name[index + 1]: i})
                            # x.append([c, letter, i, name[index + 1]])
                            # x.append('{} -> {} is {}->{}'.format(letter, name[index + 1], c, i))
                except Exception:
                    for i in val[name[index -1]]:
                        if ((c[0] - i[0])**2 + (c[1] - i[1])**2)**0.5 == 1:
                            # x.update({letter: c, name[index - 1]: i})
                            x[letter].append(c)
                            x[name[index - 1]].append(i)
                            # x.append((i, c, letter))
                            # x.append((c, letter, i, name[index - 1]))
                            # x.append('{} -> {} is {}->{}'.format(letter, name[index - 1], c, i))
    print(x[name[0]])
    for val in x[name[0]]:


    res = []
    #     for i in range(len(name)):
    #         if i + 1 < len(name):
    #             a = result[name][name[i]] + result[name][name[i + 1]]
    #             answers.append(a)

    for name, value in result.items():
        for letter in name:
            letter_1 = result[name][letter]
            letter_2 = result[name][name[name.index(letter) + 1]]
            x = []
            for c in letter_1:
                pass
                # print(name)
                # print(letter)
                # print(coordinates_check(c, letter_2))
                # if (c[0] + 1, c[1]) in letter_2:
                #     x.append((c[0] + 1, c[1]))
                #     print(letter)
                #     print(c)
                #     print((c[0] + 1, c[1]))
                # if (c[0] - 1, c[1]) in letter_2:
                #     x.append((c[0] - 1, c[1]))
                # if (c[0], c[1] + 1) in letter_2:
                #     x.append((c[0], c[1] + 1))
                # if (c[0], c[1] - 1) in letter_2:
                #     x.append((c[0], c[1] - 1))
                # if (c[0] + 1, c[1] + 1) in letter_2:
                #     x.append((c[0] + 1, c[1] + 1))
                # if (c[0] - 1, c[1] + 1) in letter_2:
                #     x.append((c[0] - 1, c[1] + 1))
                # if (c[0] + 1, c[1] - 1) in letter_2:
                #     x.append((c[0] + 1, c[1] - 1))
                # if (c[0] - 1, c[1] - 1) in letter_2:
                #     x.append((c[0] - 1, c[1] - 1))
            # print(x)

def coordinates_check(coordinate, values):
    result = []
    for val in values:
        if val[0] - coordinate[0] == 1:
           result.append(val)
        elif coordinate[0] - val[0] == 1:
           result.append(val)
        elif val[0] - coordinate[0] == 1:
           result.append(val)
        elif coordinate[0] - val[0] == 1:
           result.append(val)
    return result


    # total = []
    # for key, line in enumerate(answers):
    #     for coord in line:
    #         if key + 1 < len(answers):
    #             for c in answers[key + 1]:
    #                 first = coord[0] - c[0]
    #                 second = c[0] - coord[0]
    #                 third = coord[1] - c[1]
    #                 fourth = c[1] - coord[1]
    #                 if first is 1:
    #                     total.append(coord)
    #                     total.append(c)
    #                 elif second is 1:
    #                     total.append(coord)
    #                     total.append(c)
    #                 elif fourth is 1:
    #                     total.append(coord)
    #                     total.append(c)
    # print(total)
    return result
