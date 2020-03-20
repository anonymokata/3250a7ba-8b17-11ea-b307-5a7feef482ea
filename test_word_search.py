from word_search import is_present, handle_lists, get_names, get_coordinates, word_search


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

    def test_find_horizontally(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
        }
        assert result == expected

    def test_find_horizontally_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
        }
        assert result == expected

    def names(self):
        return ["BONES", "KHAN", "KIRK", "SCOTTY", "SPOCK", "SULU", "UHURA"]

    def data(self):
        return [
            ["U", "M", "K", "H", "U", "L", "K", "I", "N", "V", "J", "O", "C", "W", "E"],
            ["L", "L", "S", "H", "K", "Z", "Z", "W", "Z", "C", "G", "J", "U", "Y", "G"],
            ["H", "S", "U", "P", "J", "P", "R", "J", "D", "H", "S", "B", "X", "T", "G"],
            ["B", "R", "J", "S", "O", "E", "Q", "E", "T", "I", "K", "K", "G", "L", "E"],
            ["A", "Y", "O", "A", "G", "C", "I", "R", "D", "Q", "H", "R", "T", "C", "D"],
            ["S", "C", "O", "T", "T", "Y", "K", "Z", "R", "E", "P", "P", "X", "P", "F"],
            ["B", "L", "Q", "S", "L", "N", "E", "E", "E", "V", "U", "L", "F", "M", "Z"],
            ["O", "K", "R", "I", "K", "A", "M", "M", "R", "M", "F", "B", "A", "P", "P"],
            ["N", "U", "I", "I", "Y", "H", "Q", "M", "E", "M", "Q", "R", "Y", "F", "S"],
            ["E", "Y", "Z", "Y", "G", "K", "Q", "J", "P", "C", "Q", "W", "Y", "A", "K"],
            ["S", "J", "F", "Z", "M", "Q", "I", "B", "D", "B", "E", "M", "K", "W", "D"],
            ["T", "G", "L", "B", "H", "C", "B", "E", "C", "H", "T", "O", "Y", "I", "K"],
            ["O", "J", "Y", "E", "U", "L", "N", "C", "C", "L", "Y", "B", "Z", "U", "H"],
            ["W", "Z", "M", "I", "S", "U", "K", "U", "R", "B", "I", "D", "U", "X", "S"],
            ["K", "Y", "L", "B", "Q", "Q", "P", "M", "D", "F", "C", "K", "E", "A", "B"],
        ]
