import sys


def list_segmentation(list):
    arr = list.split(',')
    sum = 0
    newarr = []
    for i in arr:
        sum += int(i)
    for i in arr:
        if (int(i) >= (sum/len(arr))):
            newarr.append(int(i))
    return newarr


print(list_segmentation(sys.argv[1]))
