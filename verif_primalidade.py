from random import randrange
import time, csv


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
        continue_outer_loop = False
        if num <= 3: # verifica se é 1, 2 ou 3
            return True

        if num % 2 == 0: # verifica se é par
            return False

        s = 0
        d = num-1

        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(self.rodadas):
            a = randrange(2, num - 2 )
            x = pow(a, d, num) # x recebe a^d mod n

            if x == 1 or x == num - 1: continue

            for _ in range(s - 1):
                x = pow(x, 2, num) # x recebe x^2 mod n

            if x == num-1:
                continue_outer_loop = True
                break

            if continue_outer_loop:
                continue

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


_PRIMOS = {
    40: [701886890821, 145833959483],
    80: [627039700318015972526563, 17258016887375724832991],
    128: [281823669593790837253752644147169483721, 130149497672760612194506571911619816501],
    168: [53577236802344919857680454697879375307504576088927, 87638684248093818277104190540718855481257514307561],
    224: [9555570476784365604183370437996185501407868060964191196593302762711,
          11929041895336665885415245171139727014453130135351262254242333297897],
    256: [114521762541736572942175831292858847115978022297533643366336514473398296681259,
          11497252343705411796936888026497063219797667847435003967142716418374222663583],
    512: [
        11687988934730615085088752797282250379639560899809286759004164177768277835281798803059267186900959504974146952503606499671949523808002108371505014225254399,
        9168410681124379526825687234528018432644565710137901728047853853741091546896715023346942896824656130759676107735215870152242221051577686814226904972953379],
    1024: [
        4295990300262175286569706942624603289030853170013305621487189320909290520964802545145338800399484815159365124125403198362566442732009593596711195852873192072986050491252220531071318224293681475472026308169146527096204193789966266511659036316520094962867195427822246488653708362652700942480126595154117153523,
        4409718549809058718136578021895169493897055950058401244314045862374461586598984981007224313712892153648774256370485411186370689415870955619893596734411560764682357146184412176588364419785385753989349441526392553046352668450905445247325247631159384449414059944919242710890625383893079748692907335511203129151]
}

_NAO_PRIMOS = {
    40: [701886690821, 145834959483],
    80: [627039700318015972526565, 17258016887375724832992],
    128: [281823669593790837253752644147169483725, 130149497672760612194506571911619816502],
    168: [53577236802344919857680454697879375307504576088925, 87638684248093818277104190540718855481257514307563],
    224: [9555570476784365604183370437996185501407868060964191196593302762717,
          11929041895336665885415245171139727014453130135351262254242333297895],
    256: [114521762541736572942175831292858847115978022297533643366336514473398296681253,
          11497252343705411796936888026497063219797667847435003967142716418374222663587],
    512: [
        11687988934730615085088752797282250379639560899809286759004164177768277835281798803059267186900959504974146952503606499671949523808002108371505014225254397,
        9168410681124379526825687234528018432644565710137901728047853853741091546896715023346942896824656130759676107735215870152242221051577686814226904972953371],
    1024: [
        4295990300262175286569706942624603289030853170013305621487189320909290520964802545145338800399484815159365124125403198362566442732009593596711195852873192072986050491252220531071318224293681475472026308169146527096204193789966266511659036316520094962867195427822246488653708362652700942480126595154117153529,
        4409718549809058718136578021895169493897055950058401244314045862374461586598984981007224313712892153648774256370485411186370689415870955619893596734411560764682357146184412176588364419785385753989349441526392553046352668450905445247325247631159384449414059944919242710890625383893079748692907335511203129153]
}


if __name__ == '__main__':
    """Teste dos verificadores de primalidade
    """

    mr = MillerRabin()
    fermat = Fermat()
    numbers_lenght = _PRIMOS.keys()
    header = ["Tamanho", "Tempo-Medio", "Res-Esperado", "Resultado"]

    mr_results = open('Miller_Rabin_Results.csv', 'w+')
    dict_writer = csv.writer(mr_results, delimiter=',', quotechar='"')
    dict_writer.writerow(header)

    for lenght in numbers_lenght:
        media = 0
        for prime in _PRIMOS[lenght]:
            start = time.time()
            if mr.run(prime):
                result = 'true'
            else:
                result = 'false'
            media += (time.time() - start) / 2
        dict_writer.writerow([lenght, media, "True", result])
        media = 0
    dict_writer.writerow([])
    dict_writer.writerow(header)
    for lenght in numbers_lenght:
        for prime in _NAO_PRIMOS[lenght]:
            start = time.time()
            if mr.run(prime):
                result = 'true'
            else:
                result = 'false'
            media += (time.time() - start) / 2
        dict_writer.writerow([lenght, media, "False", result])

    mr_results.close()

    fermat_results = open('Fermat_Results.csv', 'w+')
    dict_writer = csv.writer(fermat_results, delimiter=',', quotechar='"')
    dict_writer.writerow(header)

    for lenght in numbers_lenght:
        media = 0
        for prime in _PRIMOS[lenght]:
            start = time.time()
            if fermat.run(prime):
                result = 'true'
            else:
                result = 'false'
            media += (time.time() - start) / 2
        dict_writer.writerow([lenght, media, "True", result])
        media = 0
    dict_writer.writerow([])
    dict_writer.writerow(header)
    for lenght in numbers_lenght:
        for prime in _NAO_PRIMOS[lenght]:
            start = time.time()
            if fermat.run(prime):
                result = 'true'
            else:
                result = 'false'
            media += (time.time() - start) / 2
        dict_writer.writerow([lenght, media, "False", result])

    fermat_results.close()

