data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4,5]
print(f"Ini list biasa > {data_list_biasa}")

list_2D = [data_0,data_1,16]
print(f"ini list 2d > {list_2D}")

#contoh penggunaan

peserta_1 = ["oline",18,"wanita"]
peserta_2 = ["kilal",18,"Laki-laki"]

list_peserta = [peserta_1,peserta_2]
print(f"list peserta > {list_peserta}")

for peserta in list_peserta:
	print(f"Nama\t= {peserta [0]}")
	print(f"Umur\t= {peserta [1]}")
	print(f"Gender\t= {peserta [2]}\n")