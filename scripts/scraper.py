from bs4 import BeautifulSoup
import requests


def search_subject(subject):
    source = requests.get('https://en.wikipedia.org/wiki/{}'.format(subject)).text
    soup = BeautifulSoup(source, 'lxml')
    full_article = soup.find('div', class_='mw-content-ltr')

    li = []
    for x in full_article.find_all('p'):
        li.append(x.text)

    listToStr = '\n'.join([str(elem) for elem in li])

    if len(listToStr) < 100:
        return None


    return listToStr


def list_categories(subject):
    source = requests.get('https://en.wikipedia.org/wiki/{}'.format(subject)).text
    soup = BeautifulSoup(source, 'lxml')
    toc = soup.find('div', class_='toc')

    print("\n----\nContents\n----\n")

    for ultag in toc.find_all('ul'):
        for litag in ultag.find_all('li'):
            print(litag.text)

    #div id="toc" class="toc" role="navigation"
    #return contents

























