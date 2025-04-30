'''
Aponta o local de destino mais próximo, usando a API de URL do Google Maps.

Syntax: python .\google-maps-route-scraping.py "<origin>" "['<dest1>', '<dest2>', ... , '<destN>']"

Sample:
    python .\google-maps-route-scraping.py "Belo Horizonte, MG" "['Juiz de Fora, MG', 'Contagem, MG']"

OUTPUT:
    O programa cria um arquivo com o nome out.txt contendo o relatório de comparação de distância e informa o destino mais próximo da origem.
'''

import time; init_t = time.time()
from urllib.parse import urlencode
import sys, re
from selenium import webdriver
from selenium.webdriver.common.by import By

origem = sys.argv[1]
destinos = eval(sys.argv[2])

try:
    assert len(destinos) >= 1
except AssertionError:
    sys.stdout.write('Parâmetro incorreto para lista de destinos.')
    
queries = [{'origin': origem, 'destination': dest} for dest in destinos]
urls = ['https://www.google.com/maps/dir/?api=1&'+urlencode(query) for query in queries]
del queries # libera memória

# Scraping initialize
browser = webdriver.Firefox()
browser.implicitly_wait(8)
distancias = []
assert len(urls) == len(destinos)
for url in urls:
    browser.get(url)
    element = browser.find_element(By.ID, 'section-directions-trip-0')
    match = re.search(r'[0-9]+.[0-9]+ km|[0-9]+ km', element.text).group()
    dist = match.split()[0]
    dist = int(dist.replace('.', ''))
    distancias.append((
        destinos[urls.index(url)],
        dist
    ))
browser.close()
# Scraping ends

with open('out.txt', 'w') as out:
    result = f'A distância entre {origem} e ...\n'
    minor = ('', 10**10)
    for pair in distancias:
        if pair[1] < minor[1]:
            minor = pair
        result += f'    ... {pair[0]} é {pair[1]} km\n'
    result += f'O destino mais próximo de {origem} é {minor[0]} com {minor[1]} km\n'
    final_t = time.time()
    result += f'\nTempo de execução: {final_t - init_t:.0f}s'
    out.write(result)
