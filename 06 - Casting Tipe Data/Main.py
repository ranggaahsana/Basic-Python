#Casting tipe data 
#List tipe data int, float, str, bool

#INTEGER
print("====INTEGER====")
data_int    = 10
data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int) #False jika int = 0
print("Data= ", data_int, "Tipe= ", type(data_int))
print("Data= ", data_float, "Tipe= ", type(data_float))
print("Data= ", data_str, "Tipe= ", type(data_str))
print("Data= ", data_bool, "Tipe= ", type(data_bool))

#FLOAT
print("====FLOAT====")
data_float  = 99.99
data_int    = int(data_float) #Dibuletin ke bawah, bukan ke yang terdekat
data_str    = str(data_float)
data_bool   = bool(data_float) #False jika float = 0
print("Data= ", data_float, "Tipe= ", type(data_float))
print("Data= ", data_int, "Tipe= ", type(data_int))
print("Data= ", data_str, "Tipe= ", type(data_str))
print("Data= ", data_bool, "Tipe= ", type(data_bool))

#STRING
print("====String====")
data_str    = "10000000" 
data_int    = int(data_str) #STR gabisa di ke int kecuali angka yang tipe data nya str
data_float  = float(data_str)
data_bool   = bool(data_str) #False jika str kosong. contoh data_str = ""
print("Data= ", data_str, "Tipe= ", type(data_str))
print("Data= ", data_int, "Tipe= ", type(data_int))
print("Data= ", data_float, "Tipe= ", type(data_float))
print("Data= ", data_bool, "Tipe= ", type(data_bool))

#BOOLEAN
print("====Boolean====")
data_bool   = True 
data_str    = str(data_bool) 
data_int    = int(data_bool) #jika true bernilai 1 dan false 0
data_float  = float(data_bool) #jika true bernilai 1.0 dan false 0.0
print("Data= ", data_bool, "Tipe= ", type(data_bool))
print("Data= ", data_int, "Tipe= ", type(data_int))
print("Data= ", data_float, "Tipe= ", type(data_float))
print("Data= ", data_str, "Tipe= ", type(data_str))