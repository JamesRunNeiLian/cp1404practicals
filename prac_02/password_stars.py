def main():
    password = get_password()
    asterisk = print_asterisk(password)  # Pass the password to print_asterisk
    print(asterisk)  # Print the asterisks

def get_password():
    MINIMUM_LENGTH = 4
    password = input("Enter the password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Your password is too short!")
        password = input("Enter the password: ")
    return password  # Return the valid password

def print_asterisk(password):
    asterisk = "*" * len(password)
    return asterisk

main()




