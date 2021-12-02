a= input("Input: ")
b= len(a)
print("Output :")
for x in range(0,b,1):
    for y in range(0,x+1):
        print(a[y], end="")
    print()
for x in range(b-1,0,-1):
    for y in range(0,x):
        print(a[y], end="")
    print()
