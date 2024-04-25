#função de adição

def add(x, y): 
  
 return x + y 

#função de subitração

def sub(x, y):

  return x - y 

#função de multiplicação

def mult(x, y):

  return x * y 

#função de divisão

def div(x, y):

  return x / y

#Calculadora

print("selecione uma operação.")
print("1. adição")
print("2. subtração")
print("3. multplicação")
print("4. divisão")

while True:
  escolha = input("Escolha um número (1/2/3/4): ")
  if escolha in ('1', '2', '3', '4'):
    
    num1 = float (input("Digite um  número: "))
    num2 = float (input("Digite outro número"))

  if escolha == '1': 
    print(num1, "+", num2, "=", add(num1, num2))
  elif escolha == '2':    
     print(num1, "-", num2, "=", add(num1, num2))
  elif escolha == '3':
    print(num1, "*", num2, "=", add(num1, num2))

  else: 
    print("Deixa de ser cabaço e escolhe a opção certa D:<")