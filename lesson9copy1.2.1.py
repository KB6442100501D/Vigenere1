import time
t_beg=time.time()

nameIN="Зашифрованный текст.txt"
nameOF="Повторы зашифрованного текста 3.txt"


import hashlib

class PDD:
    def __init__(self,
                 File="dataN.txt",
                 Hash="037ab10b0d7b21f7c59846f955d1efaa7fbba827cecbf011109268a7169610110e78d762481734a6ff7e6f9f948c8602410919d6a611191881897c0771ee967b"):
        with open(File, mode="br") as fIF:
            d=fIF.read()
            h=hashlib.sha512()
            h.update(d)
            assert h.hexdigest()==Hash
            self._primLST=eval(d.decode())

    def dec(self, a):
        r=[]
        for s in self._primLST:
            i=0
            while True:
                c,d=divmod(a,s)
                if d==0:
                    i+=1
                    a=c
                else:
                    break
            if i>0:
                r.append((s,i))
        assert a==1
        return r


pdd1=PDD()




d1=dict()
d2=dict()

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
                d1[dp]=d1.get(dp, 0)+1

                d2.setdefault(c, []).append(dp)
                
                #print(c, p1, p2, repr(text[p1:p1+c]), file=fOF)
#смещение и кол-во шт
    for k,v in sorted(d2.items(), reverse=True):
        d3=dict()
        for u in v:
            for a,b in pdd1.dec(u):
                d3[a]=d3.get(a, 0) + b
        print(sorted(d3.items(), key=lambda x: (-x[1], x[0])))



                
t_end=time.time()
print(t_end-t_beg)


