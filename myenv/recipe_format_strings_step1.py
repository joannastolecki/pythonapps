# DANE WEJŚCIOWE
data = [
    (1000,10),
    (2000,17),
    (2500,170),
    (2500,-170)
]

# wyświetlanie nagłówka 
print('PRZYCHOD | ZYSK   | PROCENT')

# ten szablon wyrównuje i wyświetla dane w odpowiednim formacie 
TEMPLATE = '{revenue:>8,} | {profit:>+7} | {percent:>8.2%}'

# wyświetlanie wierszy z danymi 
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue,profit=profit,percent=profit/revenue)
    print(row)