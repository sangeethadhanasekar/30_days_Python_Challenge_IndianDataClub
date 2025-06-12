# 🎯 **Challenge**
# - Calculate factorial recursively

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print("the factorial of given number is", fib(int(input("\n\n\nEnter the number: "))))