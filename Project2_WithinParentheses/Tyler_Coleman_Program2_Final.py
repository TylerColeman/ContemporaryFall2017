import re
"""
Tyler Coleman

CMPS 4143 Contemporary Programming Languages: Fall 2017

Data Structure(s) Used: List [], strings

Description: This program will take a user specified file and and find
             all sets of words/numbers contained in prentheses and the 
             number of words/numbers in each set. Finally at the bottom of the
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
All text within parentheses, The number of lines\nin the document\
 that were contained in parentheses,\nand The number of words in each line.\
 All lines will\nbe sorted according to the first characters in the first word.\n\n"
    file.write("%s" % head)

"""
    MAIN
"""
def main():
    filename = "alice.txt"
    lines_in_parenth = []
    #open input filename for reading and open a file to write results to.
    with open(filename) as inf, open("Coleman_alice_out.txt", 'w') as outf:
        #get the contents of the file into one large string
        data = inf.read()
        #using regular expressions, find all instances of words contained within parenthesis
        contained_in_parenth = re.findall('\((.+?[\s\S]*?)\)', data)
        #Get the number of items that were contained in parenthesis
        num_lines = len(contained_in_parenth)
        #sort the list of items 
        contained_in_parenth.sort(key=str.lower)

        #Get the number of words in each line after removing
        #commas and hyphens to allow regex to accurately count words
        tmp = []
        counts = []
        for i in contained_in_parenth:
            #removes commas and hyphens and single quotes
            i = i.replace(",", "").replace("-", "").replace("'", "")
            tmp.append(i)
        for i in tmp:
            #returns the number of words found in the item i
            counts.append(len(re.findall('\w+', i)))

        #for each item that was contained in prenthesis
        #1:get the items into string format
        #2:append all lines with the number of words in the line 
        #then append a newline so they print out nicely
        index = 0
        for line in contained_in_parenth:
            #this joins each element into a string with no new lines
            #and appends it 
            lines_in_parenth.append(' '.join(line.splitlines()))
            #append the word count
            lines_in_parenth.append('\t' + str(counts[index]) + '\n')
            #assure we do not go out of bounds
            if index < len(counts):
                index += 1
        
        #write the header to the outfile
        header(outf)
        #write the list of items in string form to the file
        outf.write(''.join(lines_in_parenth))
        #write the number of lines to the end of the file
        outf.write('\n' + str(num_lines))


if __name__ == '__main__':
    main()







