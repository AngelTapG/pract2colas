class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f" Customer: {self.get_customer()}")
        print(f" Quantity: {self.get_qtty()}")
        print(" ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


from abc import ABC, abstractmethod

class QueueInterface(ABC):
    @abstractmethod
    def size(self): pass

    @abstractmethod
    def is_empty(self): pass

    @abstractmethod
    def front(self): pass

    @abstractmethod
    def enqueue(self, info): pass

    @abstractmethod
    def dequeue(self): pass

class Queue(QueueInterface):
    def __init__(self):
        self.front_node = None
        self.rear = None
        self.size_count = 0

    def size(self):
        return self.size_count

    def is_empty(self):
        return self.front_node is None

    def front(self):
        if self.is_empty():
            return None
        return self.front_node.get_data()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front_node = new_node
        else:
            self.rear.set_next(new_node)
        self.rear = new_node
        self.size_count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front_node.get_data()
        self.front_node = self.front_node.get_next()
        if self.front_node is None:
            self.rear = None
        self.size_count -= 1
        return data

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f" Size: {self.size_count}")
        node = self.front_node
        index = 1
        while node is not None:
            print(f" ** Element {index}")
            node.get_data().print()
            node = node.get_next()
            index += 1
        print("******************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size_count:
            return None
        node = self.front_node
        for i in range(1, pos):
            node = node.get_next()
        return node.get_data()

def test_queue():
    queue = Queue()

    
    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")

    
    print("Añadiendo pedido 1:")
    queue.enqueue(order1)
    queue.print_info()

    print("\nAñadiendo pedido 2:")
    queue.enqueue(order2)
    queue.print_info()

    print("\nAñadiendo pedido 3:")
    queue.enqueue(order3)
    queue.print_info()

    
    print("\nFront of queue:")
    front_order = queue.front()
    if front_order is not None:
        front_order.print()

    
    print("\nDequeue:")
    dequeued_order = queue.dequeue()
    if dequeued_order is not None:
        dequeued_order.print()

   
    print("\nCola después del dequeue:")
    queue.print_info()

    
    order4 = Order(50, "cust4")
    print("\nAñadiendo pedido 4:")
    queue.enqueue(order4)
    queue.print_info()

    
    print("\nObteniendo el tercer elemento:")
    third_order = queue.get_nth(3)
    if third_order is not None:
        third_order.print()

if __name__ == "__main__":
    test_queue()