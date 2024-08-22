import random

def guess():

    levels = [
        {"min": 1, "max": 10},
        {"min": 1, "max": 20},
        {"min": 1, "max": 50},
        {"min": 1, "max": 75},
        {"min": 1, "max": 100}
    ]

    for i, level in enumerate(levels, start=1):
        min_value = level["min"]
        max_value = level["max"]
        number_to_guess = random.randint(min_value, max_value)

        print(f'Level {i}: Guess the number between {min_value} and {max_value}')

        your_number = None

        while your_number != number_to_guess:
            try:
                your_number = int(input(f'Try to guess the number between {min_value} and {max_value}: '))
            except ValueError:
                print('Enter a valid number')
                continue
            
            if your_number < number_to_guess:
                print('Too low')
            elif your_number > number_to_guess:
                print('Too high')
            else:
                print(f'Congrats! You passed level {i}')
    print('Wow! You are master! You passed all levels!')

guess()