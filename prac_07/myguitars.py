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


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Ensure the row is not empty
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save the list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
