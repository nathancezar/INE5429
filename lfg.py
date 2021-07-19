"""
    Implementação do algoritmo LFG retirado da Wikipedia.
        Sn = S[n-j] * S[n-k] mod M
    Nesse caso, o novo termo é alguma combinação de quaisquer dois termos anteriores
    'm' geralmente é uma potência de 2 (m = 2M), frequentemente 2^32 ou 2^64.
    O operador Estrela (*) denota uma operação binária geral. Isso pode ser
adição, subtração, multiplicação ou o operador ou-exclusivo bit a bit (XOR).
Fonte: https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator
"""
import time, random

class LaggedFibonacciGenerator:
    def __init__(self, number_lenght, j=21, k=34) -> None:
        self.S = []
        self.j = min(j, k)
        self.k = max(j, k)
        self.m = pow(2, 32)
        self.number_lenght = number_lenght

    def run(self):
        """
        Roda o algoritmo de LaggedFibonacciGenerator
        Sn = S[n-j] * S[n-k] (mod m)
        usando a operação XOR
        """
        return (self.S[self.j - 1] ^ self.S[self.k - 1]) % self.m

    def getBinaryRandomNum(self):
        """
        Gera um número binário aleatório usando LFG

        Usa a lista de valores aleatórios (S)
        Realiza um XOR entre valores de index j e k escolhidos
        Deleta o primeiro valor da lista
        adiciona o número aleatório (Sn) no fim da lista
        obtem um valor binário a partir do valor de (Sn)
        Força o ultimo bit em 1.

        :lenght: tamanho do número a ser gerado.
        """
        result = "1"
        for _ in range(self.number_lenght-2):
            Sn = self.run()
            del self.S[0]
            self.S.append(Sn)
            b = Sn % 2
            result += str(b)
        result += "1"
        return result

    def generateS(self):
        """
        Gera um array de numeros aleatórios
        Pra facilitar a implementação, o tamanho dos números no array é o mesmo do
        número aleatório.
        """
        lower = 10**(self.number_lenght-1)
        upper = 10**self.number_lenght - 1
        return [random.randint(lower, upper,) for _ in range(self.k)]

if __name__ == '__main__':
    """
    Função Main para testar o Lagged Fibonacci Generator para um número de 40 bits
    """

    number_lenght = 40

    print("Rodando LaggedFibonacciGenerator.")
    print(f"Procurando número aleatório de {number_lenght} digitos.")
    lfg = LaggedFibonacciGenerator(number_lenght)
    lfg.S = lfg.generateS()
    print("====================")
    print("\t Array S")
    print(f"{lfg.S}")
    print("====================")

    start = time.process_time()
    random_binary_number = lfg.getBinaryRandomNum()
    exec_time = (time.process_time() - start)

    print(f"Valor aleatório encontrado: {random_binary_number}")
    print(f"Tempo de execução: {exec_time:.20f} segundos")