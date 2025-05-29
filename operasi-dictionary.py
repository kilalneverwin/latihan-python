# operator dictionary

data_dict = {
	"dick":"dicky doli",
	"peb":"pebrian miftah",
	"bar":"akbar ujang"
}

# panjang dictionary

lendict = len(data_dict)
print(f"panjang dictionary : {lendict}")

# mengecek key exist atau tidak

key = "peb"
chekkey = key in data_dict
print(f"apakah {key} ada di data_dict : {chekkey}")

# mengakses value dengan get
print(data_dict["dick"])
print(data_dict.get("dick"))
print(data_dict.get("mud","EWEH!!"))

#mengupdate data
print(data_dict)
data_dict.update({"dick":"dicky kontol"})
print(data_dict)
data_dict.update({"lal":"kilal ganteng"})
print(data_dict)

# mengdelete data
del data_dict["lal"]
print(data_dict)