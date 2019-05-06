nameIN="dataN.txt"

import hashlib

with open(nameIN, mode="br") as fIF:
    d=fIF.read()
    h=hashlib.sha512()
    h.update(d)
    assert h.hexdigest()=="037ab10b0d7b21f7c59846f955d1efaa7fbba827cecbf011109268a7169610110e78d762481734a6ff7e6f9f948c8602410919d6a611191881897c0771ee967b"
    primLST=eval(d.decode())

aa=[11, 24, 258, 6473, 36734637, 43562567456234, 1000000000000001]

def dec(a):
    r=[]
    for s in primLST:
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



for i in aa:
    print (i, dec(i))





