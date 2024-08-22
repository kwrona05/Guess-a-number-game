import random

def guess():

    levels = [
        {"min": 1, "max": 10},
        {"min": 1, "max": 20},
        {"min": 1, "max": 50},
        {"min": 1, "max": 75},
        {"min": 1, "max": 100}
    ]

    Red = "\033[91m"
    Green = "\033[92m"
    Yellow = "\033[93m"
    Reset = "\033[0m"

    for i, level in enumerate(levels, start=1):
        min_value = level["min"]
        max_value = level["max"]
        number_to_guess = random.randint(min_value, max_value)

        print(f'{Yellow}Level {i}: Guess the number between {min_value} and {max_value}{Reset}')

        your_number = None

        while your_number != number_to_guess:
            try:
                your_number = int(input(f'{Yellow}Try to guess the number between {min_value} and {max_value}:{Reset} '))
            except ValueError:
                print(f'{Red}Enter a valid number{Reset}')
                continue
            
            if your_number < number_to_guess:
                print(f'{Red}Too low{Reset}')
            elif your_number > number_to_guess:
                print(f'{Red}Too high{Reset}')
            else:
                print(f'{Green}Congrats! You passed level {i}{Reset}')
    print(f'{Green}Wow! You are master! You passed all levels!{Reset}')

guess()