import random as rnd
attempt_list=[]
def showscore():
    if not attempt_list:
        print("There is currently no high score")
    else:
        print(f'The current best score is {min(attempt_list)} attempts')
def start_game():
    attempts = 0
    random = rnd.randint(1, 10)
    print("Hello, Welcome to the game of guess the number")
    name = input("Enter your name: ")
    wanna_play = input(f'Hi, {name}, do you want to play the guessing game?\n(Enter Yes/No): ')
    if wanna_play.lower() != 'yes':
        print("Thanks for your time... See you soon!!!")
        exit()
    else: 
        showscore()
    while wanna_play.lower() == 'yes':
        try:
            guess = int(input("Enter number between 1 and 10: "))
            if guess<1 or guess>10:
                raise ValueError("Please enter number within a range")
            attempts+=1
            if guess == random:
                attempt_list.append(attempts)
                print("You guessed it correct!!")
                print(f'You took {attempts} attempts to guess correct')
                wanna_play = input("Do you want to play more?\n(Enter Yes/No): ")
                if wanna_play.lower() != 'yes':
                    print("Good to see you again!!")
                    break
                else:
                    attempts = 0
                    random = rnd.randint(1,10)
                    showscore()
                    continue
            else:
                if guess>random:
                    print("You guessed higher")
                elif guess<random:
                    print("You guessed lower")
        except ValueError as err:
            print("That is not the valid value, Try Again!!!")
            print(err)
if __name__ == '__main__':
    start_game()