class Queue:

    def __init__(self, size):
        self.queue = list()
        self.size = size

    def push(self, item):
        if len(self.queue) < self.size:
            self.queue.insert(0, item)
            return True
        else:
            return False

    def pull(self):
        if self.queue:
            return self.queue.pop()
        else:
            return False

    def isfullstatus(self):
        if len(self.queue) == self.size:
            return True
        else:
            return False

    def isemptystatus(self):
        if not self.queue:
            return True
        else:
            return False

    def print(self):
        print('->', ','.join(str(a) for a in self.queue), '->')
