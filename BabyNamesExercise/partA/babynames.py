import re
import sys

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    names = list()

    with open(filename, 'r') as inputFile:
        text = inputFile.read()

    year = re.search(r'Popularity\sin\s(\d{4})', text)
    names.append(year.group(1))
    rawListNames = re.findall(r'<tr align="right"><td>(\d+)</td><td>([A-Za-z]+)', text)

    sortedListNames = list()
    for element in rawListNames:
        sortedListNames.append(str(element[1] + ' ' + element[0]))

    sortedListNames.sort()
    names.extend(sortedListNames)
    return names


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    if args[0] == '--summaryfile':
        del args[0]

    for arg in args:
        text = '\n'.join(extract_names(arg)) + '\n'
        print(text)


if __name__ == '__main__':
    main()
