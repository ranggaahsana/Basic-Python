#Latihan konversi satuan temperatur

print('Program Konversi Temperatur Sederhana')
kelvin = float(input("Masukan Suhu dalam kelvin: "))
print('Suhu dalam kelvin:', kelvin, "kelvin")

#Reamur
celcius = kelvin-273
print('Suhu dalam Celcius:', celcius, "Celcius")
#Reamur
reamur = (4/5)*(kelvin-273)
print('Suhu dalam reamur:', reamur, "reamur")
#Kelvin
fahrenheit = ((9/5)*(kelvin-273))+32
print('Suhu dalam fahrenheit:', fahrenheit, "fahrenheit")