import random
import time
print("\n welcome to hangman! i stole this code and am using it to learn python\n")
name = input("Enter your name here! ")  
print("Hello " + name + ", best of luck, personally I suck at hangman.")
print("You want to play?\nLets play.")
print("Loading game.")
time.sleep(1)
print("Loading game..")
time.sleep(1)
print("Loading game...")
time.sleep(1)
print("Loading game.")
time.sleep(1)
print("Loading game..")
time.sleep(1)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["fish", "stick", "naruto", "turkey", "burrito", "python"]
    word =  random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ""
def play_loop():
        global play_game
        play_game = input("sooo you wanna play again? y = yes, n = no\n")
        while play_game not in ["y", "n", "Y", "N",]:
            play_game = input("soo you wanna play again? y=yes, n=no\n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thank you for playing")
            exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 8
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try a different letter, you already asked that one before\n")
    else:
        count +=1
        if count == 1:
            time.sleep(1)
            print("  ____\n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  "_|____\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |     |\n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 8:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess." + str(limit - count) + " guesses remaining\n")
            print("The word was:", already_guessed, word)
            play_loop()
    if word == '_'*length:
        print("you got the word!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()
            