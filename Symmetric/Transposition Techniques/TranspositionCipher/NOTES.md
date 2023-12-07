# Transposition Cipher Technique
## Introduction
The Transposition Cipher is a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext. That is, the order of the units is changed (the plaintext is reordered). Mathematically a bijective function is used on the characters' positions to encrypt and an inverse function to decrypt.  
## Release
The exact release date of the Transposition Cipher is not known, but it is believed to have been used since ancient times. The Spartan military used a transposition cipher called a "scytale" as early as the 7th century BC.  
## Type and Techniques
Transposition Cipher falls under the category of Symmetric Key Cryptography. In this technique, the identity of the characters remains unchanged, but their positions are changed in the plaintext. The techniques used in Transposition Cipher include simple columnar transposition, double transposition, grille cipher, and more.  
## Strengths
- The strength of the Transposition Cipher lies in its ability to completely rearrange the order of the characters in the plaintext, making it difficult to decipher without the correct key.
- It is relatively simple to understand and implement, yet can provide a reasonable level of security for non-critical data.
- When combined with other types of ciphers (like substitution ciphers), it can significantly increase the security of the encrypted message.
## Weaknesses
- The main weakness of the Transposition Cipher is its vulnerability to frequency analysis. Since it doesn't alter the actual characters in the plaintext, a cryptanalyst can use the frequency of certain characters or groups of characters to make educated guesses about the plaintext.
- It is also vulnerable to brute force attacks, especially if the key space is small.
- If the key is lost, the data is irrecoverable.
## Python Implementation
In the provided Python implementation, the Transposition Cipher is implemented as two main functions: transpositionEncryptMessage and transpositionDecryptMessage. The encryption function works by creating a grid of characters, where the number of columns is determined by the key and filling this grid row by row with the plaintext. The ciphertext is then produced by reading the grid column by column. The decryption function works in the reverse way, filling the grid column by column and then reading the grid row by row to produce the plaintext. The implementation also includes a brute force attack function hackTransposition that tries all possible keys to decrypt a given ciphertext.