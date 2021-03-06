# word-search

Given a text file consisting of a list of words as the first line, followed by lines of single character strings, this word-search can locate and provide the x,y coordinates for the words in the first line.

For example, given a text file with this information:
```
"CAT","DOG","ELF","GLORFINDEL","HOUSE"
"J","T","V","E","X","X","J","U","S","X","H","P","T","M","P"
"Q","W","S","M","N","B","E","O","G","Z","H","T","K","U","G"
"W","J","D","T","A","Z","H","K","W","I","X","Z","H","U","M"
"H","H","M","T","G","Y","C","Q","P","G","V","R","Q","S","H"
"E","Z","L","Y","Y","O","R","R","L","R","R","S","D","W","T"
"Z","Y","P","X","J","K","D","O","T","E","Y","Y","O","V","T"
"I","E","A","M","J","T","R","I","N","N","N","O","M","Z","M"
"A","O","X","R","U","F","L","Y","R","M","L","B","I","A","T"
"L","M","X","B","I","U","O","L","K","Z","Q","P","E","P","K"
"P","L","D","N","E","S","U","O","H","A","J","Q","E","G","T"
"H","Y","D","C","F","E","Y","J","Q","N","G","P","P","F","S"
"N","E","K","T","S","C","O","V","E","A","F","Z","L","T","E"
"L","E","E","A","A","D","M","A","M","G","X","E","U","L","S"
"Q","I","U","C","X","M","V","G","V","B","E","O","F","E","F"
"I","I","V","R","W","J","C","Y","F","E","J","I","R","X","X"
````
You would get this result:
```
"CAT": [(3, 13), (3, 12), (3, 11)],
"DOG": [(6, 5), (5, 4), (4, 3)],
"ELF": [(11, 12), (12, 11), (13, 10)],
"GLORFINDEL": [(9, 3), (8, 4), (7, 5), (6, 6), (5, 7), (4, 8), (3, 9), (2, 10), (1, 11), (0, 12)],
"HOUSE": [(8, 9), (7, 9), (6, 9), (5, 9), (4, 9)]

```
# Use
- create a virtualenv with python 3.6.4
- pip install the requirements file
- create or move a `txt` file into the `data` directory
- run this command: `python word_search.py --filename [file name]`


# Notes
My original attempt involved checking each list of strings, then creating a new stack of lists by rotating the data ninety degrees. Then I ended up using a `numpy` method to create stack of lists for the diagonals, and then yet another stack for the other diagonals. Calculating coordinates turned out be a very complex task and stalled me for a while.

The real breakthrough happened when I realized that for each letter that is the first letter of the name you're searching for there are only at most 8 legitimate sets of coordinates. So instead of constructing entires lists and trying to derive coordinates, I only needed the coordinates of the first letters, and the coordinate from there could very easily be calculated by just adding by the length of the name in the eight cardinal directions.

Invalid coordinates were ignored. I don't know how efficient it is, or how well this solution would scale. I think it is a pretty elegant solution. Being able to leverage the tests I wrote for the original solution proved to be very helpful and provided a lot of confidence when both when I was writing the new solution and when I was refactoring.


# Improvement
One obvious place for refactoring is this method:
```
def get_eight_viable_answers(letter, name):
    result = []
    result.append([(letter[0], letter[1] + i) for i in range(len(name))])
    result.append([(letter[0], letter[1] - i) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1]) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1]) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1] + i) for i in range(len(name))])
    result.append([(letter[0] + i, letter[1] - i) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1] + i) for i in range(len(name))])
    result.append([(letter[0] - i, letter[1] - i) for i in range(len(name))])
    return result
```
It seems like a pretty good candidate for DRY refactoring. However I have yet to figure out a good way to refactor this.

Another place for improvement is this method:
```
def _get_word(coords, lines, name):
    result = []
    if len(coords) == len(name):
        for coord in coords:
            try:
                result.append(lines[coord[1]][coord[0]])
            except IndexError:
                pass
        return ''.join(result)

```
I am not sure if it's best to go foward with just catching and handling the `IndexError` or just check against the boundary conditions to avoid the error entirely. The advantage of the exception handling is that it removes the opportunity for errors when figuring out the boundaries. One potential downside is it's possible that the wrong errors might end up failing silently.
