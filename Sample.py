from Queue import Queue

queueObject = Queue(5)
queueObject.push(1)
queueObject.push(2)
queueObject.push(3)
queueObject.push(4)
queueObject.push(5)
queueObject.push(6)
queueObject.print()
print("Run pull :: " + str(queueObject.pull()))
queueObject.print()
