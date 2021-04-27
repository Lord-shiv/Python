class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def print_LL(self):
        if self.head is None:
            print("No Elements")
        else:
            n = self.head
            while n is not None:  # to go through each element
                print(f"--> {n.data}", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)  # created new data
        new_node.ref = self.head  # adding that on top
        self.head = new_node  # changing head position to top

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head           # starting from head whole node includeing its data and ref
            # this will traverse untill self.ref == None (last_node)
            while n.ref is not None:
                n = n.ref              # this will change ref to next node
            n.ref = new_node           # setting None ref to new node

    def add_after(self, data, x):  # x for finding the value which after we will add new node
        n = self.head  # n is the top now
        while n is not None:
            if x == n.data:  # we found the value which after..
                break
            n = n.ref   # this is increament  for while loop ++
        if n is None:
            print("node is not present in LL")
        else:
            # node a already has ref to node b and we want to insert data in between SO  node b's address is node a's ref
            new_node = Node(data)

            # new node ref is none by default and its previous node which is x's  ref will be given to it.
            new_node.ref = n.ref
            n.ref = new_node        # so whole new node is now have teh address value of its prev node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked Lis is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:  # [PREVIOUS NODE [DATA]] -----> previous node ref [NEXT NODE [DATA]]  to get x value and to get previous node access prev_node.ref which is next node which has x and prev_node.ref.data  so ref data will be the data which is x
                break
            n = n.ref

        if n.ref is None:
            print("node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("empty list can't perform that can't you see :/")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("again? you crazy??")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref  # inc
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty!")
            return[]
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("nod is not present")
        else:
            n.ref = n.ref.ref


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(23)
LL1.add_after(11, 10)
LL1.add_before(100, 11)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(23)


LL1.print_LL()
