import json
import skills
import requests
import bs4
import fake_headers
from pprint import pprint

headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

response = requests.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=headers_dict)
main_html_data = response.text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")

vacancies_tag = main_html.find("div", id_="a11y-main-content")
vacancy_tags = main_html.find_all('div', class_ = "serp-item")

parsed_data = []

for vacancy_tag in vacancy_tags:
    h3_tag = vacancy_tag.find('h3')
    span_tag = h3_tag.find('span')
    a_tag = span_tag.find('a')
    link = a_tag['href']

    company_tag = vacancy_tag.find('a', class_ ="bloko-link bloko-link_kind-tertiary")
    company = company_tag.text

    response = requests.get(link, headers=headers.generate()).text
    vacancy_html = bs4.BeautifulSoup(response, "lxml")

    salary_tag = vacancy_html.find("span", class_="bloko-header-section-2 bloko-header-section-2_lite")
    salary = salary_tag.text

    city_tag = vacancy_html.find ("div", {"data-qa": "vacancy-serp__vacancy-address"})
    city = city_tag.text

    if "Django" or "Flask" in skills.skills_required(link):
        parsed_data.append(
            {"link": link,
            "salary": salary,
            "company": company,
            "city": city
            }
        )
#pprint(parsed_data)

with open("vacancies.json", "w", encoding= 'utf-8' ) as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)

