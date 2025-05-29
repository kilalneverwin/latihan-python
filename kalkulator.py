print(18*"=")
print("Kalkulator sederhana")
print("coded by kilalsad")
print(18*"=")

angka1 = float(input("masukkan angka = "))
operator = input(" ( +, x ,- ,÷ ) = ")
angka2 = float(input("masukkan angka = "))

if operator == "+":
  hasil = angka1 + angka2
  print(f"hasilnya {hasil}")
elif operator == "x" or operator == "*":
  hasil = angka1 * angka2
  print(f"hasilnya {hasil}")
elif operator == "-":
  hasil = angka1 - angka2
  print(f"hasilnya {hasil}")
elif operator == "÷" or operator == "/":
  hasil = angka1 / angka2
  print(f"hasilnya {hasil}")
else:
  print(f"Yang bener aja jing, lu mau ngitung pakek simbol \"{operator}\"")
print(18*"=")
print("Makasih udah pakek guwe")