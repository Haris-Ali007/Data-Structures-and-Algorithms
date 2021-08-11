"""
Heap is a data structure that is used to store elements
in a way that it always satisfies heap invariant.
Heap invariant defines how elements would be arranged. A
Max Heap would always output max element from heap.
Min Heap would always output min element from heap.
"""

class BinaryHeap:

    def __init__(self):
        self.array = []
        self.size = 0
        self.capacity = 10

    def swap(self, array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]
    
    def parentIdx(self, idx):
        return (idx - 1) // 2
    
    def leftChild(self, idx):
        return (idx * 2) + 1

    def rightChild(self, idx):
        return (idx * 2) + 2

    def parentExist(self, idx):
        if self.parentIdx(idx) < 0:
            return False
        else:
            return True

    def leftExist(self, idx):
        if (self.leftChild(idx) < self.size):
            return True
        else:
            return False
    
    def rightExist(self, idx):
        if (self.rightChild(idx) < self.size):
            return True
        else:
            return False
       
    def heapifyUpwards(self):
        # size indicates last index where we added our value
        curr_idx = self.size
        while(self.parentExist(curr_idx) and self.array[self.parentIdx(curr_idx)] >  self.array[curr_idx]):
            self.swap(self.array, self.parentIdx(curr_idx), curr_idx)
            curr_idx = self.parentIdx(curr_idx)

    def heapifyDownwards(self):
        parent_idx = 0
        # because if left doesnt exist there is no way we would have right node
        while(self.leftExist(parent_idx)):
            # we consider left to be smallest
            smallerChild = self.leftChild(parent_idx)
            # if right is smaller we update our smaller child
            if (self.rightExist(parent_idx) and self.array[self.rightChild(parent_idx)] < self.array[smallerChild]):
                smallerChild = self.rightChild(parent_idx)
            # if we dont need any change we break out
            if (self.array[parent_idx] < self.array[smallerChild]):
                break
            else:
                self.swap(self.array, parent_idx, smallerChild)
                parent_idx = smallerChild

    def insert(self, value):
        # if self.size > self.capacity:
            # define extendHeap() function
            # function should double the heap size.
            # as here our list expands dynamically so we dont need it.
        self.array.append(value)
        # now we bubble up to satisfy heap invariant 
        self.heapifyUpwards() 
        self.size += 1

    def remove(self):
        if (self.size - 1 < 0):
            print("Heap empty.")
        else:
            # we remove from first
            print(self.array[0])
            # we exchange with last value of array
            self.array[0] = self.array[self.size - 1] 
            # remove last one
            self.array.pop()
            self.size -= 1
            # now we bubble down to adjust heap
            self.heapifyDownwards()

    def printHeap(self):
        print(self.array)

bh = BinaryHeap()
bh.insert(5)
bh.printHeap()
bh.insert(1)
bh.printHeap()
bh.insert(3)
bh.printHeap()
bh.insert(10)
bh.printHeap()
bh.insert(2)
bh.printHeap()
bh.remove()
bh.printHeap()
bh.remove()
bh.printHeap()
bh.remove()
bh.printHeap()
bh.remove()
bh.printHeap()
