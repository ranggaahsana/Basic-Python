#Latihan konversi satuan temperatur

print('Program Konversi Temperatur Sederhana')
reamur = float(input("Masukan Suhu dalam Reamur: "))
print('Suhu dalam Reamur:', reamur, "Reamur")

#Reamur
celcius = (5/4)*reamur
print('Suhu dalam Celcius:', celcius, "Celcius")
#Fahrenheit
fahrenheit = ((9/4)*reamur)+32
print('Suhu dalam Fahrenheit:', fahrenheit, "Fahrenheit")
#Kelvin
kelvin = ((5/4)*reamur)+273
print('Suhu dalam Kelvin:', kelvin, "Kelvin")