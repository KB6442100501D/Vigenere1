#Программа читает файл data01.txt, переводит в uppercase.
#создает список слов(переменная wordsList).
#Слово-это последовательность кириллических букв.
#В переменной textL накапливается количество слов.
nameIN="data01.txt"
nameOF="data03.txt"

fragmentS=0.1
fragmentL=10000
printLim=10

import re
p1=re.compile("[а-я]", re.I)

wordsList=[]
cw=[]

with open(nameIN, encoding="utf-8") as fIF:
    textL=0
    for s in fIF.read():
        if p1.fullmatch(s):
            s=s.upper()
            if s=="Ё":
                s="Е"
            cw.append(s)
        else:
            if len(cw)>0:
                textL+=len(cw)
                wordsList.append("".join(cw))
                cw=[]
            else:
                pass
    if len(cw)>0:
        textL+=len(cw)
        wordsList.append("".join(cw))
#Имеем список слов всего документа переменной wordsList

##i=0
##for s in wordsList:
##    i+=1
##    if i<=printLim or len(wordsList)-i<printLim:
##        print(i, s)
##print(len(wordsList), textL)

i=0
s=0
t=0
limit=int(fragmentS*(textL+len(wordsList)))
while i<len(wordsList):
    if s>=limit:
        t=1
        break
    s+=len(wordsList[i])+1
    i+=1
assert t>0

i1=i
s=0
t=0
limit=fragmentL+1
while i<len(wordsList):
    if s>=limit:
        t=1
        break
    s+=len(wordsList[i])+1
    i+=1
assert t>0
i2=i
print(i+1, s)

##i=0
##for s in wordsList[i1:i2]:
##    i+=1
##    if i<=printLim or len(wordsList)-i<printLim:
##        print(i, s)
##print(len(wordsList), textL)
#i1 i2 указывают диапазон слов, которые у нас должны быть зашифрованы i1<=i<i2

text=" ".join(wordsList[i1:i2])
print(len(text))
print(text)
with open(nameOF, mode='x', encoding="utf-8") as fOF:
    print(fOF.write(text))
