#Программа читает файл data03.txt, и шифрует шифром Виженера с ключом KEY
nameIN="data03.txt"



KEY='ВИЖЕНЕР'
ABC='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
print(len(ABC), len(KEY))

with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()
print(len(text))
#conv1 это функция замены каждого символа текста ее номером в алфавите, начиная с 0
##def conv1(text):
##    textD=[]    
##    for s in text:
##        t=ABC.find(s)
##        assert t>=0
##        textD.append(t)
##    return textD

##def conv1(text):
##    return [ABC.index(s) for s in text]

def conv1(text):
    return list(map(ABC.index, text))

textD=conv1(text)
KEYD=conv1(KEY)
print(textD)
print(KEYD)
#В переменной textD содержится открытый текст
#Каждый символ заменен на числа(порядковый номер в алфавите)
#KEYD это преобразованный ключ



#conv2 это функция замены порядкого номера на символ
##def conv2(textD):
##    text1=[]    
##    for s in textD:
##        t=ABC[s]
##        text1.append(t)
##    return "".join(text1)

def conv2(textD):
    return "".join([ABC[s] for s in textD])

text1=conv2(textD)
KEYD=conv1(KEY)
assert text==text1

print(text[:100])
print(list(text[:100]))
print(textD[:100])
print(text1[:100])
