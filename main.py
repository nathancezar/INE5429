import time, csv
import arguments

from bbs import BlumBlumShub
from lfg import LaggedFibonacciGenerator
from verif_primalidade import MillerRabin, Fermat


_NUMBERS_LENGHT = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
_SEED = int(time.time())

class Main:
    def __init__(self, args):
        self._args = args
        self.bbs_results = []
        self.lfg_results = []
        self.mr = MillerRabin()

    def run(self):
        if self._args['auto']:
            print("Execução Automática: Procurando Primos de todos os Tamanhos!")

            m = self._args['valor_p'] * self._args['valor_q']
            j = self._args['valor_j']
            k = self._args['valor_k']

            for lenght in _NUMBERS_LENGHT:

                """ Executa automaticamente o algoritmo BBS e verifica a
                primalidade usando Miller Rabin.
                """
                is_prime = False
                bbs = BlumBlumShub(_SEED, lenght, m)
                start = time.process_time()
                while( not is_prime):
                    prn_bbs = bbs.getBinaryRandomNum()
                    is_prime = self.mr.run(int(prn_bbs, 2))
                    exec_time = (time.process_time() - start)
                    if is_prime:
                        self.bbs_results.append({'Tempo': f"{exec_time:.20f}",
                                                'Numero': int(prn_bbs, 2),
                                                'Binario': prn_bbs})

                print(f'Numero de tamanho {lenght} encontrado pelo BlumBlumShub:')
                print(f'{prn_bbs}')
                print(f'Tempo de busca: {exec_time:.20f}')

            with open('BBS_Result.csv', 'a+', newline='') as csv_file:
                w = csv.DictWriter(csv_file, self.bbs_results[0].keys())
                w.writeheader()
                w.writerows(self.bbs_results)
            csv_file.close()

            for lenght in _NUMBERS_LENGHT:

                """ Executa automaticamente o algoritmo LFG e verifica a
                primalidade usando Miller Rabin.
                """
                is_prime = False
                lfg = LaggedFibonacciGenerator(lenght, j, k)
                while( not is_prime):
                    lfg.S = lfg.generateS()
                    start = time.process_time()
                    prn_lfg = lfg.getBinaryRandomNum()
                    is_prime = self.mr.run(int(prn_lfg))
                    exec_time = (time.process_time() - start)
                    if is_prime:
                        self.lfg_results.append({'Tempo': f"{exec_time:.20f}",
                                                'Numero': int(prn_lfg, 2),
                                                'Binario': prn_lfg})

                print(f'Numero de tamanho {lenght} encontrado pelo LaggedFibonacciGenerator:')
                print(f'{prn_lfg}')
                print(f'Tempo de busca: {exec_time:.20f}')

            with open('LFG_Result.csv', 'a+', newline='') as csv_file:
                w = csv.DictWriter(csv_file, self.lfg_results[0].keys())
                w.writeheader()
                w.writerows(self.lfg_results)
            csv_file.close()

        else:

            print("Executando algoritmo BlumBlumShub")
            print(f'Procurando Primo de tamanho: {self._args["tamanho"]}')
            m = self._args['valor_p'] * self._args['valor_q']

            for lenght in self._args['tamanho']:
                is_prime = False
                bbs = BlumBlumShub(_SEED, lenght, m)
                start = time.process_time()
                while(not is_prime):
                    prn_bbs = bbs.getBinaryRandomNum()
                    is_prime = self.mr.run(int(prn_bbs, 2))
                    exec_time = (time.process_time() - start)
                    if is_prime:
                        self.bbs_results.append({'Tamanho': lenght,
                                            'Tempo': f"{exec_time:.20f}",
                                            'Numero': int(prn_bbs, 2),
                                            'Binario': prn_bbs})

            print(f'Numero de tamanho {lenght} encontrado pelo BlumBlumShub:')
            print(f'{int(prn_bbs, 2)}')
            print(f'Tempo de busca: {exec_time:.20f}')

            print("Executando algoritmo LaggedFibonacciGenerator")
            print(f'Procurando Primo de tamanho: {self._args["tamanho"]}')

            for lenght in self._args['tamanho']:
                is_prime = False
                lfg = LaggedFibonacciGenerator(lenght,
                                            self._args['valor_j'],
                                            self._args['valor_k'])
                while( not is_prime):
                    lfg.S = lfg.generateS()
                    start = time.process_time()
                    prn_lfg = lfg.getBinaryRandomNum()
                    is_prime = self.mr.run(int(prn_lfg, 2))
                    exec_time = (time.process_time() - start)
                    if is_prime:
                        self.lfg_results.append({'Tamanho': lenght,
                                            'Tempo': f"{exec_time:.20f}",
                                            'Numero': int(prn_lfg, 2),
                                            'Binario': prn_lfg})

                print(f'Numero de tamanho {lenght} encontrado pelo LaggedFibonacciGenerator:')
                print(f'{int(prn_lfg, 2)}')
                print(f'Tempo de busca: {exec_time:.20f}')

            if not self._args['csv']:
                if self.lfg_results:
                    with open('LFG_Result2.csv', 'a+', newline='') as csv_file:
                        w = csv.DictWriter(csv_file, self.lfg_results[0].keys())
                        w.writeheader()
                        w.writerows(self.lfg_results)
                    csv_file.close()

                if self.bbs_results:
                    with open('BBS_Result2.csv', 'a+', newline='') as csv_file:
                        w = csv.DictWriter(csv_file, self.bbs_results[0].keys())
                        w.writeheader()
                        w.writerows(self.bbs_results)
                    csv_file.close()


if __name__ == '__main__':
    args = arguments.parseArguments()

    main = Main(args)
    main.run()