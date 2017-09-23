import sys

"""
Tyler Coleman

CMPS 4143 Contemporary Programming Languages: Fall 2017

Data Structure(s) Used: [List]

Description: This program will take a user specified file and encrypt it, or
             decrypt it depending on the user's input. The user must provide a
             valid filename in the same directory as this program, a command:
             [encrypt] or [decrypt], and a shift value by which the document's
             characters will be shifted. The program will run continuously until
             the user enters the string "exit" (Not case sensitive).
"""
#Alphabet Tables for use in the encrypt_char_list and decrypt_char_list
#I made the names all uppercase to show that they are constants.
UPPERCASE_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

UNDERCASE_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
    @Function: get_input

    @Parameters: None

    @Returns: A list of the 3 user inputs stored in the list (inputs)

    @Description: This function promtps the user for 3 inputs
    A file name, a function(encrypt or decrypt) and the shift
    value that the file will be encrypted or decrypted with.
    All of these inputs are validated by calling input_check function.
"""
def get_input():
    #get input 1 (file name)
    inputs = []
    print("Please enter a file name with it's extension (then press enter).\n\
You can type [exit] at anytime to terminate the program.")
    #get the user input
    filename = input()
    #make sure they do not want to exit
    if(str(filename).lower() == "exit"): 
        program_kill()
    #append the file name to the empty list after it 
    #is put through the input checking funciton
    inputs.append(input_check(filename, 'filename'))
    filename = inputs[0]

    #get input 2 (encrypt or decrypt)
    print("\nIf you would like " + filename + " encrypted please type [encrypt].\n\
If you would like " + filename + " decrypted please type [decrypt].\n\
If you would like to stop please type [exit].")
    #get the user input
    enc_or_dec = input()
    #make sure they do not want to exit
    if(str(enc_or_dec).lower() == "exit"): 
        program_kill()
    #append the function the user desires to the 
    #inputs list after it is put through input checking.
    inputs.append(input_check(enc_or_dec, 'function'))
    enc_or_dec = inputs[1]

    #get input 3 (Shift value)
    if(enc_or_dec == 'encrypt'):
        print("\nPlease enter the shift value that your document will be encrypted with.")
    else:
        print("\nPlease enter the shift value that your document was encrypted with.")
    #get user input
    shift = input()
    #make sure they do not want to exit
    if(str(shift).lower() == "exit"): 
        program_kill()
    #append the shift value to the inputs list
    inputs.append(input_check(shift, 'key'))

    #return the validated 3 user inputs
    return inputs

"""
    @Function: input_check

    @Parameters: user_input, type_input

    @Returns: Either a string(filename), a string(encrypt/decrypt)
    or an integer value (shift) depending on which "type_input"
    is passed from the get_input function

    @Description: This function validates the 3 User inputs that are aquired 
    from the get_input function i.e. the filename must exist
    in the current directory, a valid function must be called
    (encrypt/decrypt) and the shift value must be an integer.
"""
def input_check(user_input, type_input):
    #filename checker:
    # This block tries to open the file for reading and excepts on a 
    # FileNotFoundError the except statement runs another try except 
    # block in a while loop that asks for a new user input and validates.
    if type_input == 'filename':
        filename = user_input
        try:
            #Try to Open the file
            f = open(filename, 'r',)
        except FileNotFoundError:
            print("Please enter a valid file name in your working directory.")
            invalid_filename = True
            #The first filename was invalid, so loop until the User enters a valid file name
            #or "exit"
            while invalid_filename:
                try:
                    filename = input()
                    if(str(filename).lower() == "exit"): 
                        program_kill()
                    f = open(filename, 'r',)
                    invalid_filename = False
                except FileNotFoundError:
                    print("Please enter a valid file name in your working directory.")
        f.close()
        #return the validated filename
        return filename

    #Function checker
    # This block makes sure the user has entered the string encrypt
    # of decrypt (or exit) then returns the validated value.
    elif type_input == 'function':
        enc_or_dec = user_input
        #Loop until the user enters either "encrypt" or "decrypt" (Not case sensitive).
        while enc_or_dec.lower() != "encrypt" and enc_or_dec.lower() != "decrypt":
            print("Please enter a valid function: [encrypt] or [decrypt]")
            enc_or_dec = input()
            if(str(enc_or_dec).lower() == "exit"): 
                program_kill()
        return enc_or_dec.lower()

    #Shift Checker
    #This block ensures the user has entered
    #first an integer value and second that it
    #is positive.
    else:
        shift = user_input
        #Validate that the key is within the specified range and it is an integer  
        try:
            #This will ValueError if shift is not an integer
            shift = int(shift)
            if(str(shift).lower() == "exit"): 
                program_kill()
            #The user entered a negative shift, so i take the absolute value and let them know.
            if shift < 0:
                shift = abs(shift)
                print("\nThe shift value must be a positive integer. The absolute value of any negative entry will be used.")
        except ValueError:
            print("Please enter a valid shift. The shift value must be a positive integer.")
            invalid_shift = True
            #Run until we get valid input or the user enters "exit"
            while invalid_shift:
                try:
                    shift = input()
                    if(str(shift).lower() == "exit"): 
                        program_kill()
                    #again looking for a ValueError
                    shift = int(shift)
                    #We finally got an integer as input
                    invalid_shift = False
                    #The user entered a negative shift, so i take the absolute value and let them know.
                    if shift < 0:
                        shift = abs(shift)
                        print("\nThe shift value must be a positive integer. The absolute value of any negative entry will be used.")
                except ValueError:
                    print("Please enter a valid shift. The shift value must be a positive integer.")
        
        return shift


"""
    @Function: encrypt_or_decrypt

    @Parameters: A list (un-encrypted list of all chars in the document), 
    An integer (The value that the characters will be shifted by in the english alphabet.),
    A string (This will tell the function whether to encrypt or decrypt the file.)

    @Returns: A list (the encrypted list of all chars in the document)

    @Description: This function takes a list of characters and makes a new list 
    of characters that are either encrypted or decrypted depending on user input.
    The encryption method is a simple alphabetic shift right or left by the "shift"
    value passed in.
