#Perhitungan suatu deret angka

deret=input("Masukkan deret angka : ")
angka=deret.split(",")
hitung=0

print("Total : ",end=" ")

for deret in angka :
    deret=int(deret)
    if deret%2==1:
        hitung=hitung-deret
        print(deret*-1, end=" ")
    else:
        hitung=hitung+deret
        print("+",deret, end=" ")
        
print()
print("Hasil perhitungan diatas ialah",hitung)


