
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def appendAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
            self.count += 1
            return
        # last = self.head
        # while last.next:
        #     last = last.next
        last = self.head.previous
        new_node.previous = last
        new_node.next = self.head
        self.head.previous = new_node
        last.next = new_node
        self.count += 1
    
    def appendAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.previous = self.head.previous
            self.head.previous.next = new_node
            self.head.previous = new_node
            self.head = new_node
        self.count += 1


    def printList(self):
        temp = self.head
        for i in range(self.count):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    l = LinkedList()
    l.appendAtEnd(1)
    l.appendAtEnd(2)
    l.appendAtEnd(3)
    l.appendAtStart('s')
    l.appendAtStart('a')
    l.appendAtEnd(4)
    l.printList()