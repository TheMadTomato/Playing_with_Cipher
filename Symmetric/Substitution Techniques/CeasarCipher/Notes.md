# Ceasar Cipher

## Description
The Ceasar Cipher is a simple encryption technique that shifts each letter in a message by a fixed number of positions 
down the alphabet. For example, if the shift is 3, then the letter A would be replaced by D, B would become E, and so on. 
The method is named after Julius Caesar, who apparently used it to communicate with his generals.

The shifts in this method are cyclical, meaning that when you reach the end of the alphabet, the next letter is the
beginning of the alphabet. For example, if the shift is 3, then the letter X would become A, Y would become B, and Z would
become C.

It is possible to use keys or shifts from only 0 to 25. Also it is worth noting that encrypting the same text twice with the
different keys may sound like a good idea, but it is not. In reality you would just be using different key value on the same string 
even if encrypted.

The decryption is done by shifting the letters in the opposite direction, so if the shift is 3, then the letter D would be
replaced by A, E would become B, and so on.

In terms of brute forcing the cipher, it is quite easy to do so. There are only 25 possible keys, so it is possible to try
all of them and see which one gives the most readable output. However, this is not always the case. If the key is unknown,
then it is possible to use frequency analysis to determine the key. This is done by counting the frequency of each letter in
the ciphertext and comparing it to the frequency of each letter in the English language. The most common letter in the
ciphertext is likely to be E, the second most common is likely to be T, and so on. This is not always the case, but it is
a good starting point.

## Difficulty

Easy (level 1)


