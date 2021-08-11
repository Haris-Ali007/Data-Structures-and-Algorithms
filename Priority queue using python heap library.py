"""
This is an implementation of Priority queue using
heapq library of python. See theory in Python Cookbook.
Notes:
-Index: Index will sort items with same priority level. 
        By using increasing index items with same priority level will
        be sorted using the order of their arrival.
-We insert a tuple of priority, value and index in our queue.
"""
import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # -priority sorts items from highest to lowest.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    # awlays return items with smallest priority
    def pop(self):
        return heapq.heappop(self._queue)[-1]


# Example use case of priority queue.
class Item:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

######################################
######### Runnning Priority Queue
######################################

q = PriorityQueue()
q.push(Item('Foo'), 1)
q.push(Item('baz'), 10)
q.push(Item('bar'), 3)
q.push(Item('block'), 2)
print(q.pop())
print(q.pop())
print(q.pop())

