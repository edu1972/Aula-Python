
def é_hipotenusa(n):
    """
    Verifica se um número n é hipotenusa de algum triângulo retângulo com catetos inteiros.
    """
    for i in range(1, n):
        for j in range(i, n):
            if i**2 + j**2 == n**2:
                return True
    return False

def soma_hipotenusas(n):
    """
    Retorna a soma de todas as hipotenusas de triângulos retângulos com catetos inteiros entre 1 e n.
    """
    soma = 0
    for i in range(1, n+1):
        if é_hipotenusa(i):
            soma += i
    return soma






