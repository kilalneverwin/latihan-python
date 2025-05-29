# merubah semua menjadi upper cass

sapa = "bre"
print("Normal = " + sapa)
salam = sapa.upper()
print("UPPER = " + salam)

print(20*"=")

# lower case
sopo = "AkHu GaNtEnGsS"
print("Normal = " + sopo)
jarwo = sopo.lower()
print("LOWER = " + jarwo)

print(20*"=")

# mengecek apakah lower atau UPPER
# setiap hasilnya akan bool jadi harus diubah
cantik = "oline"
apakah_lower = cantik.islower()
print(cantik + " is lower = " + str(apakah_lower))
apakah_upper = cantik.isupper()
print(cantik + " is upper = " + str(apakah_upper))

print(20*"=")

# mengecek judul
judul = "Kilal Dan Oline"
cek_judul = judul.istitle()
print(judul + " Is title = " + str(cek_judul))

print(20*"=")

# mengecek komponen startswith() dan endswith()
erine = "Angry girl".startswith("Angry")
print("start = " + str(erine))

kimmy = "Lucu banget".endswith("banget")
print("end = " + str(kimmy))

print(20*"=")

# penggabungan komponen join() split()
pisah = ['aku','sayang','oline']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)
naonwe = "aku,sayang,kamu"
print(naonwe.split(','))

print(20*"=")

# alokasi karakter rjust() ljust() center()

kanan = "kilalz".rjust(10)
print("'" + kanan + "'")

kiri = "kilalz".ljust(10)
print("'" + kiri + "'")

tengah = "kilalz".center(20,":")
print("'" + tengah + "'")

# kebalikannya --> strip()
oiy = "kilalz".strip(":")
print("'" + oiy + "'")