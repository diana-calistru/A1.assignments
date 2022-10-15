import math

n = 3658
nr = 0
list = []
while n != 0:
    list.append(n % 10)
    nr = nr + 1
    n = math.trunc(n / 10)

list.sort(reverse=True)
n=0
for i in range (0, nr):
   n=n*10+list[i]

print(n)

