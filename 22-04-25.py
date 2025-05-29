import copy  # Untuk deep copy

# === 1. Langsung looping isi list ===
buah = ["apel", "jeruk", "pisang"]

print("=== 1. Langsung looping isi list ===")
for item in buah:
    print(item)

# === 2. Loop pakai index ===
print("\n=== 2. Loop pakai index ===")
for i in range(len(buah)):
    print(f"Index {i}: {buah[i]}")

# === 3. Loop pakai enumerate ===
print("\n=== 3. Loop pakai enumerate ===")
for i, item in enumerate(buah):
    print(f"Index {i}: {item}")

# === 4. Looping list pakai for (tanpa index) ===
print("\n=== 4. Looping list pakai for ===")
for item in buah:
    print(item)

# === 5. Loop pakai while ===
print("\n=== 5. Loop pakai WHILE ===")
i = 0
while i < len(buah):
    print(f"Index {i}: {buah[i]}")
    i += 1

# === 6. Fungsi-fungsi dasar list ===
print("\n=== 6. Fungsi dasar list ===")
buah.append("mangga")
buah.insert(1, "semangka")
buah.remove("jeruk")
buah.pop()
buah.sort()
buah.reverse()

print("Isi list setelah dimodifikasi:")
for item in buah:
    print(item)

# === 7. Nested list dan unpacking ===
print("\n=== 7. Nested list dan unpacking ===")
data = [["a", 1], ["b", 2], ["c", 3]]

for huruf, angka in data:
    print(f"Huruf: {huruf}, Angka: {angka}")

# === 8. Segitiga bintang pakai FOR ===
print("\n=== Segitiga Bintang (FOR) ===")
tinggi = 5
for i in range(1, tinggi + 1):
    print("*" * i)

# === 9. Segitiga bintang pakai WHILE ===
print("\n=== Segitiga Bintang (WHILE) ===")
i = 1
while i <= tinggi:
    print("*" * i)
    i += 1

# === 10. Copy List ===
print("\n=== Copy List ===")
buah_asli = [["apel", 10], ["jeruk", 20]]

# Shallow copy
buah_copy = buah_asli.copy()

# Deep copy
buah_deep = copy.deepcopy(buah_asli)

buah_asli[0][1] = 27

print("Shallow Copy:")
print(buah_copy)

print("Deep Copy:")
print(buah_deep)

print("Asli:")
print(buah_asli)