import random, time, heapq
import matplotlib.pyplot as plt



class MinMaxQuick(object):

    def __init__(self):
        self.content = []

    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    def quick_Sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_Sort(arr, low, pi - 1)
            self.quick_Sort(arr, pi + 1, high)

    def add(self, value):
        self.content.append(value)
        self.quick_Sort(self.content, 0, (len(self.content)-1))


    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]


class MinMaxBinary(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = MinMaxBinary(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = MinMaxBinary(data)
                else:
                    self.right.add(data)
            else:
                self.data = data

    def get_min(self):
        if self.left:
            self.left.get_min()
        else:
            return self.data


    def get_max(self):
        if self.right:
            self.right.get_max()
        else:
            return self.data



class MinMaxHeap(object):

    def __init__(self):
        self.content_min = []
        self.content_max = []
        heapq.heapify(self.content_min)
        heapq.heapify(self.content_max)

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]

    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]


class MinMaxBubble(object):

    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp

    def add(self, value):
        self.content.append(value)
        self.bubble_sort()

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max

if __name__ == '__main__' :

    repetitions = 3
    max_operations = 600
    step = 200
    data = random.randint(0, 1000)

    values_quick_add, values_quick_min, values_quick_max = [], [], []
    values_tree_add, values_tree_min, values_tree_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []

    for rounds in range(100, max_operations, 100):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 1000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxQuick()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_quick_add.append(tot_time_add * 1000)
        values_quick_min.append(tot_time_min * 1000)
        values_quick_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxBinary(data)
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_tree_add.append(tot_time_add * 1000)
        values_tree_min.append(tot_time_min * 1000)
        values_tree_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0

        for repetition in range(repetitions):
            a = MinMaxHeap()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxBubble()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_bubble_add.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)
        
    xlabels = range(100, max_operations, 100)

    plt.plot(xlabels, values_quick_add, label='Add')
    plt.plot(xlabels, values_quick_min, label='Get Min')
    plt.plot(xlabels, values_quick_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of QuickSort Solution")
    plt.show()

    plt.plot(xlabels, values_tree_add, label='Add')
    plt.plot(xlabels, values_tree_min, label='Get Min')
    plt.plot(xlabels, values_tree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of BinaryTree Solution")
    plt.show()

    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()

    plt.plot(xlabels, values_bubble_add, color='b', linestyle='-', label='Add')
    plt.plot(xlabels, values_bubble_min, color='r', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Bubble Sort")
    plt.show()

    plt.plot(xlabels, values_tree_add, color='g', linestyle='-', label='Tree Add')
    plt.plot(xlabels, values_quick_add, color='r', linestyle='-', label='Quick Add')
    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Bubble Add')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Add")
    plt.show()

    plt.plot(xlabels, values_tree_min, color='g', linestyle='--', label='Tree Get Min')
    plt.plot(xlabels, values_quick_min, color='r', linestyle='--', label='Quick Get Min')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Bubble Get Min')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Min")
    plt.show()

    plt.plot(xlabels, values_tree_max, color='g', linestyle='-.', label='Tree Get Max')
    plt.plot(xlabels, values_quick_max, color='r', linestyle='-.', label='Quick Get Max')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Bubble Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Max")
    plt.show()


    plt.plot(xlabels, values_tree_add, color='g', linestyle='-', label='Tree Add')
    plt.plot(xlabels, values_tree_min, color='g', linestyle='--', label='Tree Get Min')
    plt.plot(xlabels, values_tree_max, color='g', linestyle='-.', label='Tree Get Max')

    plt.plot(xlabels, values_quick_add, color='r', linestyle='-', label='Quick Add')
    plt.plot(xlabels, values_quick_min, color='r', linestyle='--', label='Quick Get Min')
    plt.plot(xlabels, values_quick_max, color='r', linestyle='-.', label='Quick Get Max')

    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Bubble Get Min')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Bubble Get Max')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Bubble Add')

    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance all solutions")
    plt.show()