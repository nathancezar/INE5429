import time, csv

from bbs import BlumBlumShub
from lfg import LaggedFibonacciGenerator


numbers_lenght = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
seed = int(time.time())

def main():

    bbs_results = []
    p = 100000000063
    q = 100000002499
    m = p * q

    # lfg_results = []

    for lenght in numbers_lenght:
        bbs = BlumBlumShub(seed, lenght, m)
        start = time.process_time()
        prn = bbs.getBinaryRandomNum()
        exec_time = (time.process_time() - start)
        bbs_results.append({'Tempo': f"{exec_time:.20f}", 'Numero': prn })

        # lfg = LaggedFibonacciGenerator()

    print(bbs_results)

    with open('BBS_Result.csv', 'w', newline='') as csv_file:
        w = csv.DictWriter(csv_file, bbs_results[0].keys())
        w.writeheader()
        w.writerows(bbs_results)
    csv_file.close()


if __name__ == '__main__':
    main()