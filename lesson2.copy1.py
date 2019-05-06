#Программа читает файл data03.txt, и шифрует шифром Виженера с ключом KEY
nameIN="data03.txt"

KEY='ВИЖЕНЕР'
ABC='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '

#conv1 это функция замены каждого символа текста ее номером в алфавите, начиная с 0
def conv1(text):
    return list(map(ABC.index, text))

#conv2 это функция замены порядкого номера на символ
def conv2(textD):
    return "".join([ABC[s] for s in textD])

#Чтение данных, данные помещаются в переменную text в виде строки str
with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()

#В переменной textD содержится открытый текст
#Каждый символ заменен на числа(порядковый номер в алфавите)
#KEYD это преобразованный ключ
textD=conv1(text)
KEYD=conv1(KEY)

text1=conv2(textD)
assert text==text1

print(text[:100])
print(list(text[:100]))
print(textD[:100])
print(text1[:100])

del text1

#Зашифрование кодом Виженера текста
#k это ключ в цифровой форме, t это текст в цифровой форме
#В цифровой форме-в виде списка значений типа int от 0 до len(ABC)-1 включительно
def codeD(k, t):
    return [(k[i%len(k)]-t[i])%len(ABC) for i in range(len(t))]

code1=codeD(KEYD, textD)
print(conv2(code1[:100]))

code2=codeD(KEYD, code1)
print(conv2(code2[:100]))


