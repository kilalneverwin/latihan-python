data = ["Oline", "Erine", "Nina"]

# mengambil data dari list ini
data_0 = data[0]
print(f"Data pertama adalah = {data_0}")

data_terakhir = data[-1]
print(f"Data terakhir adalah = {data_terakhir}")

# mengambil jumlah data
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

# manipulasi list
# menambah item sesuai posisi

data.insert(1,"Delynn")
print(f"Data sesudah ditambah = \n{data}")

# menambah diakhir list
data.append("Eldaa")
print(f"Data ditambah lagi = \n{data}")

# menambah list dengan list
data_baru = ["Kilal","Dicky","Lewin"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")

# merubah data
data[3] = "Eldablu"
print(f"Data setelah di rubah \n{data}")

# meremove data
data.remove("Dicky")
print(f"Data setelah di remove = \n{data}")

# meremove data paling belakang
data.pop()
print(f"Data akhir = \n{data}")