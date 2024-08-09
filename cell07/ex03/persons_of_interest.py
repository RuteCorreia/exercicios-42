#!/usr/bin/env python3
from datetime import datetime

def famous_births(historical_figures):
    
    figures_list = [(name, details['date_of_birth']) for name, details in historical_figures.items()]
    
    def parse_date(date_str):
        return datetime.strptime(date_str, '%Y')
    
    figures_list.sort(key=lambda x: parse_date(x[1]))
    
    for name, date_of_birth in figures_list:
        print(f"{name}, is a great scientist born in: {date_of_birth}")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}


famous_births(women_scientists)