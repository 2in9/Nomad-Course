import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():  # 페이지 갯수 불러오는 함수
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("ul", {"class": "pagination-list"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):  # 페이지 정보를 dict형식으로 변형시키는 함수
    h2 = html.find("h2", {"class": "jobTitle"})
    if h2.find("div") is not None:
        h2.find("div").decompose()
    title = h2.find("span")["title"]

    company = html.find("span", {"class": "companyName"})
    try:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    except:
        company = None

    location = html.find("div", {"class": "companyLocation"}).string

    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
    }


def extract_indeed_jobs(last_page):  # 받은 페이지 정보 넘겨주는 함수
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("a", {"class": "tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():  # main함수
    last_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_page)
    return jobs
