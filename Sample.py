from Queue import Queue

queueObject = Queue()
for i in range(6):
    print("Run Push :: ", str(i+1))
    queueObject.push(i+1)
    if i == 4:
        queueObject.print()
print("Run Pull :: " + str(queueObject.pull()))
print("Run Peek :: " + str(queueObject.peek()))
print("Run Pull :: " + str(queueObject.pull()))
queueObject.print()
