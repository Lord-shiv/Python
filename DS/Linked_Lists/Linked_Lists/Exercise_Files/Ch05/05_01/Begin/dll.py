class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

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

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with
        new_previous parameter."""
        self.previous = new_previous


class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "DLL object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

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

    def search(self):
        """ Traverse the list and return True 
            The time complexity if O(n) """
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

    def add_front(self, new_data):
        temp = DLLNode(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp

    def remove(self, data):
        """" Remove the first occurence of the node that contain data
            Time complexity = O(n)
        """
        if self.head is None:
            return "Linked List is already empty"

        current = self.head
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data note present"
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous)
