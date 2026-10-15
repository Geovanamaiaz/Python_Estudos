# MÓDULO 12: MINI PROJETO - MÉDIA DO ESTUDANTE
# Este programa recebe duas notas, calcula a média e mostra o resultado.

nome = input("Nome do estudante: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print("\nEstudante:", nome)
print("Média:", media)

if media >= 6:
    print("Situação: aprovado")
else:
    print("Situação: reprovado")
