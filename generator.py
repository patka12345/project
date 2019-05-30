import pandas as pd
from datetime import datetime, timedelta, time
import numpy as np
import random

def gen(sciezka):
    excel = pd.read_excel(sciezka, sheet_name = 'Sheet1')
    samolot = excel['samolot'].tolist()
    czas = excel['turnaround time'].tolist()

    parametr = excel['wartość parametru'].tolist()
    flights = [parametr[j] for j in [2,3] if parametr[j] != 0]

    writer = pd.ExcelWriter('wygenerowane_loty.xlsx', engine='xlsxwriter', datetime_format='hh:mm:ss')

    for j in range(len(flights)):
        n = flights[j]
        pairs = [[samolot[i], timedelta(minutes=czas[i])] for i in range(len(samolot)) if len(samolot) == len(czas)]
        delta = timedelta(minutes=5)
        start_time = '00:00:00'
        start_time = datetime.strptime(start_time, '%H:%M:%S')
        new_flights = []
        i = 0

        while i < n:
            pair = random.choice(pairs)
            plane = pair[0]
            arrival = np.random.choice(288)*delta + start_time
            departure = arrival + pair[1]
            arrival = arrival.strftime('%H:%M:%S')
            departure = departure.strftime('%H:%M:%S')
            if departure > arrival:
                flight_number = 'lot' + str(i+1)
                new_flights.append([plane, arrival, departure, flight_number])
                i += 1

        table = [[new_flights[i][0], pd.to_datetime(new_flights[i][1]), pd.to_datetime(new_flights[i][2]), new_flights[i][3]] for i in range(len(new_flights))]
        table = pd.DataFrame(table)
        table.columns = ['samolot', 'przylot', 'odlot', 'numer lotu']
        table.to_excel(writer, sheet_name='sheet'+str(j+1))
    writer.save()
