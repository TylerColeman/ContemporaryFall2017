import re
"""

"""

def header(file):
    head = "Name: Tyler Coleman\nExplanation: This program will scan a file and find:\n\
all text within parentheses,\nThe number of lines in the document\
 that were contained in parentheses, and\nThe number of words in each line.\n\
All lines will be sorted according to the first characters in the first word.\n\n"
    file.write("%s" % head)


def main():
    filename = "alice.txt"
    with open(filename) as inf:
        data = inf.read()
        x = re.findall('\((.*)\)', data)
    f = open("output2.txt", 'w')
    new_x = ['{0}\n'.format(i) for i in x]
    header(f)
    f.write(''.join(new_x))

if __name__ == '__main__':
    main()







