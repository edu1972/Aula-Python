

num = int(input("Digite um numero inteiro: "))
lista = []

while num != 0:
    
    dec = num * 10  # variavel para transformar em inteiro com zero final
    
    lista.append(dec)

    num = int(input("Digite um numero inteiro: "))

    numero = lista

       
print("Sequência inversa: ", end=" ") # imprime na ordem inversa
for numero in reversed(numero):
    print(numero, end=" ")
   #print()


def my_list(*lista):
    print("Mostra os numeros: ",lista)
    my_list(lista)    
