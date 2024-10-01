import random as rd

for i in range(5):  #5 chances are given to the user to make a guess

    try:

        user_guess=int(input('Guess a number between 1 to 10: '))
        computer_input=rd.randint(1,10)
        print('Computer entered: ', computer_input)

        if user_guess>=1 and user_guess<=10:


            if user_guess==computer_input:
                print('Congratulation you won')
                break


            else:
                print('You lost, try again')
                print('\n')

        else:
            print('Enter a number between 1-10')
    
    except ValueError:
        print('Enter number')

if user_guess!=computer_input:
    print('Better luck next time')