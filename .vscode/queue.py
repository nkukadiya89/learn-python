#Queue in python

from collections import deque

queue = deque([])
#add item in queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#remove item from queue
queue.popleft()
print(queue)
