def sort_array(source_array):
    sorted_array = sorted(source_array)
    odd_numbers = []
    for number in sorted_array:
        if number % 2 != 0:
            odd_numbers.append(number)
    final_array = []
    for number in source_array:
        if number % 2 == 0:
            final_array.append(number)
        else:
            final_array.append(odd_numbers[0])
            odd_numbers.pop(0)

    return final_array