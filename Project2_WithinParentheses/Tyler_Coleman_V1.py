"""

"""

def header(file):
    head = "Name: Tyler Coleman\nExplanation: This program will scan a file and find:\n\
all text within parentheses,\nThe number of lines in the document\
 that were contained in parentheses, and\nThe number of words in each line.\n\
All lines will be sorted according to the first characters in the first word.\n\n"
    file.write("%s" % head)

def find_parentheses(chars):
    string_list = []
    for index in range(int(len(chars))):
        i = 1
        string = ""
        if chars[index] == '(':
            #string = string + chars[index]
            index += 1
            while chars[index] != ')':
                if chars[index] == ' ':
                    i += 1
                if chars[index] != '\n':
                    string = string + chars[index]
                index += 1
            string_list.append(string + ')  ' + str(i))
    return string_list

def sort_list(parenth_lines):
    parenth_lines.sort(key = str.lower)
    new_list = ["({0}\n".format(i) for i in parenth_lines]
    num_lines = int(len(parenth_lines))
    new_list.append('\n' + str(num_lines))
    return new_list

def main():
    filename = "alice.txt"
    f = open(filename, 'r')
    f2 = open("output.txt", 'w')
    chars = []
    for line in f:
        for char in line:
            chars.append(char)
    parenth_strings_list = find_parentheses(chars)
    final_list = sort_list(parenth_strings_list)
    header(f2)
    f2.write(''.join(final_list))

if __name__ == '__main__':
    main()







