"""

Assignment 2: Academic Email Validator
Scenario
The CDAC academic portal needs to validate user registration submissions so that only valid academic emails ending in .edu or .res.in are registered.

Problem Description
Write a function validate_academic_email(email) that checks if a string is a valid academic email address using a regular expression.

The email must satisfy the following syntax rules:
Username: Must consist only of lowercase letters, numbers, dots, and underscores (a-z, 0-9, ., _).
It must contain at least one character.
Separator: Must contain exactly one @ symbol.
Domain: Must consist of lowercase letters, numbers, dots, and hyphens (a-z, 0-9, ., -).
Suffix: The domain must end with either .edu or .res.in (and nothing else).
The regular expression must perform an exact match of the entire string (use boundary markers ^ and $).
The function must return True if the email matches all criteria, and False otherwise.
Example Walkthrough
print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
print(validate_academic_email("vinod@gmail.com"))          # Output: False (invalid suffix)
print(validate_academic_email("ALICE@college.edu"))        # Output: False (contains uppercase letters)
print(validate_academic_email("bob@mit.edu.com"))          # Output: False (does not end in .edu or .res.in)

"""
import re
pattern = r"^[a-z0-9._]+@[a-z0-9.-]+\.(edu|res\.in)$"

def validate_academic_email(email):
    return re.match(pattern, email) is not None

print(validate_academic_email("arham.khan@cdac.res.in"))  
print(validate_academic_email("lisa_stud12@mit.edu"))      
print(validate_academic_email("vinod@gmail.com"))           
print(validate_academic_email("ALICE@college.edu"))         
print(validate_academic_email("bob@mit.edu.com"))    