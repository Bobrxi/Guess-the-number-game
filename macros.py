import time
import random
ran_num = random.randint(1, 99)

value = False

while value == False:
    user_input = int(input("Choose random number from 1 to 100: "))
    if user_input == ran_num:
        print('You have guessed the right number:', ran_num)
        value = True
        second_game = input("Wanna play another one?: ")
        if second_game == 'yes':
            value = False
            ran_num = random.randint(1, 99)
    elif user_input <= ran_num:
        print('Incorrect number, try a greater one!')

    elif user_input >= ran_num:
        print('Incorrect number, try a lower one! ')

time.sleep(1)
