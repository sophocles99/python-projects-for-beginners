from random import randint


def get_number_of_dice() -> int:
    while True:
        number_of_dice_input = input("How many dice would you like to play with? (enter a number): ")
        try:
            number_of_dice = int(number_of_dice_input)
        except ValueError:
            print("Invalid number!")

        if number_of_dice < 1:
            print("You must play with at least one die!")
        else:
            break

    return number_of_dice


def get_dice_roll(number_of_dice) -> tuple[int, ...]:
    return tuple(randint(1, 6) for _ in range(number_of_dice))


def play_game() -> None:
    number_of_dice = get_number_of_dice()
    number_of_rolls = 0

    while True:
        user_input = input("Roll the dice? (y/n): ").strip().lower()
        if user_input == "y":
            print(get_dice_roll(number_of_dice))
            number_of_rolls += 1
        elif user_input == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
            continue

    print(f'You rolled the dice {number_of_rolls} time{"" if number_of_rolls == 1 else "s"}')


if __name__ == "__main__":
    play_game()
