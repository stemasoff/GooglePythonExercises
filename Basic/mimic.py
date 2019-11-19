"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    with open(filename, 'r') as inputFile:
        words = inputFile.read().split()

    mimicDict = {}
    symbols = '`.,)(*-?:;"!`_' + "'"
    for i in range(len(words) - 1):
        if not words[i].isalpha():
            words[i].strip(symbols)

        if not mimicDict:
            mimicDict[''] = [words[i]]

        if words[i] not in mimicDict:
            mimicDict[words[i]] = [words[i + 1].strip(symbols)]
        else:
            mimicDict[words[i]].append(words[i + 1].strip(symbols))
    return mimicDict


def print_mimic(mimicDict, word):
    text = ''
    countWords = 200
    while countWords != 0:
        if word not in mimicDict:
            word = random.choice(mimicDict[''])

        text = text + word + ' '
        word = random.choice(mimicDict[word])
        countWords -= 1
    return text


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])

    with open('randomText.txt', 'w') as outFile:
        outFile.write(print_mimic(dict, 'Rabbit'))


if __name__ == '__main__':
    main()
