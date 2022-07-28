import random

def guess_random_number(tries, start, stop):
    random_num = random.randint(start, stop)

    while tries != 0:
        print('Number of tries left:', tries)
        guess = int(input(f'Guess a number between {start} and {stop}: '))
        if random_num == guess:
            print('You guessed the correct number!')
            return
        elif guess < random_num:
            print('Guess higher!')
        else:
            print('Guess lower!')
        
        tries -= 1
        if tries == 0:
            print('You have faile dto guess the number:', random_num)

# Test Driver Code 1

# guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f'The number for the program to guess is: {random_num}')

    for x in range(start, stop + 1, 1):
        print(f'The program is guessing... {x}')
        if x == random_num:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            print('The program has failed to guess the correct number.')
            return
        print("Number of tries left:", tries)

# Test Driver Code 2

# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f'The number for the program to guess is: {random_num}')

    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_num:
            print(f'Found it! {pivot}')
            return
        if pivot > random_num:
            print(f'Guessing lower!')
            upper_bound = pivot - 1
        else:
            print(f'Guessing higher!')
            lower_bound = pivot + 1

        tries -= 1
        if tries == 0:
            print('Your program failed to find the number.')
            return

# Test Driver Code 3

guess_random_num_binary(5, 0, 100)
