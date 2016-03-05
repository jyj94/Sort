import random, time
import matplotlib.pyplot as plt

class testCase:
    def __init__(self):
        self.listSize = 0
        self.list = []
        self.compareCount = 0
        self.beforeTime = 0
        self.afterTime = 0

def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    lesser_list, equal_list, greater_list = [], [], []
    for num in list:
        if num < pivot:
            lesser_list.append(num)
        elif num > pivot:
            greater_list.append(num)
        else:
            equal_list.append(num)
    return quickSort(lesser_list) + equal_list + quickSort(greater_list)
    
lists = []
for i in range(10, 1001, 10): #10에서 1000까지(100번)
    
    case = testCase()
    case.listSize = i
        
    for i in range(1, i):
        case.list.append(random.randrange(1, 10000))
    
    print("original List : ", case.list)
    case.beforeTime = time.time()
    case.list = quickSort(case.list)
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
plt.savefig('./img/quickSortTime.png')