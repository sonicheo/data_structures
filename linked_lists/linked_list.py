
class Node():
    def __init__(self,data):
        self.data = data
        self.next_node = None



class LinkedList():
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # O(1)
    def insert_start(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    # O(N)
    def insert_end(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while(temp_node.next_node):
                temp_node = temp_node.next_node
            temp_node.next_node = new_node
    
    # O(1)
    def size_of_list(self):
        return self.num_of_nodes
    
    # O(N)
    def traverse(self):
        temp_node = self.head
        
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next_node
    
    # O(N)
    def remove(self, data):
        
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next_node
        else:
            temp_node = self.head.next_node
            last_node = None
            while(temp_node and temp_node.data != data):
                last_node = temp_node
                temp_node = temp_node.next_node
            if temp_node.data == data:
                last_node.next_node = temp_node.next_node
            
            




if __name__ == '__main__':
    
    ll = LinkedList()
    ll.insert_start(10)
    ll.insert_start(15)
    ll.insert_start(12312)
    ll.insert_end(200)
    ll.insert_end(2300)
    ll.insert_end(2400)
    ll.traverse() 
    print("------------------------removing-------------")
    ll.remove(2300)
    ll.remove(2400)
    ll.remove(12312)
    ll.traverse() 