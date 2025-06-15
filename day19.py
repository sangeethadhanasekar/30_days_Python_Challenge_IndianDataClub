# 🎯 Challenge
# -  Download multiple files concurrently using threads
import urllib.request
import threading
import time
file_path_number=64 # implementation of shared variable
lock=threading.Lock() #lock initialization

def download1(url1):   
    global file_path_number
    print("downloading image1.....")
    lock.acquire()  #lock acquired so that the number is fixed until the image path for this thread is created...
    # or else other thread downloading in same name
    file_path_number+=1
    file_path= str(chr(file_path_number))+"_image.png"
    lock.release()
    time.sleep(0.5)
    urllib.request.urlretrieve(url1,file_path)
    print(f"downloaded {file_path}  -->image1")

def download2(url2):
    global file_path_number
    print("downloading image2.....")
    with lock: #another method to acquire lock (here by default it got released as we using "with")
        file_path_number+=1
        file_path=str(chr(file_path_number))+"_image.png"
    time.sleep(10)
    urllib.request.urlretrieve(url2,file_path)
    print(f"downloaded {file_path}  -->image2")

def download3(url3):
    global file_path_number
    print("downloading image3.....")
    file_path_number+=1 # not using any lock 
    file_path=str(chr(file_path_number))+"_image.png"
    time.sleep(5)
    urllib.request.urlretrieve(url3,file_path) 
    print(f"downloaded {file_path} -->image3")

if __name__=="__main__":
    url1 = 'https://cdn-icons-png.flaticon.com/256/7163/7163510.png' #Alphabet A image
    url2='https://cdn-icons-png.flaticon.com/256/7163/7163512.png' #Alphabet B image
    url3='https://cdn-icons-png.flaticon.com/256/7163/7163513.png' #Alphabet C image

    t1=threading.Thread(target=download1,args=(url1,))
    t2=threading.Thread(target=download2,args=(url2,))
    t3=threading.Thread(target=download3,args=(url3,))
    print("\n\n\n")
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("all images downloaded!!")



