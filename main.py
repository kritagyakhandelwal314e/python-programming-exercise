import Queue as Q
import random

q = Q.Queue([], capacity=9, is_limit=True)

q.echo()
q.echo_deque()
print('minimum: ', q.minimum())
q.dequeue()
q.echo()
q.echo_deque()
print('minimum: ', q.minimum())
for i in range(101):
  if i % 10 == 0:
    q.reverse()
  value = random.randint(1, 101)
  q.enqueue(value)
  q.echo()
  q.echo_deque()
  print('minimum: ', q.minimum())


# dq = Q.Dequeue()
# print(dq.get())
# dq.push_back(10)
# print(dq.size)
# print(dq.get())