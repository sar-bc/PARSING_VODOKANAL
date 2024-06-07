from bs4 import BeautifulSoup
import requests

URL = "https://engels-vodokanal.ru/index.php?show=water"
address = [
    "Приволжский",
    "Гагарина"
]


def pars():
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


resp = None
try:
    resp = requests.get(URL)

    if resp.status_code == 200:
        pars()
    else:
        print("Страница не найдена")

except requests.exceptions.ConnectionError:
    print('Seems like dns lookup failed..')
except requests.exceptions.ReadTimeout:
    print('Oops. Read timeout occured')
# except requests.exceptions.ConnectTimeout:
#     print('Oops. Connection timeout occured!')
