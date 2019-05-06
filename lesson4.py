#программа находит все простые числа до 10000000
from math import sqrt

nameOF="dataN.txt"
n = 25000000
a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1

with open(nameOF, mode='x', encoding="utf-8") as fOF:
    print(lst, file=fOF)
