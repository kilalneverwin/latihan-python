import copy

# loop list
buah = ["manggis","sirsak","nanas",]
for item in buah:
	print(item)
	
print("="*10)

# loop index
for i in range(len(buah)):
	print(f"Index {i} : {buah[i]}")
	
print("="*10)

# loop enumerate
for i, item in enumerate(buah):
	print(f"Index {i} : {item}")
	
print("="*10)

#while loop
i = 0
while i < len(buah):
	print(f"Index {i}: {buah[i]}")
	i += 1
	
print("="*10)

# nested list dan unpacking
data = [["oline",17], ["nina",15], ["erine",17]]
for nama, umur in data:
	print(f"Nama: {nama}, Umur: {umur}")
	
print("="*10)

#copy list
nama_asli = [["oline",17], ["erine",17]]

#copy biasa
nama_copy = nama_asli.copy()

#deep copy
nama_deep = copy.deepcopy(nama_asli)

nama_asli[0][1] = 18

print("Copy biasa")
print(nama_copy)

print("Copy deep")
print(nama_deep)

print("Asli")
print(nama_asli)