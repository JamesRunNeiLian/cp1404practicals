"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Dictionary of state codes and their names
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}

# Print all state codes and names neatly lined up
print("All state codes and names:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:<3} is {name}")

# Input and lookup functionality using EAFP
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()