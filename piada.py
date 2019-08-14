 import requests
    from bs4 import BeautifulSoup

    url = 'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria'

    r = requests.get(url)

soup = BeautifulSoup = soup.find_all('table', class_='textosm')

    url= 'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria'

    for lista_td in lista_piada:
        lista=lista_td.find_alii('td')
        for lista_dados in lista:
            print(lista_dados.next_element)