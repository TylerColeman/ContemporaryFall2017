"""

"""

def header(file):
    head = "Name: Tyler Coleman\nExplanation: This program will scan a file and find:\n\
all text within parentheses,\nThe number of lines in the document\
 that were contained in parentheses, and\nThe number of words in each line.\n\
All lines will be sorted according to the first characters in the first word."
    file.write(head)

def find_parentheses(chars):
    string_list = []
    for index in range(int(len(chars))):
        i = 1
        string = ""
        if chars[index] == '(':
            string = string + chars[index]
            index += 1
            while chars[index] != ')':
                if chars[index] == ' ':
                    i += 1
                string = string + chars[index]
                index += 1
            string_list.append(string + ')' + str(i))
    return string_list

def main():
    filename = "input.txt"
    f = open(filename, 'r')
    chars = []
    for line in f:
        for char in line:
            chars.append(char)
    parenth_strings_list = find_parentheses(chars)
    num_lines = int(len(parenth_strings_list))
    print(parenth_strings_list)

if __name__ == '__main__':
    main()







