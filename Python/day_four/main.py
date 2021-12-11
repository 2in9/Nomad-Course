import requests
from bs4 import BeautifulSoup

indeed_r = requests.get(
    "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")
indeed_s = BeautifulSoup(indeed_r.text, 'html.parser')

pagination = indeed_s.find("ul", {"class": "pagination-list"})

pages = pagination.find_all('a')

spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[0:-1])
