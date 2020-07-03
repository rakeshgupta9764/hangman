import random

print("H A N G M A N")
option = input('Type "play" to play the game, "exit" to quit:')
options = ['python', 'java', 'kotlin', 'javascript']
chances = 8

random.seed()
ans = random.choice(options)
unique_letters = set(ans)


def state(string, guessed_letters):
    output_string = ""
    for char in string:
        if char in guessed_letters:
            output_string += char
        else:
            output_string += '-'
    return output_string

guessed_letters = []
already_typed = []
while option == "play":
    while chances != 0:
        output_string = state(ans, guessed_letters)
        if '-' not in output_string:
            break
        
        print()
        print(output_string)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not ord('a') <= ord(letter) <= ord('z'):
            print("It is not an ASCII lowercase letter")
        elif letter in unique_letters:
            if letter in already_typed:
                print("You already typed this letter")
            else:
                guessed_letters.append(letter)
                already_typed.append(letter)
        else:
            if letter not in already_typed:
                print("No such letter in the word")
                already_typed.append(letter)
                chances -= 1
            else:
                print("You already typed this letter")

    if chances == 0:
        print("You are hanged!")
    else:
        print("You guessed the word " + ans + "!")
        print("You survived!")
    option = input('Type "play" to play the game, "exit" to quit:')
