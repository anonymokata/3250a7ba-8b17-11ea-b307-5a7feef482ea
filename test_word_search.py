from word_search import is_present, handle_lists, get_names, get_coordinates


class TestWordSearch():

    def test_word_found_in_a_list_of_strings(self):
        word = 'data'
        data = ['d', 'a', 't', 'a']
        result = is_present(word, data)
        assert result == True

    def test_word_found_in_a_list_of_strings_written_in_reverse(self):
        word = 'data'
        data = ['a', 't', 'a', 'd']
        result = is_present(word, data)
        assert result == True

    def test_word_found_going_down(self):
        word = 'data'
        data = [
            ['d', 't', 'a', 'd'],
            ['a', 't', 'a', 'd'],
            ['t', 't', 'a', 'd'],
            ['a', 't', 'a', 'd'],
        ]
        result = handle_lists(word, data)
        assert result == True

    def test_word_not_present(self):
        word = 'nothing'
        data = [
            ['d', 't', 'a', 'd'],
            ['a', 't', 'a', 'd'],
            ['t', 't', 'a', 'd'],
            ['a', 't', 'a', 'd'],
        ]
        result = handle_lists(word, data)
        assert result == False

    def test_multiple_name_checks(self):
        names = ['data', 'rat']
        data = [['d', 'a', 't', 'a']]
        result = get_names(names, data)
        assert result[0] == names[0]

    def test_get_coordinates(self):
        name = 'data'
        lines = [['d', 'a', 't', 'a']]
        result = get_coordinates(name, lines)
        assert result['data'] == [(0, 0), (0, 1), (0, 2), (0, 3)]
