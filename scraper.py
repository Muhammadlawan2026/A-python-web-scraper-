import requests
from bs4 import BeautifulSoup

# shafin yanar gizo da za mu ciro bayanai daga gare shi (Gwaji)
url = "http://books.toscrape.com/"

try:
    print("[+] muna hadawa da shafin yanar gizo...")
    response = requests.get(url,timeout=5)

    if response.status_code == 200:
        print("[+] hadin ya yi nasra! muna ciro bayanan littattafai...\n")

        # parse HTML content
        soup = BeautifulSoup(response.text, "html.parser") 

        # Nemo dukkan littattafan da ke shafin
        books = soup.find_all("article", class_="product_pod")

        print(f"=== AN SAMU LITTATTAFAN {len(books)} A SHAFIN FARKO ===\n")

        for index, book in enumerate(books[:5], 1): 
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            print(f"{index}. sunan littafi: {title}")
            print(f" farashi: {price}\n")

    else:

        print(f"[-] AKa samu matsala wajen bude shafi. status code: {response.status_code}")

except Exception as e:
    print(f"[-] kuskure: {e}")