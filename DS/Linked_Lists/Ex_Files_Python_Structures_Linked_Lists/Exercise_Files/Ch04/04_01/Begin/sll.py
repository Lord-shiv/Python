class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data
        parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next
        parameter."""
        self.next = new_next


class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL object: head={}".format(self.head)

    def is_empty(self):
        return self.head is None  # self.head == None

    def add_front(self, new_data):
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """ Traverse the linked list return the number of nodes
            The time complexity is O(n)
        """
        size = 0
        if self.head is None:
            return 0
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """ Traverse the list and return True 
            The time complexity if O(n)
        """
        if self.head is None:
            return "Linked List is empty. No nodes to search"
        current = self.head
        while current is not None:
            # The Node's data matches waht we are looking for
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()

        return False
        # The node's data does't match

    def remove(self, data):
        """ remove the first occurence of node  
            Time complexity O(n) """
        if self.head is None:
            return "The linked list is empty no Need to remove"

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True

            else:
                if:
                    current.get_next() == None:
                    return "A node with that data value not present"

                else:
                    previous = current
                    current = current.get_next

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.next())
