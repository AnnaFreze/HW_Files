import requests
from bs4 import BeautifulSoup
import fake_headers
from pprint import pprint
import unicodedata
import json

headersgen = fake_headers.Headers(browser = 'firefox', os = 'win')
response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers = headersgen.generate())
htmldata = response.text

hhmain = BeautifulSoup(htmldata, 'lxml')
vacancy_list = hhmain.find('main', class_ = 'vacancy-serp-content')

vacancy_tags = vacancy_list.find_all("div", class_="vacancy-serp-item__layout")

vacancylist = list()

for vacancy_tag in vacancy_tags:

    salary = vacancy_tag.find('span', class_="bloko-header-section-2")
    if salary == None:
        salary_text = 'Заработная плата не указана'
    else:
        salary_text = salary.text
        salary_text = unicodedata.normalize("NFKD",salary_text)

    header_tag = vacancy_tag.find('h3')
    a_tag = header_tag.find('a')
    header_text = header_tag.text
    link = a_tag['href']

    company = vacancy_tag.find('a', class_="bloko-link bloko-link_kind-tertiary")
    company_text = company.text
    company_text = unicodedata.normalize("NFKD",company_text)


    vacanсy_city = vacancy_tag.find('div', class_="vacancy-serp-item__info")
    vacanсy_city_1 = vacanсy_city.find('div', class_="bloko-text")
    vacanсy_city_text = vacanсy_city.text
    if 'Москва' in vacanсy_city_text:
        vacanсy_city_text = 'Москва'
    elif 'Санкт-Петербург' in vacanсy_city_text:
        vacanсy_city_text = 'Санкт-Петербург'

    vacanсy_response = requests.get(link, headers = headersgen.generate())
    vacanсy = BeautifulSoup(vacanсy_response.text, 'lxml')
    vacanсy_body = vacanсy.find('div', class_="g-user-content")
    if vacanсy_body == None:
        vacanсy_body_text = 'Нет описания вакансии'
    else:
        vacanсy_body_text = vacanсy_body.text


    if "Django" or "Flask" in vacanсy_body_text:
        vacancylist.append({
            'link': link,
            'salary': salary_text,
            'company': company_text,
            'city': vacanсy_city_text
        })

with open("vacancies_3.json", "w", encoding= 'utf-8' ) as f:
    json.dump(vacancylist, f, ensure_ascii=False, indent=4)
