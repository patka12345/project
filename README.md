# Jet bridge allocation simulator

Project aims to allocate jet brigdes to planes to maximize bridges usage time. Depending on chosen algoritm, more or less aircrafts park at jet brigde, rest of them at apron. There are 2 algorithms implemented: greedy algorithm and it's modification.

Before running project, make sure that:
- [x] all files are in the same folder
- [x] files *wynik_al1.xlsx* and *wynik_al2.xlsx* are closed
- [x] you have installed Python 3.7, PyCharm 2018.2.2, Excel 2016
- [x] you have installed Python libraries: NumPy, Pandas, datetime, operator, random

There are 2 available modes:

### Mode 1
Mode 1 allows to simulate allocation depending on generated random list of flight.

1. In *parametry.xlsx* fill columns:
- *samoloty*: name of desired plane
- *turnaround time*: time between departure and arrival in minutes, must be natural number  
- value of *opcja* to 1 to set Mode 1

and column *wartosc parametru* in rows:  
- value of a row *minimalna liczba bramek* to any natural number to choose minimal number of jet brigdes
- value of a row *maksymalna liczba bramek* to any natural number to choose maximum number of jet brigdes
- value of a row *minimalna liczba lotów* to any natural number to choose minimal number of generated flights
- value of a row *maksymalna liczba lotów* to any natural number to choose minimal number of generated flights

3. Run *symulator.py*
4. Results are visible in *wynik_al1.xlsx* and *wynik_al2.xlsx*.

### How to read results

Results are stored in *wynik_al1.xlsx* for algorithm 1 and in *wynik_al2.xlsx* for algorithm 2. Simulator shows results for pairs of extreme values.
Sheets are named *wynikLP*, *wynikLL*, *wynikPL*, *wynikPP*, *wynikP*, *wynikL*, where L means left extreme value (minimum) and P right extreme value (maximum).
First L or P is assigned to number of jet bridges, second to number of flights. Single L or P means that number of jet bridges or flights is set as single value, so simulation is made only for one pair of extremes.  

Examples:
- *wynikLP* shows result for minimum number of jet brigdes and maximum number of flights
- *wynikL* shows 1) result for minimum number of jet brigdes with one set number of flights or 2) result for minimum number of flights with one set number of jet brigdes

Additionaly, there are 2 statistics printed in console:
- the ratio of free time slots to all available during the day
- the ratio of planes at apron to all planes during the day


### Mode 2
Mode 2 allows to simulate allocation depending on flights list provided by user.  
1. To enter flights list, open *loty.xlsx* and set up options:  

| Option | Description |
| --- | --- |
| przylot | arrival, time when plane park at airport, must be in excel time format |
| odlot | departure, time when plane leaves gate at airport, must be in excel time format |
| numer lotu | flight number, will be displayed in final table |

2. Then in *parametry.xlsx* set:  
- value of column *opcja* to 1 to set Mode 1  

and column *wartosc parametru* in rows:  
- value of a row *minimalna liczba bramek* to any natural number to choose minimal number of jet brigdes
- value of a row *maksymalna liczba bramek* to any natural number to choose maximum number of jet brigdes

3. Run *symulator.py*
4. Results are visible in *wynik_al1.xlsx* and *wynik_al2.xlsx*.