"""
def encrypt_or_decrypt(char_list, shift, enc_or_dec):
    #converts the chars in the char_List to their ascii values
    ascii_list = [ord(char) for char in char_list]

    #negate the shift value if the user wants to decrypt the file
    if(enc_or_dec == 'decrypt'):
        shift = shift * -1
    """This statement is a list comprehension statement that is using a ternary operation.
       It checks the case of the character and applies the proper shift in the ascii table above. If the
       symbol that is found is not a letter it converts it to its char form.
       source for this idea: https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals
    """ 
    manipulated_char_list = [UPPERCASE_ALPHABET[(i - 65 + shift) % 26] if (i >= 65 and i <=90) else 
    UNDERCASE_ALPHABET[(i - 97 + shift) % 26] if (i >= 97 and i <=122) else chr(i) for i in ascii_list]
    #return the character list created by the above list comprehension statement.
    return manipulated_char_list
"""
    @Function: program_kill

    @Parameters: None

    @Returns: None
    
    @Description: This function is used at every user input
    prompt. if the user ever enters the string "exit" (not case sensitive)
    the program will immediately stop.
"""
def program_kill():
    print("\nThank you for using the encrypter/decrypter 9000.\n")
    sys.exit()

def main(times_called):
    
    #only display the welcome on the first time use.
    if times_called == 0:
        print("\nWelcome to the document encrypter/decrypter 9000\n")

    #get the inputs and validate them
    inputs = get_input()
    
    #Set the 3 inputs to variables for read
    enc_or_dec = inputs[1]
    shift = int(inputs[2])
    
    #open the file for reading AND writing with 'r+'
    f = open(filename, 'r+')

    #This will store all chars in the document.
    char_list= []
    #Loop through every character in every line in the file
    for line in f:
        for char in line:
            char_list.append(char)
    
    #This sets the file pointer f to the beginning
    #of the file (if it isn't already).
    f.seek(0)
    #this truncates everything after the pointer,
    #so...everything, effectively clearing out the 
    #file.
    f.truncate()

    #User wants to encrypt the file
    if enc_or_dec == "encrypt":
        #change the char list to an encrypted char lits
        encrypted_list = encrypt_or_decrypt(char_list, shift, 'encrypt')
        #write the list to the file without the list format
        f.write(''.join(encrypted_list))
        print("\nYour file has been encrypted!\nDon't forget, your decryption key is [" + str(shift) + "]\n")
    
    #The user wants to decrypt the file
    else:
        #change the char list to a decrypted char lits
        decrypted_list = encrypt_or_decrypt(char_list, shift, 'decrypt')
        #write the list to the file without the list format
        f.write(''.join(decrypted_list))
        print("\nYour file has been decrypted!\n")
    
    f.close()
    
#Main
if __name__ == '__main__':

    """
        Caution! This program will overwrite the chosen file
        with the encrypted/decrypted words. Make sure you 
        remember the shift value so it can be decrypted!
    """
    #First itteration of main
    i = 0
    main(i)
    i += 1
    #Run main until the user enters "exit"
    in_use = True
    while(in_use):
        print("Press [enter] to do another...\n\
Type [exit] to end the program.")
        inp =input()
        if inp.lower() != "exit":
            main(i)
            i += 1
        else:
            in_use = False
            print("\nThank you for using the encrypter/decrypter 9000.\n")