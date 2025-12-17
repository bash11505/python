#traingle pattern
n=5
for i in range(1,n+1):
    print(" " * (n - i) + "*" * (2 * i - 1))
#reverse traigle pattern
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))
#simple same number
n=5
for i in range(1,n+1):
    print(str(i)*i)
#folded petterns
n=5
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num=num+1
        print()
    #row-wise number pattern
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
        print()
#diamond pattern
        n=5
    for i in range(1,n+1):
       print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n, 0, -1):
       print(" " * (n - i) + "*" * (2*i - 1))