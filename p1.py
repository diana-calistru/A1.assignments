"""
For a given natural number `n` find the largest natural number written with the same digits.
"""

import math

n = int(input("Enter a natural number:"))
nr = 0
list = [] # the list will contain all the digits of n

while n != 0:
    list.append(n % 10)
    nr = nr + 1
    n = math.trunc(n / 10)

list.sort(reverse=True) # sorted in a descending order to find the largest number in an easier way

n = 0

for i in range(0, nr):
    n = n * 10 + list[i] # computes the largest number digit by digit using the elements of the list

print(n)
