# 🎯 Challenge
# - Generate a random 8-character password


#Method 1:
#result=''.join([(chr(random.randrange(0,127))) for i in range(8)]) -->it will include non-printable characters 
''' | ASCII Range | Description                             | Printable?                                            |
    | ----------- | --------------------------------------- | ----------------------------------------------------- |
    | 0-31        | Control characters (e.g., `\x06`, `\n`) |  No                                                   |
    | 32          | Space (`' '`)                           | Yes                                                   |
    | 33-126      | Printable symbols, digits, letters      | Yes                                                   |
    | 127         | DEL (Delete)                            | No                                                    |
    | 128-255     | Extended ASCII (varies)                 | Not guaranteed to be printable in all environments    |'''

import  random 
result=''.join([(chr(random.randrange(33,127))) for i in range(8)])
print("A random 8-character password:",result)


#Method 2:
'''import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(all_chars,k=8))'''