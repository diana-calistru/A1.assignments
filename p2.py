"""
The numbers `n1` and `n2` have the property `P` if their writing in base 10 uses the same digits (e.g. `2113 and 323121`).
Determine whether two given natural numbers have property `P`.
"""

import math


def digits(n, list, nr):
    while n != 0:
        list.append(n % 10)
        nr = nr + 1
        n = math.trunc(n / 10)

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
list1 = []
list2 = []
nr1 = 0
nr2 = 0
ok=1

digits(n1, list1, nr1)
digits(n2, list2, nr2)

if nr1>nr2:
    for i in list1:
        if i not  in list2:
            ok=0
else:
    for i in list2:
        if i not  in list1:
            ok=0

if ok == 1:
    print("Numbers have the 'P' property.")
else:
    print("Numbers don't have the 'P' property.")
