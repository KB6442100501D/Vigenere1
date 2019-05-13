import time
t_beg=time.time()

nameIN="Зашифрованный текст.txt"
nameOF="Повторы зашифрованного текста.txt"

d=dict()

with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()

with open(nameOF, mode='x', encoding="utf-8") as fOF:
    n=len(text)
    for p1 in range(n):
        for p2 in range(p1+1, n):
            assert p1<p2
            c=0
            i=p1
            j=p2
            while j<n:
                if text[i]!=text[j]:
                    break
                else:
                    c+=1
                    i+=1
                    j+=1
            if c>=3:
                dp=p2-p1
                d[dp]=d.get(dp, 0)+1
                print(c, p1, p2, repr(text[p1:p1+c]), file=fOF)
    print(72*"-", file=fOF)
    for k,v in sorted(d.items()):
        print(k,v, file=fOF)
t_end=time.time()
print(t_end-t_beg)


