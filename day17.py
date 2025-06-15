# 🎯 Challenge
# -  Build a context manager for safe file handling

class ContextManager():
    def __init__(self,name,mode):
        self.name=name
        self.mode=mode
        self.file=None


    def __enter__(self):
        print(f"\n\nfile {self.name} is opening in {self.mode} mode...")
        self.file=open(self.name,self.mode)
        self.file.write("inside __enter__ \n")
        return self.file
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        print(f"file {self.name} is closed!")

if __name__=="__main__":
    with ContextManager("Trail.txt",'a') as file:
        print(file.name)
        file.write("hello! welcome!!")
    print("Done")



