 #Questão 1

 #Faça um programa que peça um valor via input de usuário e mostre na tela se o número é positivo ou negativo.

print("======================")
print("Welcome to the program!")
print("======================")
value = float(input("To start, enter a number: "))

if value > 0:
    print(f"The number {value} is positive.")
elif value == 0:
    print(f"Wow, the number is {value}. Try again.")
else:
    print(f"The number {value} is negative.")
