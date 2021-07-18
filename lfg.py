"""
    Implementação do algoritmo LFG retirado da Wikipedia.
        Sn = S[n-j] * S[n-k] (mod m)
    'm' geralmente é uma potência de 2 (m = 2M), frequentemente 232 ou 264.
    O operador Estrela (*) denota uma operação binária geral.
    Isso pode ser adição, subtração, multiplicação ou o operador ou exclusivo
bit a bit (XOR).
"""
import time, random

class LaggedFibonacciGenerator:
    def __init__(self, s, number_lenght, j=21, k=34) -> None:
        self.S = s
        self.j = j
        self.k = k
        self.m = pow(2, 32)

    def getBinaryRandomNum(self, lenght=40):
        result = "1"
        for _ in range(lenght-1):
            Sn = (self.S[self.j - 1] + self.S[self.k - 1]) % self.m
            self.S = self.S[1:]
            self.S.append(Sn)
            b = Sn % 2
            result += str(b)
        return result

def generateS(numbers_lenght: int, array_lenght: int) -> int:
    """
    Gera um array de numeros aleatórios

    :numbers_lenght: tamanho dos numeros aleatorios
    :array_lenght: tamanho do array
    """
    lower = 10**(numbers_lenght-1)
    upper = 10**numbers_lenght - 1
    return [random.randint(lower, upper) for _ in range(array_lenght)]

if __name__ == '__main__':
    """
    Função Main para testar o Lagged Fibonacci Generator para um número de 40 bits
    """

    number_lenght = 40

    print("Rodando LaggedFibonacciGenerator.")
    print(f"Procurando número aleatório de {number_lenght} digitos.")
    s = generateS(40, 34)
    print("====================")
    print("\t Array S")
    print(f"{s}")
    print("====================")

    lfg = LaggedFibonacciGenerator(s, number_lenght)
    start = time.process_time()
    random_binary_number = lfg.getBinaryRandomNum()
    exec_time = (time.process_time() - start)

    print(f"Valor aleatório encontrado: {random_binary_number}")
    print(f"Tempo de execução: {exec_time:.20f} segundos")