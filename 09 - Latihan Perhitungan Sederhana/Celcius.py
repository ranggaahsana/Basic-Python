#Latihan konversi satuan temperatur

#Program konversi celsius ke satuan lain
print('Program Konversi Temperatur Sederhana')
celcius = float(input("Masukan Suhu dalam Celcius: "))
print('Suhu dalam Celcius:', celcius, "Celcius")

#Reamur
reamur = (4/5)*celcius
print('Suhu dalam Reamur:', reamur, "Reamur")
#Fahrenheit
fahrenheit = ((9/5)*celcius)+32
print('Suhu dalam Fahrenheit:', fahrenheit, "Fahrenheit")
#Kelvin
kelvin = celcius+273
print('Suhu dalam Kelvin:', kelvin, "Kelvin")