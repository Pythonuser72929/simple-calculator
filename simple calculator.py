def calculator() :
      x = int(input(">>>  "))
      operator = (input("+-(×÷/*%):"))
      y = int(input(">>>  "))
      if operator == "+":
          result = x + y
          print("=" , result)
          new()
      elif operator == "-":
          result = x - y
          print("=" , result)
          new()
      elif operator == "÷" or operator == "%":
          result = x / y
          print("=" , result)
          new()
      elif operator == "×" or operator == "*":
          result = x * y
          print("=" , result)
          new()
      else:
          print("invalid operator only: +-(×÷/*%)")
          calculator()
def new(): 
   new = input("make another one y/n: ").lower()
   if new == "y" or new == "yes":
      calculator()
   elif new == "n" or new == "no":
      print("see you later")
   else:
      print("invalid command only: y/n yes/no")
      new()
calculator()
    
