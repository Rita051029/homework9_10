import requests
from bs4 import BeautifulSoup
import lxml

url = "https://cash-backer.club/shops"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent": user}

session = requests.Session()

response = session.get(url, headers=headers)


for j in range(1, 6):
    url = f'https://cash-backer.club/shops?page={j}/'
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_cashbacks = soup.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
        name = soup.find('div', class_="mr-2 ml-md-1 my-1 d-none d-md-none d-sm-none d-lg-block d-xl-block")
        cashback = soup.find("div", class_="shop-rate")
        print(name.text, cashback.text)
        for i in all_cashbacks:
            try:
                if i.find('div', class_="shop-rate"):
                    company_name = i.find('div', class_="shop-title")
                    print(company_name.text)
                    cashback2 = i.find('div', class_="shop-rate")
                    print(cashback2.text)
                else:
                    print("Error")
            except ValueError:
                print("Error")
