"""
-This is a simple implementation of a linked list in python.
-Linked List works by using pointers to locate the next 
 node of the list. This creates a dynamic list.

 a->b->c->d->None

 The last node is always the null node. Here we are
 always navigating next nodes with our last pointer.
 You can also call it current node.

 Reverse:
 An important functionality of liked list. Here we are trying to 
 maintain two pointers and moving them ahead as we change their
 direction one by one.
"""

class Node:

    def __init__(self, data, next=None):
        self.data= data
        self.next= next

class LinkedList:


    def __init__(self):
        self.head= None
        self.size= 0

    def insert(self, node):
        last= self.head
        #to insert value at last node we
        if self.head==None:
            self.head=node
            node.next=None
            self.size+= 1
        else:
            while(last.next!=None):
                last= last.next
            last.next= node
            node.next= None
            self.size+= 1

    def insert_at(self, node, i):
        if i < 1 and i >= self.size:
            print("Invalid position to enter node....")
        else:
            if i==1:
                node.next= self.head
                self.head= node
                self.size = self.size + 1
            else:
                last=self.head
                pos=1
                while(pos!=i):
                    prev= last
                    last= last.next
                    pos = pos + 1
                prev.next= node
                node.next= last
                self.size = self.size + 1
        
    def remove_at(self, i):
        if i < 1 and i > self.size:
            print("Invalid position to remove node....")
        else:
            if i==1:
                remove= self.head
                self.head= self.head.next
                self.size = self.size - 1 
                del(remove)
            else:
                last= self.head
                pos=1 
                while(pos!=i):
                    prev= last
                    last= last.next
                    pos = pos + 1
                prev.next = last.next
                self.size = self.size - 1
                del(last)

    def reverse(self):
        #this is an important function of reversing a linked list
        prev= None
        last= self.head
        while (last!=None):
            temp= last.next
            last.next= prev
            prev= last
            last= temp
        self.head= prev


    def print_list(self):
        last= self.head
        while(last.next!= None):
            print(last.data,'-> ',end="")
            last= last.next
        #this prints node value when its pointer is None
        print(last.data)
    


    #TODO: add sorting. 

 

ll = LinkedList()

for i in range(10):

    ll.insert(Node(i))
            
ll.print_list()
print("Size", ll.size)

ll.insert_at(Node(15), 3)

ll.print_list()
print("Size", ll.size)

ll.remove_at(4)

ll.print_list()
print("Size", ll.size)

print("Reversed list")
ll.reverse()
ll.print_list()



