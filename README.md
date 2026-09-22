# Bincom Python Basic Developer Test

## Run

1. Install Python 3 and PostgreSQL.
2. Create the database:
   `CREATE DATABASE bincom_test;`
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it in PowerShell:
   `.venv\\Scripts\\Activate.ps1`
5. Install packages:
   `pip install -r requirements.txt`
6. Set PostgreSQL environment variables using `.env.example` as a guide.
7. Run:
   `python main.py`

## Dataset result

The supplied HTML contains 76 colour entries. `BLEW` is treated as the obvious typo `BLUE`; `ARSH` is preserved because its intended correction is not established by the source.

Frequencies:

- BLUE: 25
- WHITE: 14
- RED: 8
- GREEN: 7
- ORANGE: 7
- BROWN: 5
- PINK: 4
- YELLOW: 3
- ARSH: 1
- CREAM: 1
- BLACK: 1

Mostly worn: BLUE (25).

Because colour names are categorical, a literal arithmetic mean/median of the names is undefined. This implementation interprets the test as asking for the mean/median of the distinct-colour frequencies.

Mean frequency: 6.91; closest colours: GREEN and ORANGE.
Median frequency: 7; colours: GREEN and ORANGE.
Population variance of frequencies: 48.4463.
Probability of RED: 8/76 = 10.53%.
Sum of first 50 Fibonacci numbers (0,1,1,2,...): 20,365,011,073.

The PostgreSQL table is created automatically by `database.py`.
