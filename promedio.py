def average(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum / len(numbers)

list = [1, 2, 3]
print(f"El promedio de {list} es: {average(list)}")
