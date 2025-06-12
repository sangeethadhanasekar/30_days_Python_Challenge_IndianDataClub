# 🎯 Challenge
# - Validate gmail addresses using regex
import re
while True:
    #pattern="[a-zA-Z0-9\_\.]+@gmail.com" // sangi#abc@gmail.com turns to be valid email
    pattern="^[a-zA-Z0-9_.]+@gmail\.com$" # here  ^ $ Ensure the entire string matches the pattern 
    email=input("\n\n Enter the gmail to validate: ")

    if (re.search(pattern,email)):
        print("Valid email: {}".format(email))
    else:
        print("Invalid email: {}".format(email))