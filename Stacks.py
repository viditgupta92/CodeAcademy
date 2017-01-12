class node:
    def __init__(self):
        self.data = None
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self,item):
        n = node()
        n.data = item
        n.next = self.top
        self.top = n

    def pop(self):
        if self.top == None:
            return 0
        else:
            item = self.top.data
            self.top = self.top.next
        return item

    def peek(self):
        if self.top == None:
            return 0
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None

    def print_stack(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

s1 = stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.print_stack()
s1.pop()
s1.pop()
print(s1.peek())
print(s1.isEmpty())




