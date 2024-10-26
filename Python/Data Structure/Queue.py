
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None

    def print(self):
        for i in self.queue:
            print(i, end=" ")
        print()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()
    queue.dequeue()
    queue.print()
    print(queue.peek())
    queue.print()
    print("Size of Queue is: ", queue.size())
    print("Is the Queue Empty: ", queue.isEmpty())

if __name__ == "__main__":
    main()