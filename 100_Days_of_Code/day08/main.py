# Caesar Cipher
import string
import arts as art


print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def replay():
    res = input(
        "Do you want to play again? Enter 'Y' for Yes or 'N' for No: ").lower()

    if res == 'y':
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print('GAME OVER, Hope you had fun')
        print(art.over)


def caesar(text, shift, direction):

    final_word = ''
    if direction == 'encode':
        for char in text:
            # index = alphabet.index(char) + shift
            index = ord(char) - ord('a') + shift
            final_word += (string.ascii_letters[index %
                           len(string.ascii_letters)])

    elif direction == 'decode':
        for char in text:
            index = ord(char) - ord('a') - shift
            final_word += (string.ascii_letters[index %
                           len(string.ascii_letters)])
    else:
        pass

    print(final_word)
    replay()


caesar(text, shift, direction)
