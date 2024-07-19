import csv
from guitar import Guitar


def main():
    filename = 'guitars.csv'

    # Load guitars from file
    guitars = load_guitars(filename)

    # Display the unsorted list
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    # Display the sorted list
    print("\nSorted Guitars (by year):")
    display_guitars(guitars)

    # Get new guitars from user
    print("\nEnter new guitars:")
    while True:
        name = input("Enter guitar name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    # Save all guitars to file
    save_guitars(filename, guitars)

    # Display updated list
    print("\nUpdated Guitars List:")
    display_guitars(guitars)



