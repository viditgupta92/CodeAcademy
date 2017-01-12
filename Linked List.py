import collections

class node:
    def __init__(self):
        self.data = None
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def del_duplicates(self):
        table = []
        temp = self.head
        while(temp.next != None):
            if temp.data in table:
                prev.next = temp.next
            else:
                table.append(temp.data)
                prev = temp
            temp = temp.next


    def list_print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

l1 = linked_list()
l1.add_node(1)
l1.add_node(2)
l1.add_node(2)
l1.add_node(3)

l1.list_print()

l1.del_duplicates()

l1.list_print()

