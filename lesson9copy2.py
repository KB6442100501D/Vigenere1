import time
t_beg=time.time()

nameIN="data03.txt"

with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()




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
##        if c>=3:
##            print(c, p1, p2, repr(text[p1:p1+c]))


t_end=time.time()
print(t_end-t_beg)
