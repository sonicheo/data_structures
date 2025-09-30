
class Node():
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.last_node = None



class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0

    # O(1)
    def insert_start(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.last_node = new_node
            self.head = new_node
            
    
    # O(N)
    def insert_end(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.last_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    
    # O(1)
    def size_of_list(self):
        return self.num_of_nodes
    
    # O(N)
    def traverse_forward(self):
        temp_node = self.head
        
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next_node
    
    
    # O(N)
    def traverse_backwards(self):
        temp_node = self.tail
        
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.last_node
    # O(N)
    def remove(self, data):
        
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next_node
            self.head.last_node = None
        else:
            temp_node = self.head.next_node
            while(temp_node and temp_node.data != data):
                temp_node = temp_node.next_node
            if temp_node.data == data and temp_node.next_node:
                temp_node.last_node.next_node = temp_node.next_node
                temp_node.next_node.last_node = temp_node.last_node
            elif temp_node.data == data:
                temp_node.last_node.next_node = None
            
            




if __name__ == '__main__':
    
    ll = LinkedList()
    ll.insert_start(10)
    ll.insert_start(15)
    ll.insert_start(12312)
    ll.insert_end(200)
    ll.insert_end(2300)
    ll.insert_end(2400)
    print("------------------------Forward------------")
    ll.traverse_forward() 
    print("------------------------Backward------------")
    ll.traverse_backwards()
    print("------------------------removing-------------")
    ll.remove(2300)
    ll.remove(2400)
    ll.remove(12312)
    ll.traverse_forward() 