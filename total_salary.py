def total_salary(path):
  sum = 0
  with open(path) as file:
    for line in file:
      sum += float(line)
  return sum