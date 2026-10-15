# MÓDULO 7: IF, ELIF E ELSE
# elif significa "senão, se" e permite verificar outra condição.

nota = float(input("Digite sua nota (0 a 10): "))

if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprovado!")
else:
    print("Precisa estudar mais.")

# As condições são verificadas de cima para baixo.
