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
            print('You have failed to guess the number:', random_num)

# Test Driver Code 1

# guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f'The number for the program to guess is: {random_num}')

    for num in range(start, stop + 1, 1):
        print("Number of tries left:", tries)
        print(f'The program is guessing... {num}')
        if num == random_num:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            print('The program has failed to guess the correct number.')
            return

# Test Driver Code 2

# guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f'Random number to find: {random_num}')

    while start <= stop:
        pivot = (start + stop) // 2

        if pivot == random_num:
            print(f'Found it! {pivot}')
            return
        if pivot > random_num:
            print(f'Guessing lower!')
            stop = pivot - 1
        else:
            print(f'Guessing higher!')
            start = pivot + 1

        tries -= 1
        if tries == 0:
            print('Your program failed to find the number.')
            return

# Test Driver Code 3

guess_random_num_binary(5, 0, 100)
