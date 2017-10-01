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
    y = []
    with open(filename) as inf, open("output2.txt", 'w') as outf:
        data = inf.read()
        x = re.findall('\((.+?[\s\S]*?)\)', data)
        for line in x:
            y.append(' '.join(line.splitlines()))
        newest_x = []
        for item in y:
            count = 1
            found = False
            for i in range(len(item)):
                if found:
                    continue
                if (ord(item[i]) < 65 or ord(item[i]) > 90) and (ord(item[i]) < 97 or ord(item[i]) > 122):
                    found = True
            item2 = item + '\t' + str(count)
            newest_x.append(item2)
        new_x = ['{0}\n'.format(i) for i in newest_x]
        header(outf)
        outf.write(''.join(new_x))
        lines = len(new_x)
        outf.write(str(lines))

if __name__ == '__main__':
    main()







