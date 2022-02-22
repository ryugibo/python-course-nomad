import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  
  pagination = soup.find("div", {"class": "pagination"})
  
  links = pagination.find_all("a")
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))
  
  max_page = pages[-1]
  return max_page

def extract_job(html):
  title = html.find("h2", {"class": "jobTitle"}).find("span", recursive=False)["title"]
  company = html.find("span", {"class": "companyName"})
  if company:
    company.string.strip()
  else:
    company = None
  location = html.find("div", {"class": "companyLocation"})
  more_loc = location.find("span", {"class": "more_loc_container"})
  if more_loc is not None:
    more_loc.decompose()
  location = location.text
  job_id = html["data-jk"]
  return {
    "title": title,
    "company": company,
    "location": location,
    "link": f"https://www.indeed.com/viewjob?jk={job_id}"
  }
  
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scraping indeed {page}")
    result = requests.get(f"{URL}&start={page * LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("a", {"class": "result"})
    for result in results:
      jobs.append(extract_job(result))
  return jobs

def get_jobs():
  last_page = get_last_page()
  return extract_jobs(last_page)