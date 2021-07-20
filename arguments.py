import sys
import argparse

def getArguments():
    """
        Return argparse arguments

        Parse arguments
    """

    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tamanho", default=40,
                    help="tamanho em bits do número aleatório desejado")
    ap.add_argument("-a", "--auto", action="store_true", default=False)

    ap.add_argument("-p", "--valor_p", default=100000000063,
                    help="Numero primo usado no algoritimo BBS")
    ap.add_argument("-q", "--valor_q", default=100000002499,
                    help="Numero primo usado no algoritimo BBS")

    ap.add_argument("-j", "--valor_j", default=21,
                    help="Numero  usado no algoritmo LFG")
    ap.add_argument("-k", "--valor_k", default=34,
                    help="Numero usado no algoritimo LFG")

    ap.add_argument('-r', '--rodadas', default=40,
                    help="Quantidade de rodadas da verificação de primalidade")

    ap.add_argument('-csv', '--csv', action="store_true",
                    help="ativa opção de gerar arquivo csv com os resultados")
    return vars(ap.parse_args())

def parseArguments():
    arguments = getArguments()

    arguments['valor_p'] = int(arguments['valor_p'])
    arguments['valor_q'] = int(arguments['valor_q'])
    arguments['valor_j'] = int(arguments['valor_j'])
    arguments['valor_k'] = int(arguments['valor_k'])
    arguments['rodadas'] = int(arguments['rodadas'])
    arguments['tamanho'] = [int(arguments['tamanho'])]

    return arguments