"""
To crack a monoalphabetic cipher brute force techniques won't work but it other way such as frequency analysis exist
so i will attempt to make an interactive cli table to do a visual frequency analysis like in this site
 https://www.101computing.net/frequency-analysis/
"""
def frequency_analysis(ciphertext):
    # create a dictionary of the frequency of each letter in the ciphertext
    # f.e. {'a': 0, 'b': 0, 'c': 0, ...}
    frequency = {}
    for letter in ciphertext:
        if letter.lower() in frequency:
            frequency[letter.lower()] += 1
        else:
            frequency[letter.lower()] = 1
    return frequency

def print_frequency_table(frequency):
    # print the frequency table
    print("Letter\tFrequency")
    for letter, freq in frequency.items():
        print(f"{letter}\t{freq}")

def print_frequency_table_sorted(frequency):
    # print the frequency table sorted by the frequency
    print("Letter\tFrequency")
    for letter, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}\t{freq}")

def print_frequency_table_sorted_percentage(frequency):
    # print the frequency table sorted by the frequency
    print("Letter\tFrequency")
    for letter, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}\t{freq/len(ciphertext)*100:.2f}%")

def print_frequency_table_sorted_percentage_bar_chart(frequency):
    # print the frequency table sorted by the frequency
    print("Letter\tFrequency")
    for letter, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}\t{'*'*int(freq/len(ciphertext)*100)}")

def print_frequency_table_sorted_percentage_bar_chart_with_spaces(frequency):
    # print the frequency table sorted by the frequency
    print("Letter\tFrequency")
    for letter, freq in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}\t{' '*int(10-freq/len(ciphertext)*100)}{'*'*int(freq/len(ciphertext)*100)}")

# test
ciphertext = "itssg vgksr"
frequency = frequency_analysis(ciphertext)
# print_frequency_table(frequency)
# print()

# print_frequency_table_sorted(frequency)
# print()

print_frequency_table_sorted_percentage(frequency)
print()

# print_frequency_table_sorted_percentage_bar_chart(frequency)
# print()
#
# print_frequency_table_sorted_percentage_bar_chart_with_spaces(frequency)
# print()

# now we can compare the frequency of the ciphertext with the frequency of the english language
# from https://en.wikipedia.org/wiki/Letter_frequency
# the frequency of the english language is:
# Letter	Frequency
# e	12.702%
# t	9.056%
# a	8.167%
# o	7.507%
# i	6.966%
# n	6.749%
# s	6.327%
# h	6.094%
# r	5.987%
# d	4.253%
# l	4.025%
# c	2.782%
# u	2.758%
# m	2.406%
# w	2.360%
# f	2.228%
# g	2.015%
# y	1.974%
# p	1.929%
# b	1.492%
# v	0.978%
# k	0.772%
# j	0.153%
# x	0.150%
# q	0.095%
# z	0.074%
# so we can compare the frequency of the ciphertext with the frequency of the english language
# and try to guess the key
# but first we need to sort the frequency of the ciphertext

def compare_frequency(ciphertext_frequency):
    english_frequency = {
        'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966, 'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987,
        'd': 4.253, 'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360, 'f': 2.228, 'g': 2.015, 'y': 1.974,
        'p': 1.929, 'b': 1.492, 'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095, 'z': 0.074
    }

    sorted_ciphertext_frequency = sorted(ciphertext_frequency.items(), key=lambda item: item[1], reverse=True)
    sorted_english_frequency = sorted(english_frequency.items(), key=lambda item: item[1], reverse=True)

    suggested_key = {}
    for (ciphertext_letter, _), (english_letter, _) in zip(sorted_ciphertext_frequency, sorted_english_frequency):
        suggested_key[ciphertext_letter] = english_letter

    return suggested_key

suggested_key = compare_frequency(frequency)
print(suggested_key)
