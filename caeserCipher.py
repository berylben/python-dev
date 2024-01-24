alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input ("Type the shift number:\n"))

# TODO-1: create a function called 'encrypt' that takes 'text' and 'shift' as inputs
def encrypt(plainText, shiftAmount):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")

def decrypt(cipherText, shiftAmount):
    plainText = ""
    for letter in cipherText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        plainText += alphabet[newPosition]
    print(f"The dcoded text is {plainText}")    

# TODO-2: inside the 'encrypt' function, shift each letter of the 'text' forward in the alphabet by the shift amount and print the encrypted text

# TODO-3 call the encrypt function and pas in the user inputs.You should be able to test the code and encrypt the message
if direction == "encode":
    encrypt(plainText = text,shiftAmount = shift)
elif direction == "decode":
    decrypt(cipherText = text, shiftAmount = shift)