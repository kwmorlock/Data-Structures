"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        nodes = ListNode(value)
        if not self.head and not self.tail:
            self.head = nodes
            self.tail = nodes
        else:
            nodes.next = self.head
            nodes.prev = nodes
            self.head = nodes

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None: #if there is no node, we will return none
            return None
        data = self.head.value #value is coming from the node, this line is if there is only one node on the list
        if self.head is self.tail: #if there is a node present
            self.head = None
            self.tail = None
        else: #if more than one node we have to delete it
            self.delete(self.head) #self is refering to the list node
        self.length -= 1
        return data
         

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        nodes = ListNode(value)
        if not self.head and not self.tail:
            self.head = nodes
            self.tail = nodes
        else:
            nodes.prev = self.tail
            self.tail.next = nodes
            self.tail = nodes

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        norm_tail_value, dele_tail = self.tail.value, self.tail.prev
        self.tail.delete()
        self.tail = dele_tail
        if self.tail is None:
            self.head = None
        return norm_tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # pass
        node.delete()#next = to none and prev = to none, head.prev point to node (head nothing, tail reassigntail, and whether its either the points need to be changed and set to head)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
