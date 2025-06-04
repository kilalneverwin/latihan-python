# format string

# contoh generic
# string

# yang rumit
name = "lalzz"
sapa = "hello " + name
print(sapa)

# yang simpel
nama = "ucupz"
format_str = f"hello {nama}"
print(format_str)

# boolen
bool = True
format_str = f"boolean = {bool}"
print(format_str)

# angka
angka = 2007.7
format_str = f"angkanya = {angka}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2007.7654321
format_str = f"desimal = {angka:.4f}"
print(format_str)

# formart angka lain (binary, ocatl, hexadecimal)
angka = 255
format_binary = f"binary {bin(angka)}"
format_octal = f"octal {oct(angka)}"
format_hex = f"hex {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)