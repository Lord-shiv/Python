class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SLLNode object: data= {self.data}"

    def get_data(self):
        """ Return self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """ set new data """
        self.data = new_data

    def get_next(self):
        """ Return the self.next attribute """
        return self.next

    def set_next(self, new_next):
        """ set next vlue """
        self.next = new_next
