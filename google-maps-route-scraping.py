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
browser = webdriver.Firefox()
browser.implicitly_wait(8)
distancias = []
assert len(urls) == len(destinos)
for url in urls:
    browser.get(url)
    element = browser.find_element(By.ID, 'section-directions-trip-0')
    distancias.append((
            destinos[urls.index(url)],
            re.search(r'[0-9]+.[0-9]+ km|[0-9]+ km', element.text).group()
    ))
browser.close()
sys.stdout.write(f'A distância entre {origem} e ...\n')
for dist in distancias:
    sys.stdout.write(f'    ... {dist[0]} é {dist[1]}\n')
final_t = time.time()
sys.stdout.write(f'Tempo de execução: {final_t - init_t:.0f}s')


