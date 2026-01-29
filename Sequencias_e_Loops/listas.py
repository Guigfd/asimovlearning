lista_misturada = [0, 1.1, "PYTHON",[1,2]]

print(lista_misturada[2]) # retorna o valor do indice

print(lista_misturada[-1]) #retonra o ULTIMO valor do ULTIMO indice
print(lista_misturada[-1][1]) #retonra o ULTIMO valor do ULTIMO indice e o valor do ultimo indice da da lista dentro da lista

# -------------- TUPLAS --------------------

alunos = ['Ana', 'Nurb', 'Carlos']

alunos[1] = 0.0
print(alunos) # isso modifica a lista!

del alunos[0] # isso deleta o valor no indice indicado!
print(alunos)

valores = (1,2,3) # isso é uma tupla! Ela não aceita as modificações como as da lista/array, é uma mais segura de listas


# --------------------- Sequencias

nome = "Juliano"
print(nome[1]) # strings são sequencias

name_list = list(nome)
print(name_list)
print(len(name_list))

if name_list: #verifica se a sequencia não está vazia
    print("Sequencia nao esta vazia")

# ------- slicing

pessoas = ['joao', 'paulo', 'clara']
print(pessoas[1:3])

print(pessoas[1:]) # vai ate o final da lista
print(pessoas[:3]) # vai do inicio ate o final da lista, essas operações funcionam em strings também

numeros = [1,2,3,4,5,6,7,8,9]
print(numeros[0::3]) # lista os números pulando 3 numeros
print(numeros[::-2]) # inverte a lista e pula de 2 em 2

# ------- função Range

print(list(range(50))) # gera uma lista com a quantidade de numeros exposta
print(list(range(1, 150))) #declarado valor inicial
print(list(range(1, 150, 2))) #declarado valor inicial, final e o "pulo"


