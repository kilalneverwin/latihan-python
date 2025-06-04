## list

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["kilal","adila","oline"]
print(data_string)

# kumpulan data boolen
data_boolean = [True, False, False, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"kilal",False,2,"adila",True]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pakek for if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)