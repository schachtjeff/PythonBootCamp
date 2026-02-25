alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    new_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet):
                new_position = new_position - len(alphabet)
            new_text += alphabet[new_position]
    print(f"Your cipher text: {new_text}")

def decrypt(original_text, shift_amount):
    new_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position - shift_amount
            #if new_position < 0:
            #    new_position = new_position - len(alphabet)
            new_text += alphabet[new_position]
    print(f"Your cipher text: {new_text}")

def caesar(direction, text, shift):
    if direction == 'decode':
        decrypt(original_text=text, shift_amount=shift)
    elif direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    else:
        print("I have no idea what you are talking about!!")

caesar(direction=direction, text=text, shift=shift)