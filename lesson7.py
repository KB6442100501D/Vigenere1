#программа находит все делители чисел
nameIN="dataN.txt"

with open(nameIN, encoding="utf-8") as fIF:
    primLST=eval(fIF.read())

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





