"""
Generate the largest perfect number smaller than a given natural number n.
If such a number does not exist, a message should be displayed.
A number is perfect if it is equal to the sum of its divisors, except itself.
"""

def perfect(n):
    s = 0
    for i in range(1, (n // 2)+1):
        if n % i == 0:
            s = s + i
    if s == n:
        return True
    else:
        return False


def start():

    n = int(input("Enter a natural number: "))

    for i in range(n - 1, 1, -1):
        if perfect(i) == True:
            print("Largest perfect number smaller than ", n, " is: ", i)
            break
        elif i == 2:
            print("A perfect number smaller than ", n, " does not exist")


start()
