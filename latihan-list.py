# latihan list buku

list_buku = []

while True:
	print("Masukkan data buku")
	judul = input("Judul buku :\t")
	penulis = input("Penulis :\t")
	
	buku_baru = [judul, penulis]
	list_buku.append(buku_baru)
	
	print("\n\n","="*20, "Data Buku","="*20)
	
	for index,buku in enumerate(list_buku):
		print(f"{index} | {buku[0]} | {buku[1]}")
	
	print("\n\n","="*30)
	isLanjut = input("Lanjut? (y/n)")
	
	if isLanjut.lower() == "n":
		break
print("Selesai, Thankyou")