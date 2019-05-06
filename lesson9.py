import time
t_beg=time.time()


nameIN="data03.txt"

with open(nameIN, encoding="utf-8") as fIF:
    text=fIF.read()




n=len(text)
for p1 in range(n):
    for p2 in range(p1+1, n):

        c=0
        for i,j in zip(text[p1:n-1-p2+p1],text[p2:n-1]):
            if i!=j:
                break
            else:
                c+=1
##        if c>=3:
##            print(c, p1, p2, repr(text[p1:p1+c]))



t_end=time.time()
print(t_end-t_beg)
