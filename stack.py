class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        curr = self.top

        while curr is not None:
            items.append(str(curr.value))
            curr = curr.next

        return ', '.join(items)

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        
        pop_value = self.top.value
        self.top = self.top.next

        self.size -= 1

        return pop_value
    
    def peek(self):
        if self.top is None:
            return None
        
        return self.top.value
    
    def is_empty(self):
        return self.top is None