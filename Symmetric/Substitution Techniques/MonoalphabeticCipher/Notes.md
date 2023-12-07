# Monoalphabetic Cipher

## Introduction

The Monoalphabetic Cipher, also known as the simple substitution cipher, is a method of encryption where each letter in the plaintext is replaced by a letter in the ciphertext using a predetermined substitution. The substitution is defined by a key, which can be any permutation of the alphabet. This means that the order of the units is changed (the plaintext is reordered).
## Release
The exact release date of the Monoalphabetic Cipher is not known, but it is believed to have been used since ancient times.  
## Type and Techniques
Monoalphabetic Cipher falls under the category of Substitution Cipher, which is a part of Symmetric Key Cryptography. In this technique, the identity of the characters is changed while their positions remain the same. The technique used in Monoalphabetic Cipher is a simple substitution of characters.
## Algorithm

The algorithm for the encryption of a letter x is given by:

```
E(x) = (x + k) mod 26
```

where k is the key. The decryption algorithm is given by:

```
D(x) = (x - k) mod 26
```

## Example

### Encryption

```
Plaintext:  ATTACKATONCE
Key:        3
Ciphertext: DWWDFNDQFRGH
```

### Decryption

```
Ciphertext: DWWDFNDQFRGH
Key:        3
Plaintext:  ATTACKATONCE
```
## Strengths
The strength of the Monoalphabetic Cipher lies in its larger key space compared to the Caesar Cipher. While Caesar Ciphers have a key space of 26, Monoalphabetic Ciphers have a key space of 26! (factorial), which is approximately 4 x 10^26. This makes it less prone to brute force attacks.
It is relatively simple to understand and implement.
## Weaknesses
The main weakness of the Monoalphabetic Cipher is its vulnerability to frequency analysis. Since each letter in the plaintext is replaced by the same letter in the ciphertext, the frequency of each letter in the ciphertext is the same as the frequency of each letter in the plaintext. This means that a cryptanalyst can use the frequency of certain characters to make educated guesses about the plaintext.
If the key is lost, the data is irrecoverable.
## Python Implementation
In the provided Python implementation, the Monoalphabetic Cipher is implemented as two main functions: encrypt and decrypt. The encrypt function works by replacing each character in the plaintext with the corresponding character from the key. The decrypt function works by replacing each character in the ciphertext with the corresponding character from the key. The implementation also includes a brute_force_decrypt function that tries all possible keys to decrypt a given ciphertext.
## Frequency Analysis

![](/home/poro/Pictures/frequency-analysis-english-language.png)
Because of the nature of the English language, certain letters are more common than others.
So in a monoalphabetic cipher, the most common letter in the ciphertext will be the most common letter in the plaintext.
This means that we can use frequency analysis to break the monoalphabetic cipher. Tho it is worth noting that frequency
analysis is not always successful especially if the ciphered text is too short or if the text is not in English.