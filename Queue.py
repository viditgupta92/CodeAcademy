class node:
    def __init__(self):
        self.data = None
        self.next = None

class queue:
    def __init__(self):
        self.first = node()
        self.last = node()

    def add(self, item):
        n = node()
        n.data = item
        self.last.next = n
        self.last = n
        if self.first.data == None:
            self.first = self.last

    def remove(self):
        if self.first.data == None:
            return 0
        else:
            item = self.first.data
            self.first = self.first.next
            if self.first == None:
                self.last = None
            return item

    def peek(self):
        if self.first == None:
            return 0
        else:
            return self.first.data

    def isEmpty(self):
        return self.first.data == None

    def print_queue(self):
        temp = self.first
        while temp != None:
            print(temp.data)
            temp = temp.next

q1 = queue()
q1.add(1)
q1.add(2)
q1.add(3)
q1.print_queue()
q1.remove()
q1.remove()
q1.remove()
print(q1.peek())
q1.print_queue()



