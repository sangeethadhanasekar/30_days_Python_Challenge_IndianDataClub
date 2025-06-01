"""🎯 Challenge
- Write a function that computes the sum and average of a list of numbers"""

def sum_average(a_list):
    
    total=0
    for i in a_list:
        total+=int(i)

    average=total/len(a_list)
    return total,average

#ans= lambda a_list,total=0: total+=i for i in a_list
a_list=list(input("enter the list of numbers (eg: 10 20 30):").split(" "))
a_total,a_average= sum_average(a_list)
print(f"sum of the given list is {a_total} \naverage of the given list is {a_average}")