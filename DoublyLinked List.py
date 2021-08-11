"""
In a doubly linked list each node has the reference 
both its successor and predecessor node. It makes 
navigation, insertion and deletion easier but it
takes double the amount of regular space.

Head: back refrence is null
Tail: front refrence is null.

null <-> a <-> b <-> c <-> null
"""

class Node:

    def __init__(self, value=None):
        self.value = value
        self.back = None
        self.front = None

class DoublyLinkedList:


    def __init__(self):
        self.head = None
        self.size = 0


    def insert(self, node):
        if (self.head == None):
            self.head = node
            self.size += 1
        else:
            curr = self.head
            while (curr.front != None):
                curr = curr.front
            node.back = curr
            curr.front = node
            self.size += 1


    def insert_at_i(self, node, i):
        if (i <= 0 or i >self.size):
            print("Invalid position")
        #making seperate case for i==1 
        elif (i==1): 
            node.back = None
            node.front = self.head
            self.head.back = node
            self.head = node
            self.size += 1
        #insertion require change of 4 pointers
        else:
            curr = self.head
            prev = self.head.back
            pos = 1
            while (pos!=i):
                prev = curr
                curr = curr.front
                pos += 1
            node.back = prev
            node.front = curr
            prev.front = node
            curr.back = node
            self.size += 1
                

    def remove_at_i(self, i):
        if (i<=0 or i>self.size):
            print("Invalid position")
        elif (i==1):
            temp = self.head
            self.head = self.head.front
            self.head.back = None
            temp.front = None
            self.size -= 1
        elif (i==self.size):
            curr = self.head
            prev = self.head.back
            while(curr.front!=None):
                prev = curr
                curr = curr.front
            prev.front = None
            curr.back = None
            self.size -= 1
        else:
            curr = self.head
            prev = self.head.back
            pos  = 1
            while(pos!=i):
                prev = curr
                curr = curr.front
                pos += 1
            temp = curr.front
            prev.front = temp
            temp.back = prev
            curr.front = None
            curr.back = None
            self.size -= 1
            
    def reverse(self):
        curr = self.head
        while(curr.front != None):
            prev = curr.back
            curr.back = curr.front
            curr.front = prev
            curr = curr.back
        curr.front = curr.back
        curr.back = None
        self.head = curr
        #TO-DO correct this method to complete the code


    def print_list(self):
        if self.size == 0:
            print("Cannot print. List Empty")
        else:
            curr = self.head
            while (curr.front != None):
                print(curr.value,"<-> ",end="")
                curr = curr.front
            print(curr.value)
            




############################
###TEST INSTRUCTIONS########
############################

dll = DoublyLinkedList()
dll.insert(Node(4))
dll.insert(Node(3))
dll.insert(Node(10))
dll.print_list()
print(dll.size)
dll.insert_at_i(Node(100), 2)
dll.print_list()
dll.insert_at_i(Node(100), 4)
dll.print_list()
dll.insert_at_i(Node(134), 1)
dll.print_list()
dll.remove_at_i(6)
dll.reverse()
print('List Reversed')
dll.print_list()
dll.remove_at_i(5)
dll.print_list()
dll.remove_at_i(1)
dll.print_list()
dll.reverse()
print('List Reversed')
dll.print_list()


        