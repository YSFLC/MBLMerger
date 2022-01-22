import sys
import os
import glob
from PIL import Image


savepath = "./res"
beforename = "スライド"
aftername = ".PNG"


def merge(imgpath: str):
    print(imgpath)
    print(glob.glob(imgpath))

    print(imgs)

    for i in range(len(glob.glob(imgpath))):
        




if __name__ == "__main__":
    args = sys.argv
    if 2 == len(args):
        args[1] = os.path.abspath(args[1])
        if os.path.exists(args[1]):
            merge(args[1]+"/*")
        else:
            print("指定されたフォルダは存在しません")
            exit(2)
    else:
        print("引数に画像sの親フォルダのパスを与えてください")
        exit(1)
