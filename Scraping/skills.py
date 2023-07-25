import requests
import bs4
import fake_headers
from pprint import pprint

def skills_required(link):
    headers = fake_headers.Headers(browser="firefox", os="win")
    headers_dict = headers.generate()

    response = requests.get(link, headers=headers_dict)
    vacancy_data = response.text
    vacancy_html = bs4.BeautifulSoup(vacancy_data, "lxml")

    # skills_tag = vacancy_html.find('div', class_="bloko-tag-list")
    skill_tags = vacancy_html.find_all("div", class_="bloko-tag bloko-tag_inline")
    skills_list = []
    for skill_tag in skill_tags:
        skill = skill_tag.find('span').text
        skills_list.append(skill)

    return skills_list

# pprint(skills_required("https://spb.hh.ru/vacancy/82888245?from=vacancy_search_list&query=python"))