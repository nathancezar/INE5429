# Trabalho 2 - Numeros Primos

    Implementados 2 algoritmos de geração de números pseudo aleatórios:
        -BlumBlumShub
        -LaggedFibonacciGenerator

    Implementados 2 métodos de verificação de números primos:
        -MillerRabin
        -Fermat

    Linguagem utilizada:
        - Python 3.6.9


###Para usar os scripts:

## main.py
Rodar os scripts 1 vez em para buscar 1 numero primo de 40 bits em cada
algoritmo de geração de número aleatório:

```sh
$ python main.py
```

Rodar os scripts pra todos os tamanhos de números pedidos :
[40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

```sh
$ python main.py -a
```

Os valores padrão dos algoritmos podem ser alterado com os seguintes argumentos:

    -t = tamnho do número em bits;
    -p e -q = valores que serão multiplicados para obter 'm' no algotirmo BlumBlumShub;
    -j e -k = valores usados como índice no algoritmo de LaggedFibonacciGenerator;
    -r = quantidade de rodadas nos algoritmos de teste de primalidade;
    -csv = cancela a criação de arquivos .csv com os resultados.

Exemplo:

```sh
$ python main.py -p 100000000063 -q 100000002499 -j 21 -k 34 -r 40 -csv
# k sempre recebe o maior valor entre j e k. -> max(j, k)
```

## bbs.py
Usado para testar o algoritomo BlumBlumShub.
Tamanho padrão do número gerado: 40 Este valor pode ser alterado mudando o valor de
"number_lenght" na linha 69 do script.

```sh
$ python bbs.py
```

## lfg.py
Usado para testar o algoritomo LaggedFibonacciGenerator.
Tamanho padrão do número gerado: 40 Este valor pode ser alterado mudando o valor de
"number_lenght" na linha 66 do script.

```sh
$ python lfg.py
```

## verif_primalidade.py
Usado para testar os algoritmos de teste de primalidade.
É usado um conjunto fixo de numeros primos e não primos de até 1024 bits.
Estes números podem ser alterados no script.
Ao final os resultados são salvos em 2 arquivos csv com o nome dos algoritmos.

```sh
$ python verif_primalidade.py
```