class MonoAlohabeticCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.cipher = self.generate_cipher()

    def generate_cipher(self):
        # Generate a dictionary for the cipher
        # f.e. {'a': 'q', 'b': 'w', 'c': 'e', ...}
        cipher = {}
        for i in range(len(self.alphabet)):
            cipher[self.alphabet[i]] = self.key[i]
        return cipher
    def encrypt(self, plaintext):
        # for each letter in the plaintext check if it is alohabet list
        # then change the it's value by checking the value of the key in the cipher dictionary
        ciphertext = ""
        for letter in plaintext:
            if letter.lower() in self.alphabet:
                ciphertext += self.cipher[letter.lower()]
            else:
                ciphertext += letter
        return ciphertext
    def decrypt(self, ciphertext):
        # with the key agreed upon the cipher dict will be the same but instad of adding the values together
        # we add the keys
        plaintext = ""
        for letter in ciphertext:
            for key, value in self.cipher.items():
                if letter == value:
                    plaintext += key
        return plaintext
# test
plaintext = "hello world"

# key should consist of 26 character hence the following try except loop
# example key = "qwertyuiopasdfghjklzxcvbnm"
while True:
    try:
        key = input("Enter the key: ")
        if len(key) == 26:
            break
        else:
            print("invalid key. Length is to be equal to 26 char")
    except:
        print("invalid key. Length is to be equal to 26 char")
cipher = MonoAlohabeticCipher(key)
encrypted = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(encrypted)

print(encrypted)
print(decrypted)