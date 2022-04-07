import re
import requests
from bs4 import BeautifulSoup


def read_price(site_url):
    try:
        i = 0
        headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36' }
        page = requests.get(site_url,headers=headers)
        soup = BeautifulSoup(page.content, features="lxml")
        title = soup.find(id='productTitle')
        if title:
            title = title.get_text().strip()
            print(title)
        else:
            print('Title Not Found')

        for tag in soup.select('[class="a-price"]'):
            if i == 0 :
                i = i + 1
                tag_string = str(tag)
                tag_float = re.findall(r"[-+]?(?:\d*\,\d+|\d+)",tag_string)
                print('-' * 20)
                print(tag_float[0] + '€')
                print('-' * 20)
                
            

    except AttributeError:
        print("NoneType")

def read_lib():
    print('i have read a library')

def main():
    read_lib()

if __name__ == "__main__":
    main()
        

