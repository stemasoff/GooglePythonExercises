import re
import sys



def extract_names(filename):
    names = list()

    with open(filename, 'r') as inputFile:
        text = inputFile.read()

    year = re.search(r'Popularity\sin\s(\d{4})', text)
    names.append(year.group(1))
    rawListNames = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)', text)

    dictNames = {x[1]: x[0] for x in rawListNames}


    sortedListNames = list(map(lambda x: str(x[1] + ' ' + x[0]), rawListNames))
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
            with open(arg + '.summary', 'w') as outputFile:
                outputFile.write(text)
    else:
        for arg in args:
            text = '\n'.join(extract_names(arg)) + '\n'
            print(text)


if __name__ == '__main__':
    main()
