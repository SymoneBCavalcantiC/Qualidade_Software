class Calculadora:
    def adicionar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def fatorial(n):
        if n < 0:
            raise ValueError("Fatorial de número negativo não é permitido")
        if n == 0:
            return 1
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

    def potencia(a, b):
        return a ** b
