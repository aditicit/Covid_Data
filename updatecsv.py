import pandas as pd
import pathlib
import requests
from bs4 import BeautifulSoup

def update_csv_file():
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    soup.find_all('td')

    covid_data = []

    data_iterator = iter(soup.find_all('td'))

    while True:
        try:
            country = next(data_iterator).text
            print(country)
            confirmed = next(data_iterator).text
            print(confirmed)
            deaths = next(data_iterator).text
            print(deaths)
            continent = next(data_iterator).text

        # For 'confirmed' and 'deaths', make sure to remove the commas and convert to int
            covid_data.append((
            country,
            eval(confirmed.replace(',', '')),
            eval(deaths.replace(',', '')),
            continent
        ))

        # StopIteration error is raised when there are no more elements left to iterate through
        except StopIteration:
            break

    covidreport = pd.DataFrame(covid_data)
    covidreport=covidreport.rename(columns={0: 'Country', 1: 'Confirmed', 2:'Deaths', 3:'Continents'})

    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("./datasets").resolve()
    covidreport.to_csv(DATA_PATH.joinpath("covidreport.csv"), index=False)
