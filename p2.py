"""
The numbers `n1` and `n2` have the property `P` if their writing in base 10 uses the same digits (e.g. `2113 and 323121`).
Determine whether two given natural numbers have property `P`.
"""

import math

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
list1 = []
list2 = []
nr1 = 0
nr2 = 0

def digits(n, list, nr):
    while n != 0:
        if n%10 in list = False:
            list.append(n % 10)
            nr = nr + 1
        n = math.trunc(n / 10)

digits(n1, list1, nr1)

print(list1[:])