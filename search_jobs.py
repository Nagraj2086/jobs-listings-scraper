import csv
keyword=input('Enter job Keyword..').strip().lower()
if not keyword:
    print('not found')
else:
    matching_jobs=[]


    with open('jobs.csv','r',newline='',encoding='utf-8-sig') as file:
        reader=csv.DictReader(file)
        for job in reader:
            title=job.get('title','').lower()
            company=job.get('company','').lower()
            location=job.get('location','').lower()
            if keyword in title or keyword in company or keyword in location:
                matching_jobs.append(job)
    if matching_jobs:
        with open('filtered_jobs.csv','w',newline='',encoding='utf-8-sig') as file:
            fieldnames=['title','company','location','apply_url']
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(matching_jobs)
    else:
        print('no matching jobs..')