import datetime

mahasiswa1 = {
	"Nama":"Oline M",
	"Nim":"480101",
	"Sks_lulus":140,
	"Beasiswa":True,
	"Lahir":datetime.datetime(2007,6,19)
}
mahasiswa2 = {
	"Nama":"Erine K",
	"Nim":"480102",
	"Sks_lulus":130,
	"Beasiswa":True,
	"Lahir":datetime.datetime(2007,7,15)
}
mahasiswa3 = {
	"Nama":"Nachia T",
	"Nim":"480103",
	"Sks_lulus":135,
	"Beasiswa":True,
	"Lahir":datetime.datetime(2009,5,11)
}

data_mahasiswa = {
	"MAH001":mahasiswa1,
	"MAH002":mahasiswa2,
	"MAH003":mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<9} {'Nim':<6} {'Sks':<3} {'Beasiswa':<5} {'Lahir':10}")

print("-"*50)

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa
	NAMA = data_mahasiswa[KEY]['Nama']
	NIM = data_mahasiswa[KEY]['Nim']
	SKS = data_mahasiswa[KEY]['Sks_lulus']
	BEASISWA = data_mahasiswa[KEY]['Beasiswa']
	LAHIR = data_mahasiswa[KEY]['Lahir'].strftime("%x")
	
	print(f"{KEY:<6} {NAMA:<8} {NIM:<6} {SKS:<3} {BEASISWA:^9} {LAHIR:10}")