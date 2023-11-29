import itertools
import string


def vigenere_encrypt(plain_text, key):
    # initialize result string and key length
    # key length is used to determine the shift for each character in the plaintext
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        # Iterate through each character in the plaintext
        char = plain_text[i]
        if char.isalpha():
            # Determine the shift for the current character based on the keyword
            # the shift is calculated by taking the ASCII value of the current character in the keyword
            # and subtracting 97 (the ASCII value of 'a'). This gives us a value between 0-25.
            # This value is used to shift the current character in the plaintext. The modulo operator (%) is used
            # to ensure that the shifted character remains in the range of uppercase characters. ord() returns the
            # ASCII value of a character. chr() returns the character represented by an ASCII value. P.S shift can be -
            shift = ord(key[i % key_length].lower()) - 97

            if char.isupper():
                # If the current character is uppercase, we subtract 65 (the ASCII value of 'A') to get a value
                # between 0-25, add the shift amount and then take the result modulo 26. This ensures that the
                # result stays between 0-25. We then add 65 to the result to get the correct ASCII value for the
                # encrypted character. We then convert the ASCII value to a character and append it to the result
                # string.
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    # The decryption process is the same as the encryption process except that we subtract the shift amount
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - 97

            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char

    return decrypted_text

def brute_force_vigenere_decrypt(encrypted_text, max_key_length=10):
    # Brute force decryption is the process of trying every possible decryption key for a ciphertext.
    # The maximum key length is set to 10 by default. This can be changed by passing a different value to the
    # max_key_length parameter.
    generated_keys = 0
    for key_length in range(1, max_key_length + 1):
        # Try every possible key length from 1 to max_key_length
        # itertools.product() returns the cartesian product of the given iterables. This is used to generate
        # every possible combination of uppercase letters of length key_length.
        # For example, itertools.product('ABC', repeat=2) returns: AA AB AC BA BB BC CA CB CC
        # The cartesian product is used to generate every possible key of length key_length.
        # The key is then used to decrypt the ciphertext. If the decrypted text matches the user input, we have
        # successfully decrypted the ciphertext.
        for possible_key in itertools.product(string.ascii_uppercase, repeat=key_length):
            generated_keys += 1

            key = ''.join(possible_key)
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            print(f"Key: {key}, Decrypted Text: {decrypted_text}")
            if user_input == decrypted_text:
                print("Decryption successful!")
                print(f"Generated {generated_keys} keys")
                return


# Example
user_input = input("Enter a string to encrypt: ")
keyword = input("Enter a keyword: ")

encrypted_string = vigenere_encrypt(user_input, keyword)
print("Encrypted string:", encrypted_string)

decrypted_string = vigenere_decrypt(encrypted_string, keyword)
print("Decrypted string:", decrypted_string)

print("\nAttempting to break the Vigenère Cipher:")
brute_force_vigenere_decrypt(encrypted_string)
