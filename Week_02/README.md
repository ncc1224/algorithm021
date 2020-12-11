'''堆排序'''
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 
 
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
for i in range(n):
    print("%d" % arr[i]),

import sys
class BinaryHeap: 
  
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.Heap = [0]*(self.capacity + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos//2
  
    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def heapifyDown(self, pos): 
  
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.heapifyDown(self.leftChild(pos)) 
  
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.heapifyDown(self.rightChild(pos)) 
  
    def insert(self, element): 
        if self.size >= self.capacity : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
   
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.heapifyDown(pos) 
  
    def delete(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.heapifyDown(self.FRONT) 
        return popped 
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self): 
        return self.size == self.capacity
    
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = BinaryHeap(9)
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
    print("-----------")
    minHeap.Print() 
    print("The Min val is " + str(minHeap.delete()))

"""heapq的实现"""

def heappush(heap, item):
    #Push item onto heap, maintaining the heap invariant.
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
def heappop(heap):
    #Pop the smallest item off the heap, maintaining the heap invariant.
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # 左节点，默认替换左节点
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1  # 右节点
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos  # 当右节点比较小时，应交换的是右节点
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def heapify(x):
    #Transform list into a heap, in-place, in O(len(x)) time.
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
