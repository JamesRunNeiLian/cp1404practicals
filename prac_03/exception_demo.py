"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("The denominator cannot be zero.")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#A ValueError will occur if the user inputs something that cannot be converted to an integer.
#A ZeroDivisionError will occur if the user inputs 0 as the denominator.
#Yes, we can modify the code to explicitly check if the denominator is zero before attempting the division.