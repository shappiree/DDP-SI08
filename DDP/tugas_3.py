# 3. Buat program untuk minta input jumlah baris dan buat rangkaian
print("\n=======================\n")
jumlah_baris = int(input("Masukkan baris: "))
for i in range(1, jumlah_baris + 1):
    print("*" * i)

print("\n======================\n") 

print("\n======================\n")

isUSer = int(input("Masukan angka ="))
for k in range(1, isUSer + 1):
    print("*" * k) 

print("\n=====================\n") 

for h in range(1, isUSer + 1):
    for g in range(h):
        print("*", end="")
    print()

print("\n========================\n")        