import time









t_beg=time.time()

nameIN="Зашифрованный текст.txt"
nameOF="Автокорреляционный метод.txt"

import hashlib


lst1=[0]

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
        if s>0:
            lst1.append(gamma)
        print(s, c1, c2, gamma, file=fOF)

        

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

##objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(lst1))

plt.bar(y_pos, lst1, align='center', alpha=0.5)
##plt.xticks(y_pos, objects)
##plt.ylabel('Usage')
##plt.title('Programming language usage')

plt.show()




    
##    print(lwc, file=fOF)
                #print(c, p1, p2, repr(text[p1:p1+c]), file=fOF)


                
t_end=time.time()
print(t_end-t_beg)


