# Playing_with_Cipher
Playgrounds for learning ciphering and cryptography from basics to advanced

# What is symmetric and asymmetric cryptography?

### Symmetric Cryptography

Symmetric cryptography is a type of encryption where only one key (a secret key) is used to both encrypt
and decrypt electronic information. The entities communicating via symmetric encryption must exchange 
the key so that it can be used in the decryption process. Symmetric encryption is an old technique, 
but it is still widely used because of its speed and simplicity. Symmetric encryption is also known 
as shared key cryptography or secret key cryptography.


### Asymmetric Cryptography

Asymmetric cryptography is a type of encryption where keys come in pairs. What one key encrypts, only 
the other can decrypt. One key is public, and the other is private. The public key is used to encrypt
data sent from the sender to the receiver and is shared with everyone. The private key is used to decrypt
data on the receiver’s end and is kept secret. Asymmetric encryption is also known as public key cryptography.

# What is a cipher?

A cipher is an algorithm for performing encryption or decryption—a series of well-defined steps that
can be followed as a procedure. An alternative, less common term is encipherment. 
To encipher or encode is to convert information into cipher or code. 
In common parlance, "cipher" is synonymous with "code", as they are both a set of steps 
that encrypt a message; however, the concepts are distinct in cryptography,
especially classical cryptography.

# What is a key?

A key is a piece of information (a parameter) that determines the functional output of a cryptographic algorithm or cipher.

# What is a plaintext?

In cryptography, plaintext or cleartext is unencrypted information, as opposed to information encrypted for storage or
transmission. Cleartext usually refers to data that is transmitted or stored unencrypted "in the clear".

# What is a ciphertext?

In cryptography, ciphertext or cyphertext is the result of encryption performed on plaintext using an algorithm, called a cipher.
Ciphertext is also known as encrypted or encoded information because it contains a form of the original plaintext that is unreadable
by a human or computer without the proper cipher to decrypt it. Decryption, the inverse of encryption, is the process of turning
ciphertext into readable plaintext.

# Classical Encryption Techniques

While Transforming the plaint text into a cipher text. There are two types of classical encryption techniques.

1. Substitution Cipher
2. Transposition Cipher

## Substitution Cipher

Substitution cipher is a method of encryption by which units of plaintext are replaced with ciphertext according to a regular system;
the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth.
The receiver deciphers the text by performing the inverse substitution.

The Most common substitution ciphers are:

1. Caesar Cipher or Shift Cipher
2. Monoalphabetic Cipher
3. Polyalphabetic or Vigenere Cipher
4. homophonic substitution cipher
5. playfair cipher
6. Hill Cipher
7. Affine cipher
8. Hill cipher
9. One-time pad cipher
10. Autokey cipher

## Transposition Cipher

Transposition cipher is a method of encryption by which 
the positions held by units of plaintext (which are commonly 
characters or groups of characters) are shifted according to a regular system, 
so that the ciphertext constitutes a permutation of the plaintext.

The Most common transposition ciphers are:

1. Rail Fence Cipher
2. Row Transposition Cipher
3. simple columnar transposition cipher

# Stream Cipher

A stream cipher is a symmetric key cipher where plaintext digits are combined with a pseudorandom cipher digit stream (keystream).
In a stream cipher, each plaintext digit is encrypted one at a time with the corresponding digit of the keystream, to give a digit of the ciphertext stream.
Since encryption of each digit is dependent on the current state of the cipher, it is also known as state cipher.
In practice, a digit is typically a bit and the combining operation an exclusive-or (XOR).
Stream ciphers represent a different approach to symmetric encryption from block ciphers.

The most common stream ciphers are:

1. Vernam
2. RC4 ~ Rivest Cipher 4
3. A5/1
4. A5/2
5. A5/3
6. Salsa20

# Block Cipher

A block cipher is a method of encrypting text (to produce ciphertext) in which a cryptographic key and algorithm are applied to a block of data (for example, 64 contiguous bits) at once as a group rather than to one bit at a time.
A large amount of the high-speed encryption/decryption software that is currently in use employs block ciphers.
One of the most commonly used methods of encryption today is the block cipher algorithm, where a symmetric key algorithm is used to encrypt text in fixed-length groups of bits, called blocks.

The most common block ciphers are:

1. DES ~ Data Encryption Standard
2. 3DES ~ Triple DES
3. AES ~ Advanced Encryption Standard

