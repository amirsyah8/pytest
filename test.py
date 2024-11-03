import re

def extract_digits(string):
    pattern = r'\d+'  # Matches one or more digits
    return re.findall(pattern, string)

# Test examples
print(extract_digits("+0 19 6871 871"))  # ['3', '5', '12']
print(extract_digits("Phone number: 123-456-7890"))               # ['123', '456', '7890']
