def fib(n):
    if n<=2:
        return n
    a,b = 1,2
    print("1 1 2",end=" ")
    for i in range(3,n):
        a,b=b,a+b
        
        print(b,end=" ")

fib(5)