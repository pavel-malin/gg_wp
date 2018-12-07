#!/usr/bin env python3.6
import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://weblancer.net/projects'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_page_count(html):
    soup = BeautifulSoup(html)
    paggination = soup.find('div', class_='pages_list text_box')
    return int(paggination.find_all('a')[-2].text)

def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_='items_list')
    projects = []

    for  row in  table.find_all('tr')[1:]:
        cols = row.find_all('td')
        projects.append({'title': cols[0].a.text,'cotegories': [category.text for category in cols[0].div.find_all('noindex')], 'price': cols[1].text.strip(), 'application': cols[2].text.strip().split()[0]
                         })

        return projects
def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Проект', 'категории', 'Цена', 'заявки'))

        for project in projects:
            writer.writerow((project['title'], ', '.join(project['categories']), project['application']))

    def main():
        page_count = get_page_count(get_html(BASE_URL))
        print('Все строиници %d' % page_count)
        projects = []
        for page in range(1, page_count):
            print('Парсинг %d%%' % (page / page_count * 100))
            projects.extend(parse(get_html(BASE_URL + '?page=%d' % page)))
            for project in projects:
                print(project)


                save(projects, 'projects.csv')
        if __name__ == '__main__':
            main()
