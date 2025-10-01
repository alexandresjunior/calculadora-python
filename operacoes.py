def adicionar(a, b):
    """Soma dois números."""
    return a + b

def subtrair(a, b):
    """Subtrai dois números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números."""
    return a * b

def dividir(a, b):
    """Divide dois números, com tratamento para divisão por zero."""
    if b == 0:
        return "Erro: Divisão por 0"
    return a / b