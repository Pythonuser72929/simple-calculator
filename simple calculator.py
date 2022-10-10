def calculator() :
   x = int(input(">>>  "))
   if type(x) is str:
      print("only numbers = ")
      calculator()
   elif type(x) is not str:
      operator = (input("+-(×÷/*%):"))
      y = int(input(">>>  "))
      if type(y) is str:
        print("only numbers = ")
        calculator()
      elif type(y) is not str:
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
    
