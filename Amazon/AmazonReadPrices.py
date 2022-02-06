import requests
from bs4 import BeautifulSoup


def read_price(siteUrl):
    try:
        headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36' }
        page = requests.get(siteUrl,headers=headers)
        soup = BeautifulSoup(page.content, features="lxml")
        title = soup.find(id='productTitle')
        if title:
            title = title.get_text().strip()
            print(title)
        else:
            print('Title Not Found')

        for t in soup.select('[class="a-price"]'):
            print(t)
            print('-' * 80)


    except AttributeError:
        print("NoneType")

def __main__():
    web_url = input('Enter the url of the product: ')
    read_price(web_url)


        

