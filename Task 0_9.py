"""This function accepts a string and prints out all vowels in the string
"""


def output_vowels(word):
    vowels = []  # A list that keeps track and stores vowels found
    word.lower()
    for letter in word:
        if letter in vowels:
            continue
        elif letter == "a":
            vowels.append(letter)
        if letter in vowels:
            continue
        elif letter == "e":
            vowels.append(letter)
        if letter in vowels:
            continue
        elif letter == "i":
            vowels.append(letter)
        if letter in vowels:
            continue
        elif letter == "o":
            vowels.append(letter)
        if letter in vowels:
            continue
        elif letter == "u":
            vowels.append(letter)
    print("Vowels:", end=" ")
    for vowel in vowels:
        print(f"{vowel},", end=" ")


output_vowels("Umuzi")
