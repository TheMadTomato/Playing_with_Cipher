# Transposition Cipher Encryption
import pyperclip
import math

def transpositionEncryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
    # print(ciphertext)
    # print("len(message): ", len(message))
    # Loop through each column in ciphertext.
    for col in range(key):
        pointer = col
        # print("pointer: ", pointer)
        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the current column in the ciphertext list.
            ciphertext[col] += message[pointer]
            # move pointer over
            # print(ciphertext)
            pointer += key
    # print(ciphertext)
    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)

def transpositionDecryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and "rows" of the grid that the plaintext is written
    # on by using a list of strings. First, we need to calculate a few values.
    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # print("len(message):", len(message), "\tKey:", key)
    # print("numOfColumns: ", numOfColumns)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # print("numOfRows: ", numOfRows)
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # print("numOfShadedBoxes: ", numOfShadedBoxes)
    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns
    # print(plaintext)
    # The col and row variables point to where in the grid the next character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column
        # print(plaintext)
        # If there are no more columns OR we're at a shaded box, go back to the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

# print(transpositionEncryptMessage(8, "Common sense is not so common."))
#
# print(transpositionDecryptMessage(8, "Cenoonommstmme oo snnio. s s c"))

