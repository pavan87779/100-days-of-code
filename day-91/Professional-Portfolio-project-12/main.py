import requests

from bs4 import BeautifulSoup

import csv



URL = 'https://example.com/products'  # Replace with your target URL

HEADERS = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}



def fetch_data(url):

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:

        return response.text

    else:

        print(f'Failed to retrieve data: {response.status_code}')

        return None



def parse_data(html):

    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_='product-item')  # Modify based on target site's structure

    data = []

    for item in items:

        title = item.find('h2', class_='product-title').text.strip()

        price = item.find('span', class_='product-price').text.strip()

        data.append((title, price))

    return data



def save_to_csv(data, filename='products.csv'):

    with open(filename, 'w', newline='') as file:

        writer = csv.writer(file)

        writer.writerow(['Product Name', 'Price'])

        writer.writerows(data)

    print(f'Data saved to {filename}')



if __name__ == "__main__":

    html = fetch_data(URL)

    if html:

        extracted_data = parse_data(html)

        save_to_csv(extracted_data)

