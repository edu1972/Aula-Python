
lista = []

def n_primos(n):
    """
    Retorna a quantidade de números primos entre 2 e n (incluindo 2 e n, se forem primos)
    """
    count = 0
    for num in range(2, n+1):
        if eh_primo(num):
            count += 1
            print(num,end=" ")
        lista = num
    return count

def eh_primo(num):
    """
    Retorna True se o número for primo e False caso contrário
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
