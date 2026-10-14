
# ==========================================
# AULA 4 - OPERADORES LÓGICOS EM PYTHON
# ==========================================

# 1. VARIÁVEIS
# Guardamos dois valores para testar as condições.

idade = 20
nota = 8

# 2. OPERADOR AND (E)
# As DUAS condições precisam ser verdadeiras.

print("\n--- OPERADOR AND ---")

print(idade >= 18 and nota >= 6)

# idade >= 18  -> True
# nota >= 6    -> True
# True and True -> True


# 3. OPERADOR OR (OU)
# Pelo menos UMA condição precisa ser verdadeira.

print("\n--- OPERADOR OR ---")

print(idade >= 18 or nota < 6)

# idade >= 18 -> True
# nota < 6    -> False
# True or False -> True


# 4. OPERADOR NOT (NAO)
# Inverte o valor lógico:
# True vira False e False vira True.

print("\n--- OPERADOR NOT ---")

print(not (idade >= 18))

# idade >= 18 -> True
# not True    -> False


# 5. USANDO OPERADORES COM IF E ELSE
# Podemos tomar decisões combinando condições.

print("\n--- VERIFICACAO DE APROVACAO ---")

if idade >= 18 and nota >= 6:
    print("Aprovado e maior de idade")
else:
    print("Nao atende as duas condicoes")


# 6. VERIFICANDO COM NOT
# Se a nota NAO for maior ou igual a 6,
# a condicao abaixo sera verdadeira.

print("\n--- VERIFICACAO DA NOTA ---")

if not (nota >= 6):
    print("Nota insuficiente")
else:
    print("Nota suficiente")
