# Import all Libraries
import requests
from bs4 import BeautifulSoup
import sqlite3
import pickle

file_name = "doctor_links"
f = open(file_name, "rb")
loaded_links = pickle.load(f)
f.close()

print("There are a total of " + str(len(loaded_links)) + " no. of doctors\n")

conn = sqlite3.connect("Doctors_Data.db")
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS doctors""")
c.execute("""CREATE TABLE doctors(
                Name TEXT,
                Specialities TEXT,
                Profile_URL TEXT,
                Address TEXT,
                Phone_Number TEXT,
                Fax TEXT)""")

for link in loaded_links:
    client = requests.get(link)
    page_html = client.text
    page_soup = BeautifulSoup(page_html, 'html.parser')

    address_in_text = ""
    phone_no = ""
    fax_no = ""

    upper = page_soup.find("div", class_="row panel pt-m mb-m text-center")

    doctor_name = str(upper.h2.text)
    doctor_specialities = str(upper.span.text)

    print(f"Doctor Name : {doctor_name}\n"
          f"Doctor Specialities : {doctor_specialities}")

    lower = page_soup.find('div', class_="row panel mb-m")

    address_in_text_list = []
    phone_no_list = []
    fax_no_list = []

    try:
        all_address = lower.find_all('div', class_="row mt-m mb-m horizontal-rule location")
        for address in all_address:

            temp = f"[{str(address.find('h2', class_='fw-6 fs-s location-title').text)} ," \
                   f"{str(address.find('span', {'itemprop': 'streetAddress'}).span.text)} " \
                   f"{str(address.find('span', {'itemprop': 'addressLocality'}).text)} ," \
                   f"{str(address.find('span', {'itemprop': 'addressRegion'}).text)} " \
                   f"{str(address.find('span', {'itemprop': 'postalCode'}).text)}]"

            if temp not in address_in_text_list:
                address_in_text_list.append(temp)

            try:
                temp = f"{str(address.find('a', class_='location-phone-link').text)}"
                if temp not in phone_no_list:
                    phone_no_list.append(temp)
            except:
                phone_no_list = phone_no_list

            try:
                temp = f"{str(address.find_all('div', class_='col-xs-10 col-sm-10')[2].text)}"
                if temp not in fax_no_list:
                    fax_no_list.append(temp)
            except:
                fax_no_list = fax_no_list
    except:
        address_in_text = ""

    for item in address_in_text_list:
        address_in_text += f"{item}___"

    for item in phone_no_list:
        phone_no += f"{item}___"

    for item in fax_no_list:
        fax_no += f"{item}___"

    print(f"Address is {address_in_text}\n"
          f"Phone Number is {phone_no}\n"
          f"Fax Number is {fax_no}\n")

    c.execute("""INSERT INTO doctors VALUES(?,?,?,?,?,?)""", (doctor_name, doctor_specialities, link, address_in_text, phone_no, fax_no))
    conn.commit()

conn.close()
