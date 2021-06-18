def pretty_square(n):
  for i in range(1, 2*n):
    for j in range(1, 2*n):
      value = max(abs(n - i), abs(n - j)) + 1
      print(value, end=" ")
    print()

pretty_square(3)