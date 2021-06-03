# Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

# The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

def has_unique_chars(string):
    string_new = set(string)
    print(string_new)
    if len(string_new) == len(string):
        return True
    else:
        return False

has_unique_chars("++-")