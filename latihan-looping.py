sisi = 5

# 1. menggunakan for

# dummy variabel
print("awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir for")

# 2. menggunakan while
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir while")