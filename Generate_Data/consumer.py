import csv
import itertools
import generator
from ..measurementNames import longTermSurvival
from ..measurementNames import shortTermSurvival

def __main__():
    data = list()
    for n in range(100):
        reader = csv.reader(open(f'temp_{n}.csv'))
        data.append(list())
        sec = itertools.count()
        for l in reader:
            if l:
                data[-1].append((f'{n}_{next(sec)}', tuple(int(i) for i in l)))
        comparation_set = list()
        for l in data[-1]:
            for l_2 in data[-1]:
                pac_1_ = generator.Paciente(*l[1][0:9])
                pac_2_ = generator.Paciente(*l_2[1][0:9])
                comparation_set.append((
                        f'{l[0]}_vs_{l_2[0]}',
                        *l[1][:8],
                        generator.sofa(pac_1_),
                        generator.amib_total(pac_1_),
                        *l_2[1][:8],
                        generator.sofa(pac_2_),
                        generator.amib_total(pac_2_),
                        compare(l, l_2)
                ))
        csv.writer(open(f'temp_tot_{n}.csv', 'w')).writerows(comparation_set)
    data_set = set()
    for g in data:
        for l in g:
            data_set.add(l)
    comparation_set = list()
    if len(data_set) != 1000:
        print(len(data_set))
        raise Exception('clones')
    for l in data_set:
        for l_2 in data_set:
            pac_1_ = generator.Paciente(*l[1][0:9])
            pac_2_ = generator.Paciente(*l_2[1][0:9])
            comparation_set.append((
                    f'{l[0]}_vs_{l_2[0]}',
                    *l[1][:8],
                    generator.sofa(pac_1_),
                    generator.amib_total(pac_1_),
                    *l_2[1][:8],
                    generator.sofa(pac_2_),
                    generator.amib_total(pac_2_),
                    compare(l, l_2)
            ))
    csv.writer(open('temp_tot.csv', 'w')).writerows(comparation_set)


def compare(pac_1, pac_2):
    pac_1_ = generator.Paciente(*pac_1[1][0:9])
    pac_2_ = generator.Paciente(*pac_2[1][0:9])
    comparation = generator.compare_amib(pac_1_, pac_2_)
    if comparation is None:
        return ''
    if comparation == pac_1_:
        return pac_1[0]
    return pac_2[0]


if __name__ == '__main__':
    __main__()