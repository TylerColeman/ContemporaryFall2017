import sys
"""
Tyler Coleman

CMPS 4143 Contemporary Programming Languages: Fall 2017

Description: This program will take a user specified file and encrypt it, or
             decrypt it depending on the user's input.
Comments: Comment blocks will ALWAYS refer to the line of 
          code or block of code immediately below them.
"""
#Alphabet Tables for use in "The Workhorse" which you will find below.
UPPERCASE_ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
UNDERCASE_ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt_char_list(char_list, shift):
    #converts the chars in the words_list to their ascii values
    ascii_list = [ord(char) for char in char_list]
    """This statement is a list comprehension statement that is using a ternary operation.
       It checks the case of the character and applies the proper shift in the ascii table above. If the
       symbol that is found is not a letter it converts it to its char form.
       source for this idea: https://stackoverflow.com/questions/9987483/elif-in-list-comprehension-conditionals
    """ 
    encrypted_char_list = [UPPERCASE_ALPHABET[((i - 65) + (shift % 26)) % 26] if (i >= 65 and i <=90) else 
    UNDERCASE_ALPHABET[((i - 97) + (shift % 26)) % 26] if (i >= 97 and i <=122) else chr(i) for i in ascii_list]

    return encrypted_char_list

def decrypt_char_list(char_list, shift):
    #Same steps to decrypt the file as the encrypt function
    ascii_list = [ord(char) for char in char_list]
    decrypted_char_list = [UPPERCASE_ALPHABET[((i - 65) - (shift % 26)) % 26] if (i >= 65 and i <=90) else 
    UNDERCASE_ALPHABET[((i - 97) - (shift % 26)) % 26] if (i >= 97 and i <=122) else chr(i) for i in ascii_list]
    return decrypted_char_list

def program_kill():
    print("Thank you for using the encrypter/decrypter 9000.\n")
    sys.exit()

print("Welcome to the document encrypter/decrypter 9000\n\nPlease enter a file name with it's extension (then press enter).\n\
You can type [exit] at anytime to terminate the program.")
#Get input and kill program if user enters [exit]
filename = input()
tmp = str(filename).lower()
if(tmp == "exit"): program_kill()

#Filename validation before going into the encryption/decryption step
try:
    f = open(filename, 'r+',)
    invalid_filename = False
except FileNotFoundError:
    print("Please enter a valid file name in your working directory.")
    invalid_filename = True
    while invalid_filename:
        try:
            filename = input()
            tmp = str(filename).lower()
            if(tmp == "exit"): program_kill()
            f = open(filename, 'r+',)
            invalid_filename = False
        except FileNotFoundError:
            print("Please enter a valid file name in your working directory.")

pre_encrypted = []
char_list= []
#Make a list of all lines in the file
for line in f:
    pre_encrypted.append(line)
    #Make a list of all characters in all lines in the document
    for char in line:
        char_list.append(char)

print("\nIf you would like the file encrypted please type [encrypt].\n\
If you would like the file decrypted please type [decrypt].\n\
If you would like to stop please type [exit]")
enc_or_dec = input()
tmp = str(enc_or_dec).lower()
if(tmp == "exit"): program_kill()
#check for a valid input i.e: encrypt or decrypt
while enc_or_dec != "encrypt" and enc_or_dec != "decrypt":
    print("Please enter a valid function: [encrypt] or [decrypt]")
    enc_or_dec = input()
    tmp = str(enc_or_dec).lower()
    if(tmp == "exit"): program_kill()
        
#User wants to encrypt the document
if enc_or_dec == "encrypt":
    print("\nPlease enter the ""encryption key"" value for which you would like your document to be encrypted with.\n\
The value must be an integer between 1 and 1,000,000.\n\
This will be the value required to decrypt your file, so please remember it!" )
    invalid_shift = True
    shift = input()
    #Validate that the key is within the specified range and it is an integer  
    try:
        shift = int(shift)
        tmp = str(shift).lower()
        if(tmp == "exit"): program_kill()
    except ValueError:
        print("Please enter a valid key, Valid keys include 0 < key < 1000000.\n")
    while invalid_shift:
        try:
            shift = int(input())
            tmp = str(shift).lower()
            if(tmp == "exit"): program_kill()
            invalid_shift = False
        except ValueError:
            print("Please enter a valid key, Valid keys include 0 < key < 1000000.\n")
        
    #these 2 lines delete the text currently in the document
    f.seek(0)
    f.truncate()
    encrypted_list = []
    encrypted_list = encrypt_char_list(char_list, shift)
    #This writes our encrypted text into the same document.
    f.write(''.join(encrypted_list))
    #Friendly Reminder.
    print("Your file has been encrypted! Don't forget your decryption key is [" + str(shift) + "]\n")
    f.close()

#The user wants to decrypt the file
else:
    print("Please enter the ""encryption key"" value that the file was encrypted with.")
    shift = int(input())
    tmp = str(shift).lower()
    if(tmp == "exit"): program_kill()
    while shift < 1 and shift > 1000000:
        print("Please enter a valid key, Valid keys include 0 < key < 1000000\n")
        shift = int(input())
        tmp = str(shift).lower()
        if(tmp == "exit"): program_kill()
    f.seek(0)
    f.truncate()
    decrypted_list = []
    decrypted_list = decrypt_char_list(char_list, shift)
    f.write(''.join(decrypted_list))
    print("Your file has been decrypted!\n")
    f.close()



"""
Debug Code
"""
# shift = int(input())
# filename = "tmp.txt"
# f = open(filename, 'r+',)
# pre_encrypted = []
# word_list= []
# encrypted =[]
# #Make a list of all lines in the file
# for line in f:
#     pre_encrypted.append(line)
#     #Make a list of all characters in the document
#     for word in line:
#         word_list.append(word)
# ascii_list = [ord(letter) for letter in word_list]
# encrypted_word_list = [UPPERCASE_ALPHABET[((i - 65) + (shift % 26)) % 25] if (i >= 65 and i <=90) else UNDERCASE_ALPHABET[((i - 97) + (shift % 26)) % 25] if (i >= 97 and i <=122) else chr(i) for i in ascii_list]
# f.seek(0)
# f.truncate()
# f.write(''.join(encrypted_word_list))
# f.close()
