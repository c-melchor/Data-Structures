"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        old_head = self.head
        new_node.next = old_head #You only need new_node.next = self.head but this explains what's going on better
        
        if self.head is None: #Since there was nothing in the list before this, this becomes the entire thing
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        old_head.prev = new_node # self.head.prev = new_node (same thing)
        self.head = new_node #Moves our pointer (head) to the "front". Head is just a variable we use for our computer to point to where we want to start.
        self.length += 1 #increase length
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return

        value = self.head.value #self.head returns the location of the node, not just the value
        
        if self.length == 1:
            self.head = None #The list is empty now
            self.tail = None #The list is empty now
            self.length = 0
            return value

        new_head = self.head.next
        self.head = new_head
        self.head.prev = None #Get rid of the pointer to the old head
        self.length -= 1 #decrease the length

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass