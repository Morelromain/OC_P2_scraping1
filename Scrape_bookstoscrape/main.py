"""main script of Scrape_booktoscrape"""

import csv
import requests
from bs4 import BeautifulSoup as bs

from . import fscrape as fs


# get data of homepage
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)

# create data's directory and categorie's number
if response.ok:
    print("Scraping site bookstoscrape en cour :")
    fs.createdir()
    soup = bs(response.content, 'html.parser')
    cat_column = soup.findAll('ul')
    cat_list = cat_column[2].findAll('a')
    print('Nombres de categorie : ', len(cat_list))

    # recuperate all categorie's name and address
    nb = 0
    while nb < len(cat_list):
        nom_categorie, url_categorie = fs.list_cat(nb, cat_list)
        nb += 1

        # create file.csv of all categorie
        with open(
            '../data_scrape/' + nom_categorie + '.csv',
                'w', encoding='utf-8', newline=''
                ) as information:
            list_title = [
                "product_page_url", "universal_product_code",
                "title", "price_including_tax", "price_excluding_tax",
                "number_available", "product_description", "category",
                "review_rating", "image_name", "image_url"
                ]
            datawriter = csv.writer(information)
            datawriter.writerow(list_title)

            # Request data from url book's categorie
            i = 1
            while response.ok:
                if i == 1:
                    url_cat = 'http://books.toscrape.com/catalogue/' \
                        + url_categorie[:-11] + '/index.html'
                else:
                    url_cat = 'http://books.toscrape.com/catalogue/' \
                        + url_categorie[:-11] + '/page-' + str(i) + '.html'
                response2 = requests.get(url_cat)

                if response2.ok:
                    print("Scraping de", nom_categorie, " : page", i)
                    soup2 = bs(response2.content, 'html.parser')
                    books = soup2.findAll('article')

                    # Request data from url book's
                    for h3 in books:
                        url_book = fs.find_book(h3)
                        fs.scrape_page(url_book, information)
                i += 1
else:
    print("Site injoignable :")
