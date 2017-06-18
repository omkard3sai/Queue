from Node import Node


class Queue:

    def __init__(self):
        self.head = None

    def push(self, item):
        insert = Node(item)
        if self.empty_status():
            insert.previous = None
            self.head = insert
        else:
            insert.previous = self.head
            self.head = insert

    def pull(self):
        if not self.empty_status():
            pull_data = self.head.data
            self.head = self.head.previous
            return pull_data
        else:
            return False

    def peek(self):
        if not self.empty_status():
            return self.head.data
        else:
            return False

    def empty_status(self):
        if self.head is None:
            return True
        else:
            return False

    def print(self):
        queue = self.head
        print("Rear/Push", end=" -> ")
        while queue:
            print(queue.data, end=" -> ")
            queue = queue.previous
        print("Front/Pull")
