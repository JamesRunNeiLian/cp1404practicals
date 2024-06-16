import random

# Constants
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    # Ask the user how many quick picks they wish to generate
    quick_picks_count = int(input("How many quick picks? "))

    for i in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a single quick pick with unique numbers sorted in ascending order."""
    numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.choice(numbers)
        quick_pick.append(number)
        numbers.remove(number)

    quick_pick.sort()
    return quick_pick

main()
