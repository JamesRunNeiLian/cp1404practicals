"""
Module: guitar
Author: [Your Name]
Date: [Current Date]
Description: This module defines the Guitar class, which represents a guitar with attributes
             such as name, year, and cost. It includes methods to get the age of the guitar,
             check if it is vintage, and provide a string representation of the guitar.
Estimated time: 25 minutes
"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

# Check the current time here before starting.
# Start time: 12:00 PM
