#читаем из файла простые числа
nameIN="dataN.txt"

with open(nameIN, encoding="utf-8") as fIF:
    primLST=eval(fIF.read())


for s in primLST[:100]:
    print (s)
print()
for s in primLST[-100:]:
    print (s)
