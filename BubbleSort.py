import random, time
import matplotlib.pyplot as plt

class testCase:
    def __init__(self):
        self.listSize = 0
        self.list = []
        self.compareCount = 0
        self.beforeTime = 0
        self.afterTime = 0

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

def bubbleSort(Case):
    listLen = len(case.list)

    for i in range(listLen, 0, -1):
        for j in range(0, i - 1):
            case.compareCount += 1
            if case.list[j] > case.list[j + 1]:
                swap(case.list, j, j + 1)
    
lists = []
for i in range(10, 1001, 10): #10에서 1000까지(100번)
    
    case = testCase()
    case.listSize = i
        
    for i in range(1, i):
        case.list.append(random.randrange(1, 10000))
    
    print("original List : ", case.list)
    case.beforeTime = time.time()
    bubbleSort(case)
    case.afterTime = time.time()
    print("sorted List : ", case.list)
    lists.append(case)

x = []
for i in range(0, 100):
    x.append(lists[i].listSize)
y = []
y2 = []
for i in range(0, 100):
    y.append(lists[i].afterTime - lists[i].beforeTime)
    y2.append(lists[i].compareCount)

plt.plot(x, y) 
plt.savefig('./img/bubbleSortTime.png')
plt.cla()
plt.plot(x, y2)
plt.savefig('./img/bubbleSortCount.png')
print("test")