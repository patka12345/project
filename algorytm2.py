from datetime import time, datetime, timedelta
from operator import itemgetter
import numpy as np
import pandas as pd

def alg2(m ,sciezka, sheet_in, sheet_out, writer):

    #wczytanie plików Excel
    excel = pd.read_excel(sciezka, sheet_name = sheet_in,
                          index = False)
    a = excel['przylot'].tolist()
    d = excel['odlot'].tolist()
    fn = excel['numer lotu'].tolist()
    n_fl = len(a)
    a = [i.strftime("%H:%M:%S") for i in a]
    d = [i.strftime("%H:%M:%S") for i in d]
    N0 = [[a[i],d[i],fn[i]] for i in range(len(a))]

    # zmiana formatu danych na liczby naturalne
    M = ['G{}'.format(i) for i in range(1, m+1)]
    FMT = '%H:%M:%S'
    N0 = sorted(N0, key=itemgetter(1))

    N = [[N0[i][0], N0[i][1]] for i in range(len(a))]
    fn = [N0[i][2] for i in range(len(a))]
    a = [datetime.strptime(time[0], FMT) for time in N]
    d = [datetime.strptime(time[1], FMT) for time in N]
    b = timedelta(minutes=5)
    dic = {}
    nn = 0
    times = []

    while min(a)+nn*b <= max(d):
        dic.update({(min(a)+nn*b).strftime("%H:%M:%S"):nn})
        times.append((min(a)+nn*b).strftime("%H:%M:%S"))
        nn += 1

    def replace(list, dictionary):
        new_list = []
        for i in list:
            for j in i:
                if j in dictionary:
                    new_list.append(dictionary[j])
                else:
                  new_list.append(j)
        return new_list

    fl = replace(N,dic)
    a = [fl[i] for i in range(len(fl)) if i%2 == 0]
    d = [fl[i] for i in range(len(fl)) if i%2 != 0]
    matrix = np.zeros((len(dic), m))

    new = []
    for x in dic:
        new.append(dic[x])

    matrix = np.hstack((np.array(new)[:, np.newaxis], matrix))
    k = 0
    n = 1
    g = [0 for i in range(m)]
    apron = []
    fn1 = fn.copy()
    gg = g.copy()
    i = gg.index(max(gg)) + 1

    # algorytm:
    while a:
        if not all([x == -1 for x in gg]):
            if all([matrix[l][i] == 0 for l in range(a[0], d[0]+1)]):
                for j in range(a[0],d[0]+1):
                    matrix[j][i] += n
                gg[i-1] = d[0]
                g[i-1] = d[0]
                # k = i
                n += 1
                a.remove(a[0])
                d.remove(d[0])
                fn1.remove(fn1[0])
                gg = g.copy()
                i = g.index(max(g)) + 1
            else:
                gg[i-1] = -1
                i = gg.index(max(gg))+1
        else:
            apron.append(fn1[0])
            n += 1
            a.remove(a[0])
            d.remove(d[0])
            fn1.remove(fn1[0])
            gg = g.copy()
            i = g.index(max(g)) + 1

    # przekształcanie macierzy na ostateczną tabelę:
    matrix = matrix.tolist()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j])

    fndic = {}
    for i in range(0,len(fn)):
        fndic.update({i+1:fn[i]})

    for i in range(len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] in fndic:
                matrix[i][j] = fndic[matrix[i][j]]

    table = pd.DataFrame()
    for j in range(1,len(matrix[0])):
        table[M[j-1]] = pd.Series([k[j] for k in matrix])
    table['time'] = pd.Series(times)
    table.set_index('time')
    timetable = table.set_index('time')

    # zapisywanie do Excela:
    timetable.to_excel(writer, sheet_name= sheet_out)
    mm = pd.DataFrame({'liczba bramek': [m], 'liczba lotów': n_fl})
    # excel.rename(columns=lambda x: x[1], inplace=True)
    l = m
    if apron:
        apron = pd.DataFrame(apron)
        apron.columns = ['apron']
        apron.to_excel(writer, sheet_name = sheet_out, startcol = m+2)
        mm.to_excel(writer, sheet_name = sheet_out, startcol = m+5,
                    index = False)
        l = m + 3
    mm.to_excel(writer, sheet_name = sheet_out, startcol = l+2,
                index = False)
    excel.to_excel(writer, sheet_name = sheet_out, startcol = l+5,
                   index = False)

    count = 0
    for i in range(m):
        for j in range(len(timetable)):
            if matrix[j][i] == 0:
                count += 1

    statistic1 = round(count / (len(timetable) * m), 5)
    statistic2 = len(apron) / (n_fl - len(apron))
    print('algorytm 2, liczba lotów:', n_fl, 'liczba bramek:', m)
    print('stosunek wolnych slotów czasowych do wszystkich',
          statistic1 * 100, '%')
    print('stosunek samolotów na apronie do wszystkich',
          round(statistic2, 5) * 100, '%\n')
