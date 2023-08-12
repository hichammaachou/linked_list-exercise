class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'<data: {self.data}>'

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current:
            current = current.next
        current.next = new_node    

    def length(self):
        if not self.head:
            return 'Empty!'
        count = 0
        current = self.head
        while current:
            count += 1 
            current = current.next
        return count    
    
l = Linkedlist()
l.append(15)
l.append(5)
print(l.length())
