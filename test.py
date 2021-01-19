
from queue import SimpleQueue


q = SimpleQueue()

q.put(10)
q.put('+')
q.put(20)

v = q.get()
print(v, q.qsize())
v = q.get()
print(v, q.qsize())
v = q.get()
print(v, q.qsize())
