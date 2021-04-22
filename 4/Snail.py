"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def snail(snail_map):
    semi_final_list = []
    while len(snail_map) > 0:
        semi_final_list.append(snail_map[0])
        snail_map.pop(0)
        if len(snail_map) == 0:
            break

        for row in snail_map:
            semi_final_list.append(row[-1])
            row.pop()
        if len(snail_map) == 0:
            break

        semi_final_list.append(snail_map[-1][::-1])
        snail_map.pop()
        if len(snail_map) == 0:
            break

        for row in snail_map[::-1]:
            semi_final_list.append(row[0])
            row.pop(0)
        if len(snail_map) == 0:
            break
    
    final_list = []
    for elem in semi_final_list:
        if isinstance(elem, list) == True:
            final_list.extend(elem)
        else:
            final_list.append(elem)

    return final_list
print(snail([[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,3,6,9,8,7,4,5]