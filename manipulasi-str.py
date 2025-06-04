# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Kilal"
nama_tengah = "D"
nama_akhir = "goodboy"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " adalah " + str(panjang))

# 3. operator umtuk string
# mengecek apakah ada komponen char atau string di string

k = "K" # yang dicari harus sama huruf besar atau kecilnya
status = k in nama_lengkap
print(k + " ada di " + nama_lengkap + " = " + str(status))

k = "k" # yang dicari harus sama huruf besar atau kecilnya
status = k in nama_lengkap
print(k + " ada di " + nama_lengkap + " = " + str(status))

k = "K" # yang dicari harus sama huruf besar atau kecilnya
status = k  not in nama_lengkap
print(k + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
# print("wk" tanda bintang10)

#indexing
# lalier

# item paling kecil
print("Paling kecil : " + min(nama_lengkap))

# item paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII code adalah " + chr(data))

# 4. operator dalam bentuk method

dataa = "otong sorotong"
jumlah = dataa.count("t")
print("jumlah t pada " + dataa + " adalah " + str(jumlah))