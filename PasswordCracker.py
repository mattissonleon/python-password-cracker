import itertools
import string
import time

target = "Password" #Password to be cracked

charset_lowercase = string.ascii_lowercase
charset_uppercase = string.ascii_uppercase
charset_letters = string.ascii_lowercase + string.ascii_uppercase
charset_numbers = string.digits
charset_lettersAndNumbers = string.ascii_lowercase + string.ascii_uppercase + string.digits
charset_full = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

attempts = 0
cracked = False
repeats = 1

def bruteForce(charset):
    global attempts, cracked, repeats

    for attempt in itertools.product(charset, repeat = repeats):
        guess = "".join(attempt)
        attempts += 1

        print(f"Chars: {repeats} Attempts: {attempts} Trying: {guess}")

        if guess == target:
            cracked = True
            print(f"Password was: {guess}")
            print(f"Found in {attempts} attempts")
            print(f"Took {time.time() - start:.2f} seconds")
            break

    if not cracked:
        repeats += 1
        bruteForce(charset)

cracking_methods = [
        "BruteForce"
    ]

def option_selection(question: str, options: list):
    print(question)
    print("")
    
    for option in options:
        print(option)

    print("")

    while True:
        choice = input("Select one of the options listed above: ")

        if choice in options:
            return choice

        else:
            print("Invalid choice")

print("")
attack_input = option_selection("What cracking method would you like to use?", cracking_methods)

if attack_input == "BruteForce":
    charsets = [
        "Lowercase",
        "Uppercase",
        "Letters",
        "Numbers",
        "LettersAndNumbers",
        "Full"
    ]

    print("")
    charset_input = option_selection("What charset would you like to use?", charsets)

    if charset_input == "Lowercase":
        charset = charset_lowercase
    elif charset_input == "Uppercase":
        charset = charset_uppercase
    elif charset_input == "Letters":
        charset = charset_letters
    elif charset_input == "Numbers":
        charset = charset_numbers
    elif charset_input == "LettersAndNumbers":
        charset = charset_lettersAndNumbers
    elif charset_input == "Full":
        charset = charset_full

    start = time.time()
    bruteForce(charset)