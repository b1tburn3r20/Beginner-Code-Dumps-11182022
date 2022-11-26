import random
import time
print("\n welcome to hangman! your moms a dude\n")
name = input("enter your name here! ")
time.sleep(1)
print("Hello " + name + ", best of luck, personally I suck at this game.")
time.sleep(1)
print("You want to play?\n lets play.")
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
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["fish","bird","shark","snake","owl"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'*length
    already_guessed = []
    play_game = ""
def play_loop():
        global play_game
        play_game = input("You want to play? lets play. y=yes, n = no\n")
        while play_game not in ["y", "n", "Y", "N"]:
            play_game = input("You want to play? lets play. y=yes, n=no\n")
        if play_game == "y" or "Y":
            main()
        elif play_game == "n" or "N":
            print("Thanks for playing")
            time.sleep(2)
            exit()
def hangman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit = 5
        guess = input("This is the word: " + display + " Enter your guess: \n")
        guess = guess.strip()
        if len(guess.strip()) == 0 or len(guess.strip()) >- 2 or guess <= "9":
            print("Invalid Input, try a letter\n")
            hangman()
        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index+1:]
            display = display[:index] + guess + display[index + 1:]
            print (display + "\n")
        elif guess in already_guessed:
            print ("You did this letter already\n")
        else:
            count +1
            if count == 1:
                time.sleep(1)
                print("D")
                print("INCORRECT ") + str(limit - count)+" guesses remaining\n"
            if count == 2:
                time.sleep(1)
                print ("DE")
                print("INCORRECT ") + str(limit - count)+" guesses remaining\n"
            if count == 3:
                time.sleep(1)
                print("DEA")
                print("INCORRECT ") + str(limit - count)+" guesses remaining\n"
            if count == 4:
                time.sleep(1)
                print("DEAT")
                print("INCORRECT ") + str(limit - count)+" guesses remaining\n"
            if count == 5:
                time.sleep(1)
                print("DEATH")
                print("INCORRECT ") + str(limit - count)+" guesses remaining\n"
                play_loop()
    if word == '_'*length:
        print("you got the word!!")
        play_loop()
elif count != limit:
        hangman()
main()
hangman()