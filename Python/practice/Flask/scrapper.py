import requests
from bs4 import BeautifulSoup


def extract_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find_all("a", {"class": "s-pagination--item"})
    last_page = int(pages[-2].span.string)
    return last_page


def extract_job(html):
    title = html.find("a", {"class", "s-link"})["title"]
    company, location = html.find(
        "h3", {"class", "fc-black-700"}).find_all("span", recursive=False)
    # ValueError: too many values to unpack 예외 관련 ↓
    # recursive=False : 자식 태그에 동일한 태그가 있을경우 첫번째 태그에서 find를 멈춤
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page+1}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = extract_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
