import requests
from bs4 import BeautifulSoup

home_url = "https://www.pmi.com"
greeceJobs_url = "/careers/explore-our-job-opportunities?locations=Greece"
url = f"{home_url}{greeceJobs_url}"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

fdPages = soup.find("div", class_="pages-nav--numbers")
pages = len(fdPages.find_all()) + 1

for page in range(1, pages):
    url = f"{home_url}{greeceJobs_url}&page={page}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break

    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    jobs = soup.find_all("a", class_="job-row", href=True)

    for job in jobs:
        print(job.h3.text.strip(), end=" ")
        job_url = f"{home_url}{job['href']}"
        print(job_url)
