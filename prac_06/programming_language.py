"""
Module: programming_language
Author: [Your Name]
Date: [Current Date]
Description: This module defines the ProgrammingLanguage class, which represents
             a programming language with attributes such as name, typing,
             reflection support, and year of introduction. It includes methods
             to check if the language is dynamically typed and to provide a
             string representation of the language.
Estimated time: 20 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

# Check the current time here before starting.
# Start time: 11:00 AM
