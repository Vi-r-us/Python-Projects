# Import Required Modules
import requests
from bs4 import BeautifulSoup
import pickle

file_name = "doctor_links"
url = 'https://doctors.ololrmc.com'
Doctors_link = []

# Getting all the Doctors profile links from each pages
# Iterating through 187 pages
for page in range(1, 188):

    # Opening a connection
    client = requests.get(url + "/search?sort=networks&page=" + str(page))
    page_html = client.text

    page_soup = BeautifulSoup(page_html, 'html.parser')

    # Getting all the doctors data
    Doctors = page_soup.find_all("div", class_="css-16pfjm6-ProviderContainer e16v8r6n0")

    # get all doctors profile link if not present already
    for doctor in Doctors:
        content = str(url + doctor.h2.a['href'].replace("'", ""))
        if content not in Doctors_link:
            Doctors_link.append(content)
        print(content)

    print(f"Page {page} scrapped !!!\n")

# Pickle the list for further use
f = open(file_name, "wb")
pickle.dump(Doctors_link, f)
f.close()
