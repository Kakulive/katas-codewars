# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# Examples:
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
    num = list(map(int, numbers.split(" ")))
    evens = 0
    odds = 0
    for i in num:
        if i % 2 == 0:
            evens += 1
            continue
        else:
            odds += 1
            continue
    
    if evens >= 2:
        for i in range(len(num)):
            if num[i] % 2 == 1:
                return i+1
    else:
        for i in range(len(num)):
            if num[i] % 2 == 0:
                return i+1

print(iq_test("1 2 2"))