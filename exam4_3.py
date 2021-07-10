from random import randint


a = []
b = []
SameNumbers =[]
for i in range(10):
    a.append(randint(1,50))
    b.append(randint(1,50))


for i in a:
    if i in b :
        SameNumbers.append(i)


a.sort()
b.sort()
SameNumbers.sort()
print((a),(b))
print(SameNumbers)