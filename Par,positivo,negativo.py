def linha():
  print("                                  ")
linha()

vezes = int(input("Quantas vezes você quer que repita o codigo? "))
vezes=vezes+1

linha()

for i in range(1,vezes):
  
  n = float(input(f'Digite o {i}º valor: '))
  linha()
  teste1= n % 2 > 0
  testepositivo= n > 0

  if n !=0:
    if teste1 ==0 :
      print("o numero", n, "é par")
    else:
      print("o numero", n, "é impar")
  else:
    print("o numero", n, "é nulo")

  if testepositivo:
    print("e positivo")
  elif n < 0:
    print("e negativo")
  linha()
  
linha()

print("fim do programa")

print("obrigado a todos")

print("Feito por: BrunoHads")
