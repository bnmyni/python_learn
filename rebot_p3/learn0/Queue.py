from multiprocessing import Queue

q = Queue(3)
q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

try:
    q.put("消息4", True, 2)
except:
    print("队列已经满了")

try:
    q.put_nowait("消息5")
except:
    print("队列已经满了2")

if not q.full():
    q.put_nowait("消息6")

if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())