
"""Single Linked List"""

#Lists are made up of objets called nodes
#You must first make a node class
class Node(object):
    #Node constructor
    def __init__(self, val):
        #a node must contain a value
        self.val = val
        #This is a single linked list, so the node must have a pointer to the next node in a list only (initially to nil)
        self.next = None
        
#Singly linked list object
class LinkedList(object):
    #constructor
    def __init__(self):
        #create an initial head pointer (initially to nil)
        self.head = None
        #must also contain a size value (initially at 0)
        self.size = 0
        
    #add at head function for a linked list
    #adds a node to the head of the list
    def addAtHead(self, val):
        #create a node
        node = Node(val)
        
        #new node's next points to current head first, then head points to new node
        node.next = self.head
        self.head = node
            
        #size of list is increased by 1
        self.size += 1
        
    #add at tail function for a linked list
    #adds a node to the end of the list
    def addAtTail(self, val):
        #create a pointer initially to head
        current = self.head
        
        #if the list is empty make a new node the head
        if current is None:
            self.head = Node(val)
        else:
            #loop will go through entire list until it reaches the last value of the list
            while current.next is not None:
                current = current.next
            #set the next pointer of current to the new node
            current.next = Node(val)

        self.size += 1
        
    #add at index function for linked list
    #this adds a new node to a specified spot in the list (between 0 and size - 1)
    def addAtIndex(self, index, val):
        #if the index is out of range return nothing
        if index < 0 or index >= self.size:
            return
        
        #if the index is 0 add it at the head
        if index == 0:
            self.addAtHead(val)
            
        #if index is somewhere in the middle
        else:
            #create new node
            node = Node(val)
            
            #create a pointer initially at the head
            current = self.head
            
            #increment through the list until you are at the node before the index
            # setting range = index - 1 means that it will increment index - 2 times, bringing you to element right before
            for i in range(index - 1):
                current = current.next
            
            #once at array before index, set new node's next to point at current's next
            node.next = current.next
            
            #next set current's next to point at the new node
            current.next = node
            
            #increase list size by 1
            self.size += 1
            
    #delete at index function
    #this deletes a node at a certain index from the list
    def deleteAtIndex(self, index):
        #if list is empty or index is out of range return nothing
        if index < 0 or index >= self.size:
            return        
        
        #create a pointer initially at head
        current = self.head
        
        #if index is at the head, delete the head without running for loop
        if index == 0:
            self.head = current.next
        #if it is anything else
        else:
        #increment through the list until you reach the node right before the one you want to delete
        #Can use the range index - 1 here as well
            for i in range(index - 1):
                current = current.next
            
            #Set current's next to point at the index's next (its next next if you will)
            current.next = current.next.next
        
        #decrease the size of the array by 1
        self.size -= 1
        
    #get value at index function
    #this gets a value at a specified index (returns int)
    def get(self, index) -> int:
        #if list is empty or the index is out of range, return -1
        if index < 0 or index >= self.size:
            return -1
        
        #create a pointer initially pointing at the head
        current = self.head
        
        #traverse through list until you reach desired index
        #this time make sure you increment to a range index (this will move the pointer index - 1 times)
        for i in range(index):
            current = current.next
            
        return current.val
    
    #print list function
    #this function prints the list of values in the linked list
    def printList(self):
        #if the list is empty
        if self.size == 0:
            print('Sorry bud, list is empty')
        #if it isn't empty
        else:
            #set a pointer to the head
            current = self.head
            
            #traverse through all elements of the list and print their value
            #since index of the tail = size - 1 set the range to size to go to each element of the list
            for i in range(self.size):
                if i == self.size - 1:    
                    print(current.val)
                else:
                    print(current.val, end = ', ')
                #go to next value
                current = current.next
        
        
## test if it works ##

#create a linked list
list = LinkedList()

#print for an empty list
list.printList()

#try to get a value from an empty list
print(list.get(0))

#add an element to the list
list.addAtHead(5)
list.printList()

#add three more elements to the front of the list
list.addAtHead(4)
list.addAtHead(3)
list.addAtHead(7)
list.printList()

#add three elements to the end of the list
list.addAtTail(9)
list.addAtTail(8)
list.addAtTail(6)
list.printList()

#add three elements to the middle of the list
list.addAtIndex(2, 11)
list.addAtIndex(3, 13)
list.addAtIndex(4, 14)
list.printList()
        
#insert at front using index 
list.addAtIndex(0, 15)
list.printList()

#insert at end using index (should not replace tail)
list.addAtIndex(10, 34)
list.printList()

#delete from list
list.deleteAtIndex(1)
list.printList()

#delete head
list.deleteAtIndex(0)
list.printList()
        
#delete tail
list.deleteAtIndex(9)
list.printList()        
        
            