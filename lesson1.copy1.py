#Программа читает файл data03.txt, и шифрует шифром Виженера с ключом KEY
nameIN="data03.txt"



KEY='ВИЖЕНЕР'
ABC='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
print(len(ABC))

with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()
#conv1 это функция замены каждого символа текста ее номером в алфавите, начиная с 0
def conv1(text):
    textD=[]    
    for s in text:
        t=ABC.find(s)
        assert t>=0
        textD.append(t)
    return textD

textD=conv1(text)
KEYD=conv1(KEY)
print(textD)
print(KEYD)
#В переменной textD содержится открытый текст
#Каждый символ заменен на числа(порядковый номер в алфавите)
#KEYD это преобразованный ключ
