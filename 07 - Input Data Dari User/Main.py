#ngambil data dari user dengan simpel

#Semua data yang diinput typenya STR
data = input("Masukan Data: ") 
print("data = ",data, "tipe data = ", type(data))

#kalo mau inputannya int ato float di cast
angka = int(input("Masukan angka: "))
print("data = ",angka, "tipe data = ", type(angka))

#Kalo boolean
trufalse = bool(int(input("Masukan nilai boolean: ")))
print("data = ",trufalse, "tipe data = ", type(trufalse))
