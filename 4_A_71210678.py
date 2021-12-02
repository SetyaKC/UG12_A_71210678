#bintang pola segitiga

i=int(input("input: "))
n=2
print("Output :")

# x untuk garis bawah
# y untuk garis kanan kiri

for x in range(1,i+1):
    for y in range (1,2*i):
        if x+y==i+1 or y-x==i-1:
            print("*",end="")
        elif x==i and y!=n:
            print ("*",end="")
            n=n+2
        else:
            print(end=" ")
    print ()
