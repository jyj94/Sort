import random, time
import matplotlib.pyplot as plt

class testCase:
    def __init__(self):
        self.listSize = 0
        self.list = []
        self.beforeTime = 0
        self.afterTime = 0

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def MergeSort(list):
    listLen = len(list)
    if listLen <= 1:
        return list
    mid = listLen // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = MergeSort(leftList)
    rightList = MergeSort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

lists = []
for i in range(10, 1001, 10): #10에서 1000까지(100번)
    
    case = testCase()
    case.listSize = i
        
    for i in range(1, i):
        case.list.append(random.randrange(1, 10000))
    
    print("original List : ", case.list)
    case.beforeTime = time.time()
    case.list = MergeSort(case.list)
    case.afterTime = time.time()
    print("sorted List : ", case.list)
    lists.append(case)

x = []
for i in range(0, 100):
    x.append(lists[i].listSize)
y = []
for i in range(0, 100):
    y.append(lists[i].afterTime - lists[i].beforeTime)

plt.plot(x, y) 
plt.savefig('./img/mergeSortTime.png')