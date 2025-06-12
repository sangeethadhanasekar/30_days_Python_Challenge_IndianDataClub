# 🎯 Challenge
# - Read numbers from a file and handle errors gracefully
print("\n\n")
try:
    with open("day10.txt",'r') as f:
        number=[]
        for line in f:
            for word in line.split(" "):
                try:
                    number.append(int(word.strip()))    
                except ValueError:
                    print("Invalid number:",word)

        print(number)            

except FileNotFoundError:
    print("file doesn't exists")
    
print("\n\n")
