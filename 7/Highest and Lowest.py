# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    numbers = numbers.split()
    ducks = list(map(int, numbers))

    return f"{max(ducks)} {min(ducks)}"

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))