from bs4 import BeautifulSoup, element
import requests



def search_subject(subject):
    source = requests.get('https://en.wikipedia.org/wiki/{}'.format(subject)).text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('div', class_='mw-content-ltr').text
    return article





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



















