# copy dict

oshi_oshi = {
	"line":"oline",
	"rine":"erine",
	"chia":"nachia"
}

oshi2 = oshi_oshi.copy()

print(f"oshi : {oshi_oshi}")
print(f"oshi2 : {oshi2}\n")

oshi_oshi["chia"] = "nachia tutachia"
print(f"oshi : {oshi_oshi}")
print(f"oshi2 : {oshi2}")

# pop dictionary (berdasarkan key)

dataErine = oshi2.pop("rine")
print(f"Data erine : {dataErine}")
print(f"Data oshi2 : {oshi2}\n")

# popitem dict (yang terakhir)

dataTerakhir = oshi2.popitem()
print(f"Data terakhir : {dataTerakhir}")
print(f"Data oshi2 : {oshi2}")