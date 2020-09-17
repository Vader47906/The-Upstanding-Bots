import random

def is_letter(c):
    return ord(c) > ord('a') and ord(c) < ord('z')\
        or ord(c) > ord('A') and ord(c) < ord('Z')

def mocking_case(string):
    new_str = ""
    upper = True
    for c in string:
        if is_letter(c):
            if upper:
                new_str += c.upper()
            else:
                new_str += c.lower()
            if random.randint(0,100) >= 30:
                upper = not upper
        else:
            new_str += c
    return new_str
