"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

# Check if the score is outside the valid range
while score < 0 or score > 100:
    print("Invalid input")
    score = float(input("Enter score: "))
# Evaluate the score
if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")



