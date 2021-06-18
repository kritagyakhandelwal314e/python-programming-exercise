def sublist(li, S):
  l = 0
  sum = 0
  for r, item in enumerate(li):
    sum += item
    while sum > S:
      sum -= li[l]
      l += 1
    if sum == S:
      return li[l:r + 1]
  return []

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = 60
print(sublist(li, S))