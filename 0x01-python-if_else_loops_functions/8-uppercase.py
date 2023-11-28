#!/usr/bin/python3
def uppercase(str):
    final = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            asci = ord(char) - 32
            final = final + chr(asci)
        else:
            final = final + char
    print("{}".format(final))
