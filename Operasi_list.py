data_angka = [1,1,2,3,4,5,6,7,8,9,9,8,6,5]
print(f"data angka = {data_angka}")

#count
data_angka1 = data_angka.count(1)
data_angka9 = data_angka.count(9)

print(f"angka 1 ada = {data_angka1}")
print(f"angka 9 ada = {data_angka9}")

# ambil posisi data (index)

data_nama = ["Nachia","Erine","Oline","Lily"]
print(f"data = {data_nama}")

index_erine = data_nama.index("Erine")
index_oline = data_nama.index("Oline")

print(f"Index sayang erine = {index_erine}")
print(f"Index sayang oline = {index_oline}")

# mengurutkan list
print(f"Data = \n{data_angka}")
data_angka.sort()
print(f"Data sort = \n{data_angka}")

print(f"Data = \n{data_nama}")
data_nama.sort()
print(f"Data sort = \n{data_nama}")

# reverse
data_angka.reverse()
data_nama.reverse()
print(f"Data reverse = \n{data_angka} \n{data_nama}")