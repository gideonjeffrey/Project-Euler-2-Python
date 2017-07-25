# Project-Euler-2-Python
# Sum even Fibonacci numbers through 4,000,000
def sum_even_fibonacci_through(number):
  if number < 2:
    return 0
  if number == 2:
    return 2
  start = 1
  step = 2
  even_terms = [2]
  new_num = start + step
  while new_num < number:
    if new_num % 2 == 0:
      even_terms.append(new_num)
    start = step
    step = new_num
    new_num = start + step
  return sum(even_terms)

print(sum_even_fibonacci_through(4000000))
