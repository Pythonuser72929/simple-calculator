def calculadora() :
   x = int(input(">>>  "))
   if type(x) is str:
      print("inserte solo numeros")
      calculadora()
   elif type(x) is not str:
      signo = (input("+-×÷:"))
      y = int(input(">>>  "))
      if type(y) is str:
        print("inserte solo numeros")
        calculadora()
      elif type(y) is not str:
        if signo == "+" or signo == "sumar" or signo == "mas":
          resultado = x + y
          print("=" , resultado)
          nuevo()
        elif signo == "-" or signo == "restar" or signo == "menos":
          resultado = x - y
          print("=" , resultado)
          nuevo()
        elif signo == "÷" or signo == "dividido" or signo == "dividir":
          resultado = x / y
          print("=" , resultado)
          nuevo()
        elif signo == "×" or signo == "por" or signo == "multiplicar":
          resultado = x * y
          print("=" , resultado)
          nuevo()
        else:
          print("comando invalido, inserte simbolo de       operador intentelo de nuevo")
          calculadora()
def nuevo(): 
   nuevo = input("desea realizar otra operacion? y/n: ").lower()
   if nuevo == "y" or nuevo == "yes":
      calculadora()
   elif nuevo == "n" or nuevo == "no":
      print("hasta luego")
   else:
      print("comando invalido solo se acepta y/n yes/no")
      nuevo()
calculadora()
    