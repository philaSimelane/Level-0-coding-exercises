"""This function takes two strings as input and outputs common characters they share
"""


def common_characters(word1, word2):
    character_store = []  # A list to keep track and store common characters
    print("Common letters: ", end="")
    for character in word1:
        if character in character_store:
            continue
        elif character in word2:
            character_store.append(character)
    for letters in character_store:
        print(f"{letters},", end="")


common_characters("girl", "world")
