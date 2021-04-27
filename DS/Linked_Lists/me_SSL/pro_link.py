class ListNode:
    def __init__(self, x=None):
        if isinstance(x, list):
            self.val = None
            for n in x:
                self.next = self = ListNode(n)
        else:
            self.val = x
            self.next = None

    def __str__(self):
        lst = []
        self = self.next
        while self:
            lst.append(self.val)
            self = self.next
        return ' -> '.join(map(str, lst))


def reverseList(A, B):
    head = A
    while head.next:
        node = head.next
        for _ in range(B - 1):
            next_node = node.next
            if next_node:
                node.next = next_node.next
                next_node.next = head.next
                head.next = next_node
        head = node
    return A


lst = [1, 2, 3, 4, 5, 6]
print(reverseList(ListNode(lst), 2))
print(reverseList(ListNode(lst), 3))
