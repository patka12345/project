from algorytm2 import alg2
from algorytm1 import alg1
from generator import gen
import pandas as pd

parameter_path = 'parametry.xlsx'
generated_flights =  'wygenerowane_loty.xlsx'
flights = 'loty.xlsx'


nn = pd.read_excel(parameter_path, sheet_name = 'Sheet1')
m_min = int(nn['wartość parametru'][0])
m_max = int(nn['wartość parametru'][1])
n_min = int(nn['wartość parametru'][2])
n_max = int(nn['wartość parametru'][3])

choice = int(nn['opcja'][0])

writer1 = pd.ExcelWriter('wynik_al1.xlsx', engine='xlsxwriter',
                         datetime_format='hh:mm:ss')
writer2 = pd.ExcelWriter('wynik_al2.xlsx', engine='xlsxwriter',
                         datetime_format='hh:mm:ss')

if choice == 1:
    gen(parameter_path)

    if n_min != 0 and n_max != 0:
        if m_min != 0:
            alg1(m_min, generated_flights, 'sheet1', 'wynikLL', writer1)
            alg1(m_min, generated_flights, 'sheet2', 'wynikLP', writer1)
        if m_max != 0:
            alg1(m_max, generated_flights, 'sheet1', 'wynikPL', writer1)
            alg1(m_max, generated_flights, 'sheet2', 'wynikPP', writer1)
    else:
        if m_min != 0:
            alg1(m_min, generated_flights, 'sheet1', 'wynikL', writer1)
        if m_max != 0:
            alg1(m_max, generated_flights, 'sheet1', 'wynikP', writer1)

    writer1.save()

    if n_min != 0 and n_max != 0:
        if m_min != 0:
            alg2(m_min, generated_flights, 'sheet1', 'wynikLL', writer2)
            alg2(m_min, generated_flights, 'sheet2', 'wynikLP', writer2)
        if m_max != 0:
            alg2(m_max, generated_flights, 'sheet1', 'wynikPL', writer2)
            alg2(m_max, generated_flights, 'sheet2', 'wynikPP', writer2)
    else:
        if m_min != 0:
            alg2(m_min, generated_flights, 'sheet1', 'wynikL', writer2)
        if m_max != 0:
            alg2(m_max, generated_flights, 'sheet1', 'wynikP', writer2)
    writer2.save()

elif choice == 2:

    if m_min != 0:
        alg1(m_min, flights, 'sheet1', 'wynikL', writer1)
    if m_max != 0:
        alg1(m_max, flights, 'sheet1', 'wynikP', writer1)
    writer1.save()

    if m_min != 0:
        alg2(m_min, flights, 'sheet1', 'wynikL', writer2)
    if m_max != 0:
        alg2(m_max, flights, 'sheet1', 'wynikP', writer2)
    writer2.save()

else:
    print('\npole “opcja” w pliku “parametry.xlsx” '
          'nie zostało uzupełnione prawidłowo')
