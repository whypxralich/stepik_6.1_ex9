a = int(input())

#каждая цифра числа
n1 = (a//100)%10
n2 = (a%100)//10
n3 = a%10

x = min(n1, n2, n3) #меньшее число
y = max(n1, n2, n3) #большее число
z = (n1+n2+n3) - (x+y) #среднее

if y - x == z:
    print ("Число интересное")
else: 
    print ("Число неинтересное")

