#!/usr/python3
import os,sys,time
from PIL import Image
import threading
def scanImages():

    imgsGifs=[]

    for root,dirs,files in os.walk("."):
        for fl in files:
            flnm_lower=fl.lower()
            if ".jpg" in flnm_lower or ".png" in flnm_lower or ".jpeg" in flnm_lower or ".gif" in flnm_lower:
                fl=os.path.abspath(os.path.join(root,fl))
                imgsGifs.append(fl)
    return imgsGifs

def removeImage(img):

    tmp = Image.open(img).size
    if int(tmp[0]) < 512 and int(tmp[1]) < 512:
        os.remove(img)




def main():
    
    os.chdir(sys.argv[1])

    imgs=scanImages()

    for img in imgs:
        print(img)
        threading.Thread(target=removeImage,args=(img,)).start()
        while threading.active_count() > 10:
            time.sleep(1.5)


if __name__ == "__main__":
    main()