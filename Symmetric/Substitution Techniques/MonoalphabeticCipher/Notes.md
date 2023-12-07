# Monoalphabetic Cipher

## Description

The monoalphabetic cipher, also known as simple substitution cipher, is a substitution cipher where each letter in the plaintext is replaced by a letter in the ciphertext.
For example, if the key to the cipher is 3, then we replace the letter A by D, B by E, C by F, and so on.

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

Monoalphabetic ciphers are better than Caesar ciphers because they have a larger key space. While ceasar ciphers have a key space of 26, monoalphabetic ciphers have a key space of 26! (factorial).
26! is approximately 4 x 10^26, which is a very large number. It is not prone to brute force attack.
## Vulnerabilities

The monoalphabetic cipher is a very weak cipher because it is vulnerable to frequency analysis.
This is because each letter in the plaintext is replaced by the same letter in the ciphertext.
This means that the frequency of each letter in the ciphertext is the same as the frequency of each letter in the plaintext.
For example, if the letter E is the most common letter in the plaintext, then the letter E will be the most common letter in the ciphertext.

### Frequency Analysis

![](/home/poro/Pictures/frequency-analysis-english-language.png)
Because of the nature of the English language, certain letters are more common than others.
So in a monoalphabetic cipher, the most common letter in the ciphertext will be the most common letter in the plaintext.
This means that we can use frequency analysis to break the monoalphabetic cipher. Tho it is worth noting that frequency
analysis is not always successful especially if the ciphered text is too short or if the text is not in English.