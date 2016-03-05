import random, time
import matplotlib.pyplot as plt

class testCase:
    def __init__(self):
        self.listSize = 0
        self.list = []
        self.compareCount = 0
        self.beforeTime = 0
        self.afterTime = 0

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heapSort(unsorted):
    n = len(unsorted)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted
    
lists = []
for i in range(10, 1001, 10): #10에서 1000까지(100번)
    
    case = testCase()
    case.listSize = i
        
    for i in range(1, i):
        case.list.append(random.randrange(1, 10000))
    
    print("original List : ", case.list)
    case.beforeTime = time.time()
    case.list = heapSort(case.list)
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
plt.savefig('./img/heapSortTime.png')