import time, random

class BlumBlumShub:
    def __init__(self, seed, number_lenght, m=None) -> None:
        """
        Implementação do Algoritmo BlumBlumShub: x(n+1) = x(n)² mod M

        """
        self.number_lenght = number_lenght
        self.num = seed
        self.m = m

    def run(self) -> None:
        """
        Roda o algoritmo do BlumBlumShub
        x(n+1) = x(n)² mod M
        Onde 'm' é o produto de dois grandes números primos p e q
        """
        self.num = pow(self.num, 2, self.m) # (num^2) mod m


    def getBinaryRandomNum(self):
        result = "1"
        for _ in range(self.number_lenght - 2):
            self.run()
            b = self.num % 2
            result += str(b)
        result += "1" # Força o ultimo bit em 1
        self.num = int(result, 2)
        return result

"""
    Funções Auxiliares para encontrar numeros (p = 3 mod 4)
"""

def getPrimeNumber(number_lenght) -> int:
    """
    Gerar um numero "p" aleatório onde (p = 3 mod 4)

    :number_lenght: tamanho do numero desejado
    """
    lower = 10**(number_lenght-1)
    upper = 10**number_lenght - 1
    while True :
        p = random.randint(lower, upper)
        if (p % 4 == 3) : break
    return p

def generateM(number_lenght) -> int:
    """
    Gera 2 numeros aleatórios e retorna o produto deles
    """
    p = getPrimeNumber(number_lenght)
    q = getPrimeNumber(number_lenght)

    # Pra garantir que p != q
    while (p == q) :
        q = getPrimeNumber(number_lenght)
    print(f"Numeros primos Gerados: p: {p} | q: {q}")
    return p*q


if __name__ == '__main__':
    """
    Função Main para testar o BlumBlumShub para um número de 40 bits
    """

    seed = int(time.time())
    number_lenght = 40

    print("Rodando BlumBlumShub.")
    print(f"Procurando número aleatório de {number_lenght} digitos.")
    m = generateM(2)
    print(f"Valor de M utilizado: {m}")

    bbs = BlumBlumShub(seed, number_lenght, m)
    start = time.process_time()
    random_binary_number = bbs.getBinaryRandomNum()
    exec_time = (time.process_time() - start)

    print(f"Valor aleatório encontrado: {random_binary_number}")
    print(f"Tempo de execução: {exec_time:.20f} segundos")
