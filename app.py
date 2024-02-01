# number guessing game !

from random import randint

# function to get the guess from the  user
def get_user_guess() :
    while True :
        try :
            guess = int(input("enter your guess : "))
            break
        except ValueError :
            print("it should be a number !")
            continue
    return guess

# function to get the top of range from the user
def get_top_of_range() :
    while True :
        try :
            top_of_range = int(input("please enter the top of range (minimum 10) : "))
            if top_of_range < 10 :
              print("it should be higher than 10!")
              continue
            break
        except ValueError :
            print("it should be a number!")
            continue
    return top_of_range

# function to check the user guess if it's correct or no
def check_user_guess( number_guessed , max_range , rand_number ) :
    while True :
        if number_guessed > max_range :
           print("respect the range !")
           number_guessed = get_user_guess()
           continue
        if number_guessed > rand_number :
           print("too high")
           number_guessed = get_user_guess()
           continue
        if number_guessed < rand_number :
           print("too low")
           number_guessed = get_user_guess()
           continue
        if number_guessed == rand_number :
           print("that's correct !")
           break

#getting the top of range from the user
max_range = get_top_of_range()

# function that generate a random number
def generating_random_number (max_range) :
    random_number = randint(0 , max_range)
    return rand_number

#generating the random number
rand_number = generating_random_number(max_range)

#getting the guess from the user
number_guessed = get_user_guess()

#checking the user guess 
check_user_guess(number_guessed , max_range , rand_number)


