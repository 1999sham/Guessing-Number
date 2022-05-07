#importing the Random and Datetime Modules
import random
import datetime as dt
#Writing the Guessingno fun in that all the main stuff is present
def Guessingno():
    Name = input('ENTER YOUR NAME:')
    Sex = input('ENTER YOUR GENDER:')
    Age = int(input('ENTER YOUR AGE:'))
    # Getting choice on play game from the user
    choice = input('HELLO '+ Name.upper() +' ARE YOU READY NOW?')
    if choice.upper() == 'YES':
        print('''OK THATS !!! GREAT\n
        ____________________\n
        ____________________\n
        ____________________''')
        #using the Random module method randrange to generate a random number
        Guessno = random.randrange(1,50)
        print('HEY '+ Name.upper() +' YOU HAVE FIVE CHANCES TO GUESS THE NUMBER IF YOU NOT GUESSED CORRECTLY THE GAME WILL BE ENDED.')
        print('HEY '+ Name.upper() + ' WE ARE GIVING A GAME STARTED POINTS TO YOU I.E IS 10')
        # using a while loop for the chances
        points = 10
        i = 1
        while i<=5:
            userguessing = int(input('HEY!! '+ Name.upper() +' GUESS THE NUMBER IN BETWEEN 1 AND 50:'))
            # checking the condition
            if userguessing == Guessno:
                print('HEY!! '+ Name.upper() +' HURRY YOU GUESSED CORRECTLY.')
                points = points + 5
                print('YOUR SCORE IS ',points)
                break
            else:
                print('HEY!!! '+ Name.upper() +' HOOO YOUR GUESS IS WRONG.')
                points = points - 1
                print('YOUR SCORE IS ',points)
                if i == 4:
                    print('HEY '+ Name.upper() +' YOU HAVE ONLY ONE CHANCE TO GUESS THE NUMBER.')
                    Hint = input('IF YOU WANT HINT THEN YOU HAVE TO PAY 5 POINTS.')
                    if Hint == 'yes' or 'Yes':
                        points = points - 5
                        print('THE HINT IS THE GUESSNO IS',Guessno*5,'MULTIPLE OF 5')
                        print('AFTER DEDICTING THE POINTS FOR THE HINT THE SCORE IS ',points)
                    else:
                        print('OK THATS GREAT BETTER LUCK NEXT TIME!!!!!')
            i = i + 1

    else:
        print('OK PLAY THE GAME AFTER SOMETIME ')

# knowing the interest of the user to play the game or not
while True:
    x = dt.datetime.now()
    print('NOW THE TIME IS ',x)
    print('WELCOME TO THE GUESSING NUMBER GAME!!!!')
    choice = input('ARE YOU READY TO PLAY THE GAME?')
    if choice.upper() == 'YES':
        Guessingno()
    elif choice.upper() == 'NO':
        break



