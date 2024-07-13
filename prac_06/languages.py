"""
Module: languages
Author: [James Run Nei Lian]
Date: [13.7.2024]
Estimated time: 30 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
print(ruby)
print(visual_basic)

languages = [python, ruby, visual_basic]

# Loop through and print the names of all dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)

# Check the current time here after finishing.
# End time: 11:30 AM
