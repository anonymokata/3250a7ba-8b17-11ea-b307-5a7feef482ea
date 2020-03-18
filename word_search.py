

def is_present(word, data):
    result = word in ''.join(data)
    if result:
        return result
    data.reverse()
    return word in ''.join(data)
