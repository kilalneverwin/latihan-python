# copy list dengan .copy()

a = ["Adit","Tio","Ezhar"]

b = a.copy()
print(f" address a = {hex(id(a))}")
print(f" address b = {hex(id(b))}")

print(f"a = {a}")
print(f"b = {b}")

print("Ubah data 0")
b[0] = "Adin"

print(f" a = {a}")
print(f" b = {b}")