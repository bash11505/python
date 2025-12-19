#square patterns
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

    #stars
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# traingle patterns
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
    #stars
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()