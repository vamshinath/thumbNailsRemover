#!/usr/python3
import os,sys,time
from PIL import Image

def scanImages():

    imgsGifs=[]

    for root,dirs,files in os.walk("."):
        for fl in files:
            flnm_lower=fl.lower()
            if ".jpg" in flnm_lower or ".png" in flnm_lower or ".jpeg" in flnm_lower or ".gif" in flnm_lower:
                imgsGifs.append(fl)
    return imgsGifs

def removeImages(imgs):

    for img in imgs:
        tmp = Image.open(img).size
        print(tmp)
        time.sleep(10)




def main():
    
    os.chdir(sys.argv[1])

    imgs=scanImages()

    removeImages(imgs)


if __name__ == "__main__":
    main()