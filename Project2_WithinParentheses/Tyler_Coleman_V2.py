import re
"""
Tyler Coleman

CMPS 4143 Contemporary Programming Languages: Fall 2017

Data Structure(s) Used: List [], strings

Description: This program will take a user specified file and and find
             all sets of words/numbers contained in prentheses and the 
             number of words in each set. Finally at the bottomr of the
             output file, it will display the number of sets that were found
"""

"""
    @Function: header

    @Parameters: file object

    @Returns: None

    @Description: Simple function used to write a header to a file
"""
def header(file):
    head = "Name: Tyler Coleman\nExplanation: This program will scan a file and find:\n\
all text within parentheses,\nThe number of lines in the document\
 that were contained in parentheses, and\nThe number of words in each line.\n\
All lines will be sorted according to the first characters in the first word.\n\n"
    file.write("%s" % head)


def main():
    filename = "alice.txt"
    lines_in_parenth = []
    #open inputfilename for reading and open a file to write results to.
    with open(filename) as inf, open("output2.txt", 'w') as outf:
        #get the contents of the file into on elarge string
        data = inf.read()
        #using regular expressions, find all instances of words contained within parenthesis
        contained_in_parenth = re.findall('\((.+?[\s\S]*?)\)', data)
        #Get the number of items that were contained in parenthesis
        num_lines = len(contained_in_parenth)

        #for each item that was contained in prenthesis
        #1:Get the number of words in that line using regular expression
        #2:get the items into string format
        #3:append all lines with the number of words in the line 
        # and then append a newline so they print out nicely
        for line in contained_in_parenth:
            count = len(re.findall('\w+', line))
            lines_in_parenth.append(' '.join(line.splitlines()))
            lines_in_parenth.append('\t' + str(count) + '\n')
        
        #write the header to the outfile
        header(outf)
        #write the list of items in string form to the file
        outf.write(''.join(lines_in_parenth))
        #write the number of lines to the end of the file
        outf.write('\n' + str(num_lines))


if __name__ == '__main__':
    main()







