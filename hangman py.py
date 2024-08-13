import random
import time

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    print("The number of letters in word is:",length)
    already_guessed = []
    play_game = ""



def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   ___ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   ___ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "_|_\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "_|_\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


def choices():
    print("Please choose what you would like to do.")
    print("For Sigining Up Type 1\nFor Signing in Type 2 ")
    print("please enter the choice:")
    choice = int(input())
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       print("please enter the correct option")
       choices()

def getdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("game.txt",'r')
    info = f.read()
    if name in info:
          print("Name Unavailable. Please Try Again")
          return getdetails()
    f.close()
    f = open("game.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)
    f.close()
    print("Sigining Up is completed")
    choices()
    

def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("game.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            print("Welcome Back, " + name)
            main()
            hangman()
            

            
        else:
            return "Password entered is wrong"
    else:
        print("Name not found.")
        print( "Please Sign Up.")
        
        return getdetails()

print(choices())
