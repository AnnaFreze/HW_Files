import json
import bs4
import fake_headers
import requests
from pprint import pprint

headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

response = requests.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2", headers=headers_dict)
main_html_data = response.text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")

vacancy_tags = main_html.find_all("div", class_="vacancy-serp-item__layout")

parsed_data = []
result_list = []

for vacancy_tag in vacancy_tags:
    h3_tag = vacancy_tag.find('h3')
    span_tag = h3_tag.find('span')
    a_tag = span_tag.find('a')
    link = a_tag['href']

    company_tag = vacancy_tag.find("div", class_= "vacancy-serp-item__meta-info-company")
    company = company_tag.text

    city_tag = vacancy_tag.find("div", {"data-qa": "vacancy-serp__vacancy-address"})
    city = city_tag.text

    response = requests.get(link, headers=headers.generate())
    vacancy_data = response.text
    vacancy_html = bs4.BeautifulSoup(vacancy_data, "lxml")

    # salary_tag = vacancy_html.find('div', {"data-qa": "vacancy-salary"})
    # salary = salary_tag.text
    # print(salary)

    description_tag = vacancy_html.find("div", class_="vacancy-description")
    description = description_tag.text.split(' ')
    low_description = [x.lower() for x in description]
    if "django" or "flask" in low_description:
        result_list.append(link)
        parsed_data.append(
            {"link": link,
             "company": company,
             "city": city,
             "salary": "unknown"}
        )


#pprint(parsed_data)
with open("vacancies_2.json", "w", encoding= 'utf-8' ) as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)





