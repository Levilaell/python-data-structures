class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if self.head is None:
            return '[]'
        else:
            last = self.head

            return_string = f'[{last.value}'

            while last.next:
                last = last.next
                return_string += f', {last.value}'
            
            return_string += ']'

        return return_string

    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self):
        counter = 0
        last = self.head
        while last is not None:
            counter += 1
            last = last.next
        return counter

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)


    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head 
        
        self.head = first_node
 
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)

        else:  
            if self.head is None:
                raise ValueError('Index out of bounds')
            else:
                last = self.head
                for i in range(index - 1):
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    def delete(self, value):
        if self.head is None:
            return


        if self.head.value == value:
            self.head = self.head.next
            return

        last = self.head
        while last.next is not None:
            if last.next.value == value:    
                to_delete = last.next
                last.next = to_delete.next
                return

    def pop(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            val = self.head.value
            self.head = None
            return val
        
        prev = self.head
        curr = self.head.next

        while curr.next is not None:
            prev = curr
            curr = curr.next

        val = curr.value
        prev.next = None
        return val

    def get(self, index):
        if index < 0: 
            return None
        
        last = self.head

        for i in range(index):
            if last is None:
                return None
            last = last.next
        
        return last.value

    def print(self):
        pass

if __name__ == '__main__':
    ll = LinkedList()

    ll.append(10)
    ll.append(10)
    ll.append(30)

    print(ll.__repr__())
    print(ll.pop())
    print(ll.__repr__())