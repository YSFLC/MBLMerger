from ast import Num
import sys
import os
import glob
from PIL import Image

savepath = "./res/"
beforename = "スライド"
aftername = ".PNG"
minus = 41

def get_concant_h(im1,im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def cropAndSave(l: Image, r:Image, num: Num) -> None:
    l = l.crop((0,0,l.width-minus,l.height))
    r = r.crop((minus,0,r.width,r.height))
    get_concant_h(l,r).save(savepath+str(num)+".png")


def merge(imgpath: str):
    print(imgpath)
    print(glob.glob(imgpath+"/*"))
    os.mkdir(savepath)

    maxnum = len(glob.glob(imgpath+"/*"))
    if maxnum % 2 != 0:
        print("これページ奇数やぞ")
        exit(3)

    imgpath += "/"

    for i in range(maxnum//2):
        if i % 2 == 0:
            print(str(max(i+1, maxnum-i)) + ":" + str(min(i+1, maxnum-i)))
            l = Image.open(imgpath + beforename + str(max(i+1, maxnum-i)) + aftername)
            r = Image.open(imgpath + beforename + str(min(i+1, maxnum-i)) + aftername)
            cropAndSave(l,r,i)

        else:
            print(str(min(i+1, maxnum-i)) + ":" + str(max(i+1, maxnum-i)))
            l = Image.open(imgpath + beforename + str(min(i+1, maxnum-i)) + aftername)
            r = Image.open(imgpath + beforename + str(max(i+1, maxnum-i)) + aftername)
            cropAndSave(l,r,i)


if __name__ == "__main__":
    args = sys.argv
    if 2 == len(args):
        args[1] = os.path.abspath(args[1])
        if os.path.exists(args[1]):
            merge(args[1])
        else:
            print("指定されたフォルダは存在しません")
            exit(2)
    else:
        print("引数に画像sの親フォルダのパスを与えてください")
        exit(1)
