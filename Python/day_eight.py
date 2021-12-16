import requests
from bs4 import BeautifulSoup
import csv


def extract_link_and_comp():
    result = requests.get("https://www.alba.co.kr/")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div", {"id": "MainSuperBrand"}
                        ).find_all("li", {"class", "impact"})

    links = []
    companys = []
    for result in results:
        links.append(result.a["href"])
        companys.append(result.find("span", {"class": "company"}).string)

    return [links, companys]


def extract_alba(result):
    try:
        place = result.find(
            "td", {"class": "local first"}).get_text(strip=True).replace(u'\xa0', u' ')
    except:
        place = None
    try:
        title = result.find("td", {"class": "title"}).find(
            "span", {"class": "company"}).string
    except:
        title = None
    try:
        time = result.find("td", {"class": "data"}).span.string
    except:
        time = None
    try:
        pay = result.find("td", {"class": "pay"}).span.string + result.find(
            "td", {"class": "pay"}).find("span", {"class": "number"}).string
    except:
        pay = None
    try:
        date = result.find(
            "td", {"class": "regDate last"}).get_text(strip=True)
    except:
        date = None

    return {
        'place': place,
        'title': title,
        'time': time,
        'pay': pay,
        'date': date
    }


def extract_albas(link):
    albas = []
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div", {"id": "NormalInfo"}).tbody.find_all("tr")
    for result in results[::2]:
        albas.append(extract_alba(result))

    return albas


def save_to_file(albas, company):
    file = open(f".\Python\CSV\{company}.csv", mode="w",
                encoding="utf-8", newline='')
    newline = ''
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for alba in albas:
        writer.writerow(list(alba.values()))
    file.close()
    return


links, companys = extract_link_and_comp()
for x in range(len(links)):
    print(companys[x])
    albas = extract_albas(links[x])
    save_to_file(albas, companys[x].replace('/', '&'))
