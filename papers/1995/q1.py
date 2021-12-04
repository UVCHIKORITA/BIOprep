"""

You are required to implement a program to encode and decode text using a string-based coding method as described below.
Your program should have a simple menu-based structure. Its main menu is

1) Enter an encoding "key" string.
2) Encode a section of text using the current key.
3) Decode a section of text using the current key.
4) Exit the program.

Choice?
When Option 1 is selected, the program should read in a one-line string from the keyboard. This should be converted to
upper case, all characters other than A to Z, comma, full stop and space should be deleted, and the string adapted to
be used as a code key as follows.

The key must contain all the characters A to Z, comma, full stop and space exactly once. If a character occurs more than
once, the second, third etc. occurrences should be deleted. If a character does not occur in the string, it should be
added to the end in the order given above - so a blank input string would simply give the code string
'ABCDEFGHIJKLMNOPQRSTUVWXYZ,. '

For example, the input string 'I wandered lonely as a cloud' gives the code key
'I WANDERLOYSCUBFGHJKMPQTVXZ,.'

When Option 2 is chosen, the program should read in a text message from the keyboard; this may not be more than 250
characters long and your program should check for this limit. Note that Pascal will not let you enter more than 127
characters per line. Characters other than A to Z, comma, full stop and space should be removed, and the input should
finish when a # character is encountered in the text. Line breaks, except when immediately preceded by a \ character
(see below), should be converted into spaces. No text or spaces before the # should be deleted, but all text after it on
the same line must be and the input buffer must be cleared to the end of the line.

Your program should then encode the text as follows. Start with a marker, p, pointing to the first character in the key.
For each character in the message, p is moved right by the value of the character and the key symbol at p gives the next
character in the encoded message.

The value of characters is given in order: A=1, Z=26, space=29. If p moves beyond the end if the key, 29 is subtracted
from it (in other words, it rolls round to the start). This means that one error in copying the encoded message will
result in two character errors in the decoded message, but this is acceptable.

For example, with the above code key, the message 'I WANDER' would be encoded as follows. p starts with a value of 1,
pointing to the I in the key. The value of the first character in the message (also I), 9, is added to give 10; the 10th
key character is O. Space has a value of 29 - and therefore, when rolled round, p is again 10 and the first two output
characters are OO. W has a value of 23, so the 4th character in the code is selected next: A. And so on, to give the
encoded form 'OOANJQ,G'.

The encoded message is output in this way. It is printed as lines of maximum length 50 characters, and if it must be
split after the 50th character on a line, a \ should be printed to indicate that the line end should be ignored. At the
end of the text, a # should be printed. You should also output the original message, after transformation to upper case
etc, in the same format, to allow the user to see what the message will look like when decoded.

Option 3 requires you to reverse this process, using the same input and output methods with the exception of printing
the encoded text again. The same coding key should be used.

When option 4 is selected your program should terminate. After the other menu options have been executed, you might like
to ask the user to press enter before returning to the main menu.

"""


currentkey = ""

def validateInput(acceptable_values, input_val):
    if input_val in acceptable_values:
        return True
    return False


def menu():
    print("1) Enter an encoding key string")
    print("2) Encode a section of text using the current key.")
    print("3) Decode a section of text using the current key.")
    print("4) Exit the program.")
    try:
        selection = int(input().strip())
        if not validateInput([1, 2, 3, 4], selection):
            print("Invalid number entered. Please try again.")
            print("")
            print("------")
            print("")
            menu()
        else:
            if selection == 1:
                createkey()
            elif selection == 2:
                pass
            elif selection == 3:
                pass
            elif selection == 4:
                pass
    except Exception as e:
        print(e)
        print("")
        print("------")
        print("")
        menu()


def stringToKey(value):
    acceptableCharsList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ',', '.', ' ']
    charsList = []
    key = ""
    for char in value:
        if char in acceptableCharsList and char not in charsList:
            key += char
            charsList.append(char)
    for char in acceptableCharsList:
        if char not in charsList:
            key += char
    return key


def createkey():
    print("Please enter the string to be converted to a key: ")
    try:
        enteredString = input().strip().upper()
        global currentkey
        currentkey = stringToKey(enteredString)
        print("KEY || "+currentkey)
        print("")
        print("<Press the ENTER key to continue>")
        pls_continue = input()
        menu()
    except Exception as e:
        print(e)
        print("")
        print("------")
        print("")
        createkey()


def encodefromkey():
    global currentkey
    if currentkey == "":
        print("There is no current key. Please create key before continuing")
        print("")
        print("------")
        print("")
        menu()



menu()
