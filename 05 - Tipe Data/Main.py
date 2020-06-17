##list tipe data standar di integer
#integer
integer = 10
print("data: ", integer)
print("Tipe datanya: ", type(integer))

#float
floatData = 10.99
print("data: ", floatData)
print("Tipe datanya: ", type(floatData))

#String
Stringnih  = "aselole"
print("data: ", Stringnih)
print("Tipe datanya: ", type(Stringnih))

#Boolean
booleanNih = True
print("data: ", booleanNih)
print("Tipe datanya: ", type(booleanNih))



##List tipe data khusus
#Bilangan kompleks (imaginer 5+7i)
data_complex = complex(5, 7)
print("data: ", data_complex)
print("Tipe datanya: ", type(data_complex))

#Tipe data dari bahasa C
#from ctypes import c_(tipe data)  
from ctypes import c_double