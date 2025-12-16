#basic patterns
n=5
for i in range (1,n+1):
    print("*"*i)


#2nd programme
    n=5
    for i in range (n , 0, -1):
        print("*"*i)


#3rd programme
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#4th programme
n=5
for i in range(1,n+1):
     print(" "*(n-i)+"*"*i)

     #5th programme
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

