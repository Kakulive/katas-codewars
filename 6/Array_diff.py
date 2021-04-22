# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

a = [55,33,22,11]
b = [22,11]

def array_diff(a, b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    return c

def ab(a,b):
    return [x for x in a if x not in b]

print(ab(a,b))