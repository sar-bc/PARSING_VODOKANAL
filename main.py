from bs4 import BeautifulSoup


f = open("html_txt/otkl_1.html").read()
soup = BeautifulSoup(f, "html.parser")
row = soup.find_all('div', id=lambda x: x and x.startswith('nowaterdiv_'))
print(row)

