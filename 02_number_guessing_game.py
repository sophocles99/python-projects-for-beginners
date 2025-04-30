from random import randint


def get_user_limit(limit_name: str) -> int:
    try:
        user_limit = int(input(f"Enter the {limit_name} number for the game: "))
    except ValueError:
        print("Please enter a valid number.")
    return user_limit


def get_max_and_min_numbers() -> tuple[int, int]:
    max_number = get_user_limit("maximum")
    while True:
        min_number = get_user_limit("minimum")
        if not min_number < max_number:
            print("Minimum number must be less than maximum number!")
            continue
        else:
            break
    return (min_number, max_number)


def play_game() -> None:
    min_number, max_number = get_max_and_min_numbers()
    number_to_guess = randint(min_number, max_number)

    while True:
        try:
            user_guess = int(input(f"Guess the number (between {min_number} and {max_number}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < min_number or user_guess > max_number:
            print(f"Please enter a number between {min_number} and {max_number}.")
            continue

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break


if __name__ == "__main__":
    play_game()
