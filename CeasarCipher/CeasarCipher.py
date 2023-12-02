"""DIFFUCLTY = Easy"""
def encrypt(text, shift):
    # initialize result string
    result = ""
    for char in text:
        # Shift uppercase characters by shift amount using ASCII values. 65 is the ASCII value of 'A'
        # and 90 is the ASCII value of 'Z'. The modulo operator (%) is used to ensure that the shifted
        # character remains in the range of uppercase characters. ord() returns the ASCII value of a character.
        # chr() returns the character represented by an ASCII value. P.S shift can be negative.
        if char.isalpha():
            if char.isupper():
                # f.e if char is 'A' and shift is 3, then ord(char) + shift - 65 = 65 + 3 - 65 = 3
                # 3 % 26 = 3, chr(3 + 65) = chr(68) = 'D'. The % 26 ensures that the value wraps around
                # the alphabet if the shift is greater than 26.
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    # To decrypt the ciphertext, we make a call to the encrypt function with a negative shift.
    return encrypt(ciphertext, -shift)

def brute_force_decrypt(ciphertext):
    # Brute force decryption is the process of trying every possible decryption key for a ciphertext.
    for shift in range(26):
        # Try every possible shift value in the range of 0-25. until the user input is found.
        decrypted_text = decrypt(ciphertext, shift)\
        # Uncomment the line below if you want to see the brute force attempts .
        # print(f"Shift {shift}: {decrypted_text}")
        if user_input == decrypted_text:
            print(f"Shift {shift}: {decrypted_text}")
            break

# Example
user_input = input("Enter a string to encrypt: ")
shift_amount = int(input("Enter a shift degree: "))

encrypted_string = encrypt(user_input, shift_amount)
print("Encrypted string:", encrypted_string)

print("\nAttempting to break the encryption:")
brute_force_decrypt(encrypted_string)
