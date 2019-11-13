import os
import shutil
import sys
import re


def get_special_paths(pathsToSearch):
    specialPattern = '__\w*__'
    absolutePaths = []

    for path in pathsToSearch:
        for root, dirs, files in os.walk(path):
            for file in files:
                if re.search(specialPattern, file) is not None:
                    absolutePaths.append(root + '/' + file)
    return absolutePaths


def copy_to(paths, dir):
    for path in paths:
        shutil.copy(path, dir)


def zip_to(paths, zipfile):
    pathsToZip = ' '.join(paths)
    os.system(f'zip -j {zipfile} {pathsToZip}')


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir]")
        sys.exit(1)


    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]


    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]


    if len(args) == 0:
        print("error: must specify dir")
        sys.exit(1)


    paths = get_special_paths(args)
    try:
        copy_to(paths, todir)
    except NameError:
        pass


    try:
        zip_to(paths, tozip)
    except NameError:
        pass


if __name__ == "__main__":
    main()
