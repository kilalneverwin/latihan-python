# date and time (latihan)

import datetime as dt

print("masukkan tanggal lahir bro sama tahun dan bulan")

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(f"Tanggal lahir anda : {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

# menghitung umur

hari_ayeuna = dt.date.today()
umur = hari_ayeuna - tanggal_lahir
print(f"Umur anda sekarang {umur}")