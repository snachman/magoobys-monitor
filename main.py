import pandas as pd    
import requests
from bs4 import BeautifulSoup

def gather_data_for_debug():
    with open('data.html', 'w') as f:
        data = f.write(get_month_data_from_prod(1, 2023))
        f.close()





def get_month_data_from_prod(month, year):
    url = "https://www.magoobysjokehouse.com/calendar?month={month}&year={year}".format(month=month, year=year)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    return r.text


def read_data_from_debug():
    with open('data.html', 'r') as f:
        data = f.read()
        f.close()
    return data



def get_month_cells(html):
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    cells = tbody.find_all('td')
    return(cells)

def parse_cell(cell):
    return cell.text


def main(debug=False):
    if debug:
        month_data = read_data_from_debug()
    else:
        month_data = get_month_data_from_prod(1, 2023)
    
    month_cells = get_month_cells(month_data)

    for cell in month_cells:
        print(parse_cell(cell))





if __name__ == '__main__':
    main(debug=True)