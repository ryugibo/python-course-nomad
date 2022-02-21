import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  print(pages)

def extract_jobs(last_page):
  return []
  
def get_jobs():
  last_page = get_last_page()
  return extract_jobs(last_page)
