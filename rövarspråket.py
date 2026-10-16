"""Rövarspråket encoder used in the SEP400 lab."""

# Swedish names are required by the lab exercise.
# pylint: disable=non-ascii-name,non-ascii-file-name


def main():
    """Read a word and print its Rövarspråket translation."""
    word = input("Ange ord: ")
    final_word = rövarspråket(word)
    print(final_word)


def is_vowel(letter):
    """Return True if the character is a Swedish vowel."""
    return letter.upper() in "AEIOUYÅÄÖ"


def rövarspråket(word):
    """Translate text into Rövarspråket."""
    new_word = []

    for character in word:
        if character.isalpha() and not is_vowel(character):
            new_word.append(character + "o" + character.lower())
        else:
            new_word.append(character)

    return "".join(new_word)


if __name__ == "__main__":
    main()
