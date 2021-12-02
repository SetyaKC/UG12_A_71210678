nama=[]
nomor_kursi=[]

a=input("Masukkan nama: ")
b=("Masukkan nomor kursi "+a+": ")

while a!="STOP":
    b=("Masukkan nomor kursi "+a+": ")
    i=input(b)
    if i not in nomor_kursi:
        nomor_kursi.append(i)
        nama.append(a)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    a=input("Masukkan nama: ")

print()
print("List kursi yang telah terisi : ")

for x in range(0, len(nomor_kursi), 1):
    print("Kursi nomor", nomor_kursi[x], "telah diisi oleh", nama[x])
