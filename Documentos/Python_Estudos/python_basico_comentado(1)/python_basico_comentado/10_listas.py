# MÓDULO 10: LISTAS
# Uma lista armazena vários valores em uma única variável.
# Os índices começam em 0: o primeiro elemento é notas[0].

notas = [8.0, 7.5, 9.0]

print("Primeira nota:", notas[0])
print("Todas as notas:", notas)

notas.append(10.0)  # append() adiciona um elemento ao final da lista.
print("Lista atualizada:", notas)

for nota in notas:
    print("Nota:", nota)  # Percorre cada elemento da lista.
