"""
CP1404/CP5632 - Practical
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit the loop when a valid integer is entered
    except ValueError:  # Catch the ValueError exception
        print("Please enter a valid integer.")
print("Valid result is:", result)
