import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://ihub.co.ke/jobs")

soup = BeautifulSoup(response.text, 'lxml')

jobs = soup.find_all(class_="container-fluid jobs-list")
post_title = []
post_title_link = []
company_name = []
post_location = []
post_desc = []
post_type = []
post_date = []

for post in jobs:
    job_data = post.find_all(class_='container-fluid jobsboard-row')
    for job in job_data:
        h3 = job.find('h3')
        post_title_header = h3.select('[href]')
        post_title_link.append(post_title_header[0]['href'])
        post_title.append(post_title_header[0].get_text())
        post_type.append(job.find(class_='job-cat').get_text())
        post_date.append(job.find(class_='job-time').get_text())
        post_desc.append((job.find(class_='post-description').get_text().strip().replace('\n', ' ')))
        post_location.append(job.find(class_='job-location').get_text())

ihub_post = pd.DataFrame({
    "Post Title": post_title,
    "Post Type": post_type,
    "Post Description": post_desc,
    "Post Location": post_location,
    "Post Date": post_date
})

ihub_post.to_csv('ihub.csv')
