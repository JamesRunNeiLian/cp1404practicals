"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))

    # Check if the score is outside the valid range
    while score < 0 or score > 100:
        print("Invalid input")
        score = float(input("Enter score: "))

    # Evaluate and print the result for the user's score
    result = evaluate_score(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    random_result = evaluate_score(random_score)
    print(random_result)

def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()



