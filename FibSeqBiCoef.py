from math import factorial
print "This program calculates the Fibonacci Sequence or Binomial Expansion Coefficient"
print 
def calcFib(n):
  number = 0
  
  list = [1, 1]
  
  if n == 0 or n == 1:
    number = 0
  else:
    for x in range(2,n):
      
      list.append(list[x - 1] + list[x - 2])
      
  print list
      

def biEx(size):
  x = int(size)
  list = []
  if size != 0:
    for x in range(0, size):
      list.append(int((factorial(size - 1)) / (factorial(x) * factorial(size - 1 - x))))
  print list
  
  
choice = input("Do you want to calculate the Fibonacci Sequence or the Binomial Expansion Coefficient?:")

if choice.lower() == "fibonacci sequence" or choice == "1":
  index = input("What index of the Fibonacci Squence do you want?:")
  calcFib(int(index))
elif choice.lower() == "binomial expansion coefficient" or choice == "2":
  rows = input("What index of the binomial expansion coefficient?: ")
  biEx(int(rows))
  

