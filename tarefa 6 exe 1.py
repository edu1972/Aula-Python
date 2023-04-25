
lista = []
def remove_repetidos(lista):
    lista_sem_repeticao = list(set(lista))
    lista_sem_repeticao.sort()
    return lista_sem_repeticao

def soma_elementos(lista):
    lista_soma = sum(lista)
    print(lista_soma)

def maior_elemento(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

lista = []
while True:
    valor = int(input("Digite um número inteiro (0 para sair): "))
    if valor == 0:
        break
    lista.append(valor)

for i in range(len(lista) - 1, -1, -1):
    print(lista[i])
