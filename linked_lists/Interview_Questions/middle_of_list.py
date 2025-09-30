


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
        traverse = (self.size-1)//2
        temp = self.head
        for i in range(traverse):
            temp = temp.next_node
        return temp
            
        # your implementation goes here !!!

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node
   
         

if __name__ == '__main__':
    
    ll = LinkedList()
    # ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    ll.traverse_list()
    print("Middle")
    print(ll.get_middle_node().data)