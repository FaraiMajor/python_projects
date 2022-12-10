# Caesar Cipher
import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    word = ''
    for i in text:
        # index = alphabet.index(i) + shift
        index = ord(i) - ord('a') + shift
        word += (string.ascii_letters[index % len(string.ascii_letters)])
    print(word)


def decrpyt(text, shift):
    word = ''
    for i in text:
        index = ord(i) - ord('a') - shift
        word += (string.ascii_letters[index % len(string.ascii_letters)])
    print(word)


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrpyt(text, shift)
else:
    pass
