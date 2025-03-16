from queue import Queue
childs=['A','B','C','D','E','F']
queue=Queue()

for kid in childs:
    queue.put(kid)
while queue.qsize() >1:
    for i in range(6):
        kid=queue.get()
        queue.put(kid)
    queue.get(kid)
print(queue.get())








