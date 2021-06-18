class Dequeue():
  def __init__(self):
    self.dequeue = []
    self.size = 0

  # dequeue operations
  def push_back(self, value: int):
    self.size += 1
    self.dequeue.append(value)

  def pop_front(self):
    if self.size != 0:
      popped = self.dequeue.pop(0)
      self.size -= 1
      return popped
    return None

  def pop_back(self):
    if self.size != 0:
      popped = self.dequeue.pop(-1)
      self.size -= 1
      return popped
    return None

  # getters
  def is_empty(self):
    return self.size == 0

  def front(self):
    if self.is_empty():
      return None
    return self.dequeue[0]

  def back(self):
    if self.is_empty():
      return None
    return self.dequeue[-1]

  def get(self):
    return self.dequeue
