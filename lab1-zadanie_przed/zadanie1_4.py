import sys


def repetition_list(list):
    newlist = []
    oldlist = list.split(',')
    for i in oldlist:
        for j in range(0, int(i)):
            newlist.append(int(i))
    return newlist


print(repetition_list(sys.argv[1]))
