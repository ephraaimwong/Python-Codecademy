def is_prime(x):
  #numbers below 2 is not prime
  if x < 2:
    return False
  else:
      for n in range(2, x - 1):
          #if x is fully divisible by another number, it is not a prime number
        if x % n == 0:
          return False 
      return True
print(is_prime(5))