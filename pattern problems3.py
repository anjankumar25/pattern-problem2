

for i in range(1,5):
    for m in range(i,5):
        print(" ",end="")
    for l in range(i):
        print(i,end="")
    for k in range(i-1):
        print(i,end="")
    for p in range(i,5):
        print(" ",end="")
    print()
p=5
for j in range(1,6):
    for t in range(j-1):
        print(" ",end="") 
    
    for q in range(j,6-1):
        print(p,end="")
    for f in range(j,6):
        print(p,end="")
    p+=1
    print()

    
    