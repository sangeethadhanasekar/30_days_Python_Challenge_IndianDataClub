# 🎯 Challenge
# -  Generate the first n Fibonacci numbers with a generator

def fib(val):
    i,a,b=0,0,1

    while i<val:
        yield a , i
        a,b=b,a+b
        i+=1

for i,j in fib(int(input("\n Enter the fibonacci series limit: \n"))):
    print(f"the {j+1} th element of fibonacci series is: {i}")