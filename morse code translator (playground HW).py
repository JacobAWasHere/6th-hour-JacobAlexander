# name : Jacob Alexander
# this is a morse code and binary code translator
#this is NOT functional yet
language = input("hello, what would you like to translate to? Binary, or Morse?")
if language == "binary":
    print("Binary code has been selected, what would you like to translate to binary?")
elif language == "morse":
    message = input("Morse code has been selected, what would you like to translate to morse? (please make it under 10 characters)")
    if "a" in message[0]:
        firstChar = "a"
        if "a" in message[1]:
            secondChar = "a"
            if "a" in message[2]:
                thirdChar = "a"
                if "a" in message[3]:
                    fourthChar = "a"
                    if "a" in message[4]:
                        fifthChar = "a"
                        if "a" in message[5]:
                            sixthChar = "a"
                            if "a" in message[6]:
                                sevenChar = "a"
                                if "a" in message[7]:
                                    eighthChar = "a"
                                    if "a" in message[8]:
                                        nineChar = "a"
                                        if "a" in message[9]:
                                            tenChar = "a"
    if "b" in message[0]:
        firstChar = "b"
        if "b" in message[1]:
            secondChar = "b"
            if "b" in message[2]:
                thirdChar = "b"
                if "b" in message[3]:
                    fourthChar = "b"
                    if "b" in message[4]:
                        fifthChar = "b"
                        if "b" in message[5]:
                            sixthChar = "b"
                            if "b" in message[6]:
                                sevenChar = "b"
                                if "b" in message[7]:
                                    eighthChar = "b"
                                    if "b" in message[8]:
                                        nineChar = "b"
                                        if "b" in message[9]:
                                            tenChar = "b"
else:
    print("this is an unrecognized language")
print(firstChar + secondChar + thirdChar + fourthChar + fifthChar + sevenChar + eighthChar + nineChar + tenChar)