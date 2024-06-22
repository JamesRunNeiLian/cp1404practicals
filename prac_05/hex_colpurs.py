COLOUR_TO_HEX = {"Absolute Zero": "#0048ba",
                 "Ancid Green": "#b0bf1a",
                 "Alice Blue": "#f0f8ff",
                 "Alizarin Crimson": "#e32636",
                 "Amaranth": "#e52b50",
                 "Amber": "#ffbf00",
                 "Aqua": "#00ffff",
                 "Army Green": "#4b5320",
                 "Ash Grey": "#b2beb5",
                 "Aureolin": "#fdee00"}

# Calculate maximum lengths for formatting
maximum_length_name = max(len(name) for name in COLOUR_TO_HEX)
maximum_length_code = max(len(code) for code in COLOUR_TO_HEX.values())

# Print all colour names and their codes
print("Available colour names and their codes:")
for name, code in COLOUR_TO_HEX.items():
    print(f"{name:<{maximum_length_name}} is {code:>{maximum_length_code}}")

# Input and lookup functionality using EAFP
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name:<{maximum_length_name}} is {COLOUR_TO_HEX[colour_name]:>{maximum_length_code}}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
