nazov = input("zadaj názov súboru: ")
import os

#C:\\Program Files

def path(subor, depth=0):
    for item in os.listdir(subor):
        if os.path.isdir(subor + "\\" + item) and item[0] not in ".$":
            print("-" * depth, item)
            if os.listdir(subor + "\\" + item):
                path(subor + "\\" + item, depth + 1)

path(nazov)