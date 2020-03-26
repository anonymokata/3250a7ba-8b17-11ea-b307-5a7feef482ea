

def word_search(data):
    names = data[0]
    final = {name: [] for name in names}
    lines = data[1:]
    first = []
    for name in names:
        first = get_first_letters(name, lines)
        up = []
        down = []
        left = []
        right = []
        up_right = []
        up_left = []
        down_right = []
        down_left = []
        for val in first:
            up.append([(val[0], val[1] + i) for i in range(len(name))])
            down.append([(val[0], val[1] - i) for i in range(len(name))])
            right.append([(val[0] + i, val[1]) for i in range(len(name))])
            left.append([(val[0] - i, val[1]) for i in range(len(name))])
            up_right.append([(val[0] + i, val[1] + i) for i in range(len(name))])
            up_left.append([(val[0] + i, val[1] - i) for i in range(len(name))])
            down_right.append([(val[0] - i, val[1] + i) for i in range(len(name))])
            down_left.append([(val[0] - i, val[1] - i) for i in range(len(name))])
        all_combos = [up, down, right, left, up_right, up_left, down_right, down_left]
        for combo in all_combos:
            for coordinates in combo:
                if name in _get_word(coordinates, lines, name):
                    final[name] = coordinates
                if name[::-1] in _get_word(coordinates, lines, name):
                    coordinates.reverse()
                    final[name] = coordinates
    return final

def get_first_letters(name, lines):
    first = []
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == name[0]:
                first.append((x, y))
    return first

def _get_word(coords, lines, name):
    result = []
    if len(coords) == len(name):
        for coord in coords:
            try:
                result.append(lines[coord[1]][coord[0]])
            except IndexError:
                pass
        return ''.join(result)
