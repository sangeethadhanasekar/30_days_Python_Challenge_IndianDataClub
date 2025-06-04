'''🎯 Challenge
- Count word frequencies in a text file'''

# appending message into text file
'''with open("day7.txt","a") as f:
     message=input("Enter the passage to be inserted into the file: ")
     f.write(message)
'''
import re
# reading text document lines  

word=dict()
with open("day7.txt","r") as r:
     messagelines=r.readline()
     r.close()
     
# counting words
word_count={}
regex_message=re.sub(r"[^\w\s]",' ',messagelines).lower() #got help from internet
for word in regex_message.split(" "):
     if word not in word_count.keys():
       word_count[word]=1
     else:
          word_count[word]+=1

# printing words occurences in sorted order        
#    for x in sorted(word_count.keys(),reverse=True): -->in reverse order
for x in sorted(word_count.keys(),reverse=False):
     print(f"{x} : {word_count[x]}")

