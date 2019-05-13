import time
t_beg=time.time()

nameIN="Зашифрованный текст.txt"
nameOF="Автокорреляционный метод.txt"

import hashlib




with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()

with open(nameOF, mode='w', encoding="utf-8") as fOF:
    n=len(text)
    for s in range(100):
        c1=0
        c2=0
        for p1 in range(n-s):
            p2=p1+s

            if text[p1]==text[p2]:
                c1+=1
            c2+=1
        gamma=c1/c2
        print(s, c1, c2, gamma, file=fOF)






    
##    print(lwc, file=fOF)
                #print(c, p1, p2, repr(text[p1:p1+c]), file=fOF)


                
t_end=time.time()
print(t_end-t_beg)


