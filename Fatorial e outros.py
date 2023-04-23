# Fatorial

print("Fatorial")
n = int(input("Digite um numero inteiro: "))
while n > 0:
    fatorial = 1
    while n> 1:
        fatorial = fatorial * n
        n = n -1
    print (fatorial)
    n = int(input("Digite um numero inteiro: "))

#=====================================================#
# Decomposição de fatores primos e mutiplicidades de cada fator

print("Decomposição de fatores")
n = int(input("Dighite um numero inteiro > 1:  "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("fator ", fator, "multiplicidade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0

#======================================================#
# Informar se o numero é primo

print("Verificar se é primo")
def ehPrimo (x):
    fator = 2
    
    if x == 2:
        return True
    
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input("Digite um numero inteiro: "))
while n > 0:
    if ehPrimo(n):
        print (n, " é Primo!")
    else:
        print (n, "não é Primo!")
    n = int(input("Digite um numero inteiro: "))





    




    
