#skrypt łączy się ze wskazanym adresem
#zczytuje wskazane dane ze wskazanych 'class'
#zapisuje je w tabeli i tabelę w pliku

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import csv


#define url
url = 'https://www.biznesradar.pl/fundusze/ppk'

# Ask hosting server to fetch url
pages = requests.get(url)
pages.text

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text, 'lxml')
soup

# Searching specific attributes of tags

nazwy = soup.find_all('td', class_='td-left')
aktualna_wartosc = soup.find_all('span', class_='q_ch_act')
data_notowania = soup.find_all('span', class_='q_ch_date')
zmiana_wartosci = soup.find_all('span', class_='q_ch_per cplus')

#loops
lista_nazw_ppk=[]
for i in nazwy:
    nazwy=i.text
    lista_nazw_ppk.append(nazwy)

lista_wartosci_ppk=[]
for i in aktualna_wartosc:
    aktualna_wartosc=i.text
    lista_wartosci_ppk.append(aktualna_wartosc)

lista_dat_ppk=[]
for i in data_notowania:
    data_notowania=i.text
    lista_dat_ppk.append(data_notowania)


tabela_ppk = pd.DataFrame({'Nazwa PPK':lista_nazw_ppk,'Aktualna wartość':lista_wartosci_ppk,'Data notowania':lista_dat_ppk})
#print(tabela_ppk)

#save csv
now = datetime.now()
today = now.strftime("%d-%m-%Y")
adres_pliku = f'webscraping/{today}.csv'
tabela_ppk.to_csv(adres_pliku, index=False)


print('zapisano powyższą tabelę w pliku '+adres_pliku)
