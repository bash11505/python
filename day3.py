#numbers diamond pattern
n=5
for i in range (1,n+1):
    print(" "*(n-i)+(str(i)+" ")*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+(str(i)+" ")*i)
#diamond pattern with 5 numbers
#upper case
n = 5

# Upper half
for i in range(1, n+1):
    print(" " * (n - i), end="")      # Spaces
    for j in range(1, i+1):           # Ascending numbers
        print(j, end="")
    for j in range(i-1, 0, -1):       # Descending numbers
        print(j, end="")
    print()                            # Move to next line
# Lower half
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")      # Spaces
    for j in range(1, i+1):           # Ascending numbers
        print(j, end="")
    for j in range(i-1, 0, -1):       # Descending numbers
        print(j, end="")
    print()                            # Move to next line
