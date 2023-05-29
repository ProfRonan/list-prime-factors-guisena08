"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    n = 0
    for i in range (1,number + 1):
        if number % i == 0:
            n += 1
    if n ==2:
        return True
    else:         
       
          return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    f = []
    d = 2
    
    while d <= number:
        if number % d ==0:
            f.append(d)
            number/= d
        else:
            d +=1    
        

    return f
