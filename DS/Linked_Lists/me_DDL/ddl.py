class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def print_DLL_reverse(self):
        print()
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(f"<-- {n.data}", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Nothing is list")

        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.ref
            if n is None:
                print("given node is not present is list")
            else:
                new_node = Node(data)
                new_node.nref = n.ref
                new_node.pref = n
                if n.nref is not None:
                    n.nerf.pref = new_node
                n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Nothing is list")

        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.ref
            if n is None:
                print("given node is not present is list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:  # previous reference is empty means that its the begining of the string
                    n.perf.nref = new_node
                else:
                    self.head =  new_node
                n.pref = new_node


dl1 = DoublyLL()
dl1.insert_empty(10)
dl1.add_begin(90)
dl1.add_end(30)
dl1.print_DLL()
dl1.print_DLL_reverse()
