from bs4 import BeautifulSoup
import requests
URL = "https://engels-vodokanal.ru/index.php?show=water"
address = [
    "Персидского",
    "Пристанская"
]
resp = requests.get(URL)

# f = open("html_txt/otkl_2.html").read()
# soup = BeautifulSoup(f, "html.parser")
soup = BeautifulSoup(resp.text, "html.parser")
row = soup.find('div', id=lambda x: x and x.startswith('nowaterdiv_'))
if row:
    # print(row[0].text.strip())
    print(row.text.strip())
    for a in address:
        if a in row.text:
            print("Наш адрес отключат")
else:
    print("Нет отключений")

