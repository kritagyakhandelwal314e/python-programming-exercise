from Dequeue import Dequeue
class Queue():
  def __init__(self, queue: list = [], capacity: int = 100, is_limit: bool = True):
    self.is_limit = is_limit
    self.all_int = True
    self._queue = []
    self.size = 0
    self._min_deque = Dequeue()
    self.capacity = capacity
    for item in queue:
      self.enqueue(item)
    self.size = len(self._queue)

  # dequeue operations functions
  def handle_enqueue(self, value):
    if (not self._min_deque.is_empty()) and value < self._min_deque.back():
      self._min_deque.pop_back()
      self.handle_enqueue(value)
    else:
      self._min_deque.push_back(value)

  def handle_dequeue(self, value):
    if self._min_deque.front() == value:
      self._min_deque.pop_front()

  # queue operations functions
  def dequeue(self):
    if self.size > 0:
      popped = self._queue.pop(0)
      if self.all_int:
        self.handle_dequeue(popped)
      self.size -= 1
      return popped
    else:
      return None

  def enqueue(self, value):
    if type(value) != type(1):
      self.all_int = False
    if (not self.is_limit) or (self.is_limit and len(self._queue) != self.capacity):
      self._queue.append(value)
      self.size += 1
      if self.all_int:
        self.handle_enqueue(value)
    else:
      popped = self.dequeue()
      self.enqueue(value)

  def reverse(self):
    if self.size == 0:
      return
    popped = self.dequeue()
    self.reverse()
    self.enqueue(popped)

  # getter functions
  def echo(self):
    print(self._queue)

  def minimum(self):
    if self.all_int:
      return self._min_deque.front()
    return None

  def echo_deque(self):
    print(self._min_deque.get())

  def is_empty(self):
    return self.size == 0

  def __len__(self):
    return self.size

  def __str__(self):
    return str(self._queue)

  def __list__(self):
    return self._queue.copy()