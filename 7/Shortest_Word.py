"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    x = s.split(" ")
    shortest = x[0]
    for element in x:
        if len(element) < len(shortest):
            shortest = element
    return len(shortest)

print(find_short("Kek bobol sie drze"))