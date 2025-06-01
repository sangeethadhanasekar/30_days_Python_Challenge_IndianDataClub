# 🎯 Challenge
# - Check if a user-entered number is prime

def prime_or_not(nums):
    if (nums ==0 or nums ==1):
        print(nums,"is not a  prime number")
    elif nums>1:
        for i in range(2,nums):
            if nums%i==0:
                print(nums,"is not a prime number")
                break
        else: print(nums,"is a prime number")


nums=int(input("Enter the number: "))
prime_or_not(nums)