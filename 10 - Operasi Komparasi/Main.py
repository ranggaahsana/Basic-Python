#Operasi komparasi
#hasil operasi selalu hasilnya boolean

#>, <, >=, <=, ==, !=, is, is not

a=4
b=2

hasil = a < 2
print(hasil) #False
hasil = a > 2
print(hasil) #True

hasil = a <= 4
print(hasil) #true
hasil = a >= 4
print(hasil) #true

hasil = a != 2
print(hasil) #True
hasil = a == 4
print(hasil) #True

#is sebagai komparasi object identity
x = 5
y = 5
maka = x is y
print('nilai x= ',x,'id= ',hex(id(x)))
print('nilai y= ',y,'id= ',hex(id(y)))
#karena nilai x dan y sama maka disimpan di memory yang sama
print(maka)