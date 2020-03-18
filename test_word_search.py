from word_search import is_present, handle_lists


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
