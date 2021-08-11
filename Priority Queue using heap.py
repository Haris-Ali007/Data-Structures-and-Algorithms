"""
Priority Queue is an Abstract Data Structure that is used
to access elements based on a particular priority.
This is achieved using a heap data strcture. Here we will 
use binary heap to create a priority queue. For implementing
a binary heap we will use array based implementation.

"""
class Priority_queue:

    def __init__(self, criteria = "Min"):
        self.criteria = criteria
        self.bh = self.BinaryHeap()

    def push(self, value):
        if (self.criteria == "Max"):
            self.bh.insert(-value)
        else:
            self.bh.insert(value)
    
    def pop(self):
        if (self.bh.heapSize() <= 0):
            print("Empty Queue")
        else:
            if (self.criteria == "Max"):
                print(-self.bh.remove())
            else:
                print(self.bh.remove())

 ####### Using Nested / Inner classes #######   
    
    class BinaryHeap:

        def __init__(self):
            self.array = []
            self.size = 0

        def heapSize(self):
            return self.size

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
            self.array.append(value)
            # now we bubble up to satisfy heap invariant 
            self.heapifyUpwards() 
            self.size += 1
        
        def remove(self):
            # we remove from first
            top_element = self.array[0]
            # we exchange with last value of array
            self.array[0] = self.array[self.size - 1] 
            # remove last one
            self.array.pop()
            self.size -= 1
            # now we bubble down to adjust heap
            self.heapifyDownwards()
            return top_element

        def printHeap(self):
            print(self.array)

pq = Priority_queue("Max")
pq.push(5)
pq.push(1)
pq.push(3)
pq.push(10)
pq.push(2)
pq.pop()
pq.pop()
pq.pop()
pq.pop()
pq.pop()
pq.pop()

