# -*-coding:Utf-8 -*
import os
import csv
import requests                
from bs4 import BeautifulSoup       

def createdir():
    """create directory if they dont exist"""
    if not os.path.exists('../data_scrape'):
        os.makedirs('../data_scrape')
    if not os.path.exists('../image_scrape'):
        os.makedirs('../image_scrape')

def list_cat(nb, cat_list):
    """recuperate categorie's name and address"""
    list_nom_categorie = cat_list[nb].text.strip()
    list_url_categorie = [] 
    for a in cat_list :
        link = a['href']
        list_url_categorie.append(link)
    return (list_nom_categorie, list_url_categorie[nb])

def find_book(h3):
    """find book on url page"""
    a = h3.find('a')
    link = a['href']
    link2 = link[8:]
    url_cat2 = "http://books.toscrape.com/catalogue" + link2
    return (url_cat2)

def scrape_page(url_book, information):
    """Request data from url book's page"""
    response = requests.get(url_book)
    if response.ok: 
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.content, 'html.parser')
        tds = soup.findAll('td')
        categorie = soup.findAll('a')
        ptag = soup.findAll('p')  
        review = ptag[2]
        review2 = review['class']
        title = soup.find('h1').text
        image = soup.find('img')
        link = image['src']
        image_link = []
        image_link.append('http://books.toscrape.com' + link[5:]) 
        
        list_data = [url_book, tds[0].text, title,
        tds[2].text, tds[3].text, tds[5].text, ptag[3].text, 
        categorie[3].text, review2[1], image_link[0]]
        datawriter = csv.writer(information)
        datawriter.writerow(list_data)

        img_data = requests.get(image_link[0]).content
        with open('../image_scrape/' + url_book[36:-11] 
        + '.jpg', 'wb') as download:
            download.write(img_data)