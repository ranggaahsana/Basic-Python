#Operasi aritmatika standar
a = 10
b = 3

#Operasi penambahan +
hasil = a + b
print(a,'+',b, '=', hasil)

#Operasi pengurangan -
hasil = a - b
print(a,'-',b, '=', hasil)

#Operasi Perkalian *
hasil = a * b
print(a,'*',b, '=', hasil)

#Operasi Pembagian /
#di python kalo pembagian yang ada koma komaan dari int
#auto berubah ke float
hasil = a / b
print(a,'/',b, '=', hasil)

#Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a,'**',b, '=', hasil)

#Operasi Modulus (Sisa bagi) %
hasil = a % b
print(a,'%',b, '=', hasil)

#Operasi Floor Division (Pembagian dibulatkan ke bawah) //
hasil = a // b
print(a,'//',b, '=', hasil)

'''
Prioritas operasi
Urutan aritmatika yang dikerjakan
1. ( )
2. Eksponensial
3. Perkalian, Pembagian, Modulus, Floor Division
4. Penjumlahan, Pengurangan
'''