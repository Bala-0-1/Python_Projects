def is_prime(n):
  if n<0:
    return "Negative primes does not exist"
  if n<2>=0:
     return "Try higher value"
  primes=[2]
  for i in range(3,n,2):
    j=2
    f=0
    while j<=round(i**0.5):
      if i%j==0:
        f=1
      j+=1
    if f==0:
      primes.append(i)
  return primes
try:
    n = int(input("Enter a number : "))
    if isinstance(is_prime(n),str):
        print(is_prime(n))
    else:
       print("The number of primes between 1 and {} is {}".format(n,len(is_prime(n))))
except ValueError:
    print("Wrong data type!")