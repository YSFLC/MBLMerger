import sys
import os


def merge():
    print()


if __name__ == "__main__":
    args = sys.argv
    if 2 == len(args):
        merge()
    else:
        print("引数に画像sの親フォルダの絶対パスを与えてください")
