def average(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum / len(numbers)

print(f"El promedio de [1, 2, 3] es: {average([1, 2, 3])}")
