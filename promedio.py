def average(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum / len(numbers)

print(average([1, 2, 3]))