#Latihan konversi satuan temperatur

print('Program Konversi Temperatur Sederhana')
fahrenheit = float(input("Masukan Suhu dalam Fahrenheit: "))
print('Suhu dalam fahrenheit:', fahrenheit, "fahrenheit")

#Reamur
celcius = (5/9)*(fahrenheit-32)
print('Suhu dalam Celcius:', celcius, "Celcius")
#Fahrenheit
reamur = (4/9)*(fahrenheit-32)
print('Suhu dalam reamur:', reamur, "reamur")
#Kelvin
kelvin = ((5/9)*(fahrenheit-32))+273
print('Suhu dalam Kelvin:', kelvin, "Kelvin")