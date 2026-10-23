import csv
import requests
from bs4 import BeautifulSoup
url="https://realpython.github.io/fake-jobs/"
response=requests.get(url,timeout=15)
soup=BeautifulSoup(response.text,"html.parser")
results=soup.find(id='ResultsContainer')
if not results:
    print('Job listings not found..')
job_cards=results.find_all("div",class_="card-content")
jobs=[]
# print("Total Job Cards:",len(job_cards))
for card in job_cards:
    title_element=card.find('h2',class_='title')
    company_element=card.find('h3',class_='company')
    location_element=card.find('p',class_='location')
    links=card.find_all('a')
    apply_url=links[1].get('href','') if len(links)>1 else ""

    title=(title_element.get_text(strip=True) if title_element else "N/A")
    company=(company_element.get_text(strip=True) if company_element else "N/A")
    location=(location_element.get_text(strip=True) if location_element else "N/A")

    job={
        'title':title,
        'company':company,
        'location':location,
        'apply_url':apply_url,
    }
    
    jobs.append(job)
with open('jobs.csv','w',newline="",encoding='utf-8-sig') as file:
    fieldnames=['title','company','location','apply_url']
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(jobs)
print(f'successfully saved {len(jobs)}')
