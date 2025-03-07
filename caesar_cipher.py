from caesar_cipher_logo import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print (logo)

def caesar(direction_provided, original_text, shift_amount):
    
    output_text = ""
    if direction_provided == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"here is your {direction_provided}d text {output_text}")

should_continue = True

while should_continue:

    direction = input("type 'encode' to encrypt a message or 'decode' to decrypt a message:\n")
    message = input("enter your message here:\n").lower()
    shift = int(input("enter by what number you want to shift your message:\n"))

    caesar(direction, message, shift)

    restart = input("do you want to restart the program? 'yes' 'no' \n")
    if restart == "no":
        print("Goodbye!")










