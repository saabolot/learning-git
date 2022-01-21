liczby = list(range(0,101))  
liczby_podzielne5=[]
liczby3=[]

for i in liczby:
    if i % 5 == 0:
        liczby_podzielne5.append(i)
for i in liczby_podzielne5:
    liczby3.append(i**3)
print(liczby_podzielne5)
print(liczby3)