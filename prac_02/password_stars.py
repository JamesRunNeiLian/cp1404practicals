password = input(f"enter the password : ")
MINIMUM_LENGTH = 4
while len(password) < MINIMUM_LENGTH:
    print(f"your password is too short!")
    password = input(f"enter the password : ")
asterisk = "*" * len(password)
print(asterisk)