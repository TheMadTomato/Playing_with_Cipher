# Vigenère Cipher
## Introduction
The Vigenère Cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution, which means it uses multiple substitution alphabets to encrypt the text. The use of multiple alphabets makes the Vigenère Cipher significantly more difficult to crack than a simple Caesar Cipher.  
## Release
The Vigenère Cipher was described by Giovan Battista Bellaso in his 1553 book "La cifra del. Sig. Giovan Battista Bellaso". However, the cipher is often attributed to Blaise de Vigenère, who published a similar autokey cipher in 1586.  
## Type and Techniques
Vigenère Cipher falls under the category of Polygraphic Substitution Cipher, which is a part of Symmetric Key Cryptography. In this technique, the identity of the characters is changed based on a keyword, while their positions remain the same. The technique used in Vigenère Cipher is a series of Caesar ciphers.  
## Strengths
The strength of the Vigenère Cipher lies in its use of multiple substitution alphabets, which makes it resistant to frequency analysis attacks.
It is relatively simple to understand and implement, yet provides a higher level of security than simple substitution ciphers.
## Weaknesses
The main weakness of the Vigenère Cipher is its repetition of the keyword. If the length of the keyword can be determined, the cipher can be broken by grouping the ciphertext into clusters and performing frequency analysis on each cluster.
It is also vulnerable to Kasiski examination and Friedman test, which are methods used to determine the length of the keyword.
## Python Implementation
In the provided Python implementation, the Vigenère Cipher is implemented as two main functions: vigenere_encrypt and vigenere_decrypt. The vigenere_encrypt function works by shifting each character in the plaintext by a number of positions down the alphabet based on the corresponding character in the keyword. The vigenere_decrypt function works by shifting the characters in the opposite direction. The implementation also includes a brute_force_vigenere_decrypt function that tries all possible keys up to a certain length to decrypt a given ciphertext.