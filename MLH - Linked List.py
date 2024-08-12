class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtStart(self, data): #Inserts the new node as the start of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtStart(data)

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not found")

    def updateNode(self, value, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = value
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = value
            else:
                print("Index not found")

    def remove_head(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head == None:
            return
        

        current_node = self.head
        while current_node.next != None and current_node != None:
            current_node = current_node.next

        current_node = None
        

    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return
        
        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

            if current_node == None:
                return
            else:
                current_node.next = current_node.next.next

    def size_of_list(self):
        size = 0
        current_node = self.head
        if current_node == None:
            return 0
        else:
            while (current_node != None):
                size = size + 1
                current_node = current_node.next
                return size
    
    def print_list(self):
        current_node = self.head
        while (current_node != None):
            print({current_node.data})
            current_node = current_node.next
