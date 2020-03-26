from word_search import is_present, handle_lists, get_names, get_coordinates, word_search, get_diagonals
from unittest import TestCase


class TestWordSearch(TestCase):

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

    # def test_find_horizontally_new_word(self):
    #     new_data = self.data().copy()
    #     new_data.insert(0, ["SCOTTY", "SULU"])
    #     result = new_word_search(new_data)
    #     expected = {
    #         'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
    #     }
    #     assert result == expected

    def test_find_horizontally_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
        }
        assert result == expected

    def test_find_horizontally_reversed(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
            'BONES': [(0, 6),(0, 7),(0, 8),(0, 9),(0, 10)],
        }
        assert result == expected

    def test_find_khan(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
            'BONES': [(0, 6),(0, 7),(0, 8),(0, 9),(0, 10)],
            'KHAN': [(5, 9), (5, 8),(5, 7), (5, 6)],
        }
        assert result == expected

    def test_get_diagonals(self):
        data = [
            ['A', '1', 'X'],
            ['B', '2', 'Y'],
            ['C', '3', 'Z']
        ]
        expected_1 = [
                ['X'],
                ['1', 'Y'],
                ['A', '2', 'Z'],
                ['B', '3'],
                ['C'],
        ]
        expected_2 = [
                ['A'],
                ['B', '1'],
                ['C', '2', 'X'],
                ['3', 'Y'],
                ['Z'],
        ]
        diagonals = get_diagonals(data)
        result = {x[0][0]: x for x in diagonals}
        self.assertCountEqual(result['C'], expected_1)
        self.assertCountEqual(result['A'], expected_2)

    def test_find_spock(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN", "SPOCK"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
            'BONES': [(0, 6),(0, 7),(0, 8),(0, 9),(0, 10)],
            'KHAN': [(5, 9), (5, 8),(5, 7), (5, 6)],
            'SPOCK': [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
        }
        assert result == expected

    def test_find_uhura(self):
        new_data = self.data().copy()
        new_data.insert(0, ["SCOTTY", "KIRK", "BONES", "KHAN", "SPOCK", "UHURA"])
        result = word_search(new_data)
        expected = {
            'SCOTTY': [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)],
            'KIRK': [(4, 7), (3, 7), (2, 7),(1, 7)],
            'BONES': [(0, 6),(0, 7),(0, 8),(0, 9),(0, 10)],
            'KHAN': [(5, 9), (5, 8),(5, 7), (5, 6)],
            'SPOCK': [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)],
            'UHURA': [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
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
