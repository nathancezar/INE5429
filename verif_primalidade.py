from random import randrange


_RODADAS = 40

class MillerRabin():
    def __init__(self, rodadas=_RODADAS) -> None:
        self.rodadas = rodadas

    def run(self, num):
        """
        Algoritmo de Miller Rabin para verificar primalidade
        write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
        WitnessLoop: repeat k times:
            pick a random integer a in the range [2, n − 2]
            x ← ad mod n
            if x = 1 or x = n − 1 then
                continue WitnessLoop
            repeat r − 1 times:
                x ← x2 mod n
                if x = n − 1 then
                    continue WitnessLoop
            return “composite”
        return “probably prime”

        Fonte: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test
        """
        if num <= 3: # verifica se é 1, 2 ou 3
            return True

        if num % 2 == 0: # verifica se é par
            return False

        s = 0
        d = num-1

        while d % 2 == 0:
            d //= 2
            s += 1

        if not (pow(2,s) * d == num-1):
            print(f"Erro: Não é possivel fatorar {num}.")
            return False

        for _ in range(self.rodadas):
            a = randrange(2, num - 2 )
            x = pow(a, d, num) # x recebe a^d mod n

            if x == 1 or x == num - 1: continue

            for _ in range(s - 1):
                x = pow(x, 2, num) # x recebe x^2 mod n

            if x == num-1:
                break
        else:
            return False

        return True

class Fermat():
    def __init__(self, rodadas=_RODADAS) -> None:
        self.rodadas = rodadas

    def run(self, num):
        """
        Algoritmo de Fermat para verificação de primalidade
        Repeat k times:
            Pick a randomly in the range [2, n − 2]
            If a n − 1 ≢ 1 ( mod n ), then return composite
        If composite is never returned: return probably prime

        Fonte: https://en.wikipedia.org/wiki/Fermat_primality_test#Algorithm
        """
        if num <= 3: # verifica se é 1, 2 ou 3
            return True

        if num % 2 == 0: # verifica se é par
            return False

        for _ in range(0, self.rodadas):
            a = randrange(2, num-2 + 1)
            x = pow(a,num-1, num)

            if x != 1:
                return False

        return True
