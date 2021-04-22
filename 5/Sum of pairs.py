# Sum of Pairs

# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]

# Negative numbers and duplicate numbers can and will appear.

# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.

import itertools

def sum_pairs(ints, s):
    valid_pairs = []
    indices_list = []
    indices_sliced = []
    start = 0
    end = 1
    maxi = 99999999999999999
    min_index = 0
    a = list(itertools.combinations(ints, 2))
    for element in a:
        if sum(element) == s:
            valid_pairs.append(element)
    if len(valid_pairs) == 0:
        return None
    for element in valid_pairs:
        for i in element:
            indices_list.append(ints.index(i))
            ints[ints.index(i)] = "B"
    for element in range(len(indices_list) - 2):
        indices_sliced.append(indices_list[start:end+1])
        start += 2
        end += 2
    for element in indices_sliced:
        if max(element) < maxi:
            maxi = max(element)
            min_index = indices_sliced.index(element)

    return list(valid_pairs[min_index])

print((sum_pairs([1, 2, 3, 4, 1, 0], 2)))