

def is_present(word, data):
    forward = word in ''.join(data)
    data.reverse()
    backward = word in ''.join(data)
    return forward or backward


def handle_lists(word, list_of_lists):
    for lst in list_of_lists:
        if is_present(word, lst):
            return True
    data = []
    for i in range(0, len(list_of_lists)):
        data.append([val[i] for val in list_of_lists])
    for lst in data:
        if is_present(word, lst):
            return True

