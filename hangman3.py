import random
import time
#warm welcome
print("\n Hello, welcome to hangman. I suck at python so the chances of this working at 50/50 at best. Enjoy! \n")
name = input("Here you will enter your name that you would like to be addressed as: ")
print("Hello " + name + "! Okay, the options are naruto, sasuke and kakashi. lets see if you get it right!")
time.sleep(1)
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
print("Loading game...")
time.sleep(1)
print("Loading game.")
time.sleep(1)
print("Loading game..")
#here we set the parameters for the game to be executed
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["naruto", "sasuke","kakashi"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' *length
    already_guessed = []
    play_game = ""
#creating a loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("you want to play, lets play. y = yes n = no\n")
    while play_game not in ["y", "n", "Y", "N",]:
        play_game = input ("you want to play? lets play. y = yes n = no\n")
    if play_game == "y" or "Y":
        main()
    if play_game == "n" or "N":
        print("Thank you for playing! have a nice day.")
        exit()
#initializing the conditions reqiured to run the game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 8
    guess = input("This is the Hangman Word: " + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print ("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print(" You already guessed this word cuh. ")
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
            print("Wrong guess." + str(limit - count) + "guesses remaining\n")
            
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
            print("Wrong guess. " + str(limit - count) + "guesses remaining\n")
            print("the word was: ", already_guessed, word)
            if word == '_'*length:
                print("You got the word!")
                play_loop()
            elif count != limit:
                hangman()
main()
hangman()
    
    