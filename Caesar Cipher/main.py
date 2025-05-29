import art
print(art.logo)
# TODO-1: Import and print the logo from art.py when the program starts.



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(final_direction, original_text, shift_amount):
    final_text = ""
    overlap = 0
    original_text = original_text.lower()
    if final_direction == "encode":
        for letter in original_text:
            if letter in alphabet:
                current_position = alphabet.index(letter)
                new_position = (current_position + shift_amount) % 26
                letter = alphabet[new_position]
            final_text += letter
        print(final_text)
    elif final_direction == "decode":
        for letter in original_text:
            if letter in alphabet:
                current_position = alphabet.index(letter)
                new_position = (current_position - shift_amount) % 26
                letter = alphabet[new_position]
            final_text += letter
        print(final_text)
    else:
        print("You did not type encode or decode. Restart the program")


play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(final_direction=direction, original_text=text, shift_amount=shift)

    answer = input("Do you want to play again? Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if answer != "yes":
        play_again = False
        print("Goodbye!")


# TODO-3: Can you figure out a way to restart the cipher program?







