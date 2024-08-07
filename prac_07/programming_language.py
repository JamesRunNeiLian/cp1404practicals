"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def __str__(self):
        """Return a user-friendly string representation of the ProgrammingLanguage."""
        return (f"{self.name} ({self.typing} Typing) - "
                f"Reflection: {self.reflection}, Pointer Arithmetic: {self.pointer_arithmetic}, "
                f"Year: {self.year}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

