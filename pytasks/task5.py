"""The provided code stub reads and integer,n , from STDIN. For all non-negative integers i>n, print i*i."""

n = int(input(""))
if n <= 0 or n >= 20: 
    print("try again")
    n = int(input(""))
x = 0
for i in range(n):
    x = i*i
    print(x)