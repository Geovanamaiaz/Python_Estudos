# MÓDULO 4: ENTRADA DE DADOS E CONVERSÃO
# input() recebe o que a pessoa digita.
# Por padrão, input() retorna texto (str).
# int() converte para inteiro e float() converte para decimal.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

idade_futura = idade + 5

print("Olá,", nome)
print("Daqui a 5 anos você terá", idade_futura, "anos.")
