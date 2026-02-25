alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
           'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n").lower()
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
    print(new_text)

encrypt(original_text=text, shift_amount=shift)