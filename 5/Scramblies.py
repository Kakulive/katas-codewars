# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

#     Only lower case letters will be used (a-z). No punctuation or digits will be included.
#     Performance needs to be considered

# Input strings s1 and s2 are null terminated.

# Examples

# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

#TOO SLOW
# def scramble(s1, s2):
#     for i in s2:
#         if s1.count(i) < s2.count(i):
#             return False
#     return True

#TOO SLOW AGAIN
# def scramble(s1, s2):
#     l2 = [x for x in s2]
#     for i in s1:
#         if i in l2:
#             l2.remove(i)
#     if len(l2) == 0:
#         return True
#     else:
#         return False

def scramble(s1, s2):
    dictionary = {}
    for i in s1:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for i in s2:
        if i not in dictionary:
            return False
        elif dictionary[i] > 0:
            dictionary[i] -= 1
        else:
            return False

    return True

print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))