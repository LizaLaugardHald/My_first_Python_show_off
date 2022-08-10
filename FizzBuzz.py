for x in range(100):
  if x % 3 == 0 and x % 5 == 0 and x != 0:
      print("FizzBuzz " , x)
  else: 
    if x % 3 == 0 and x != 0:
        print("Fizz " , x)
    if x % 5 == 0 and x != 0:
        print("Buzz " , x)
    
  
