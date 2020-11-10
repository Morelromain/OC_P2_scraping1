# -*-coding:Utf-8 -*
import os
import requests                
from bs4 import BeautifulSoup       

#create directory if they dont exist
def createdir():
    if not os.path.exists('../data_scrape'):
        os.makedirs('../data_scrape')
    if not os.path.exists('../image_scrape'):
        os.makedirs('../image_scrape')

#recuperate categorie's name and address
def list_cat(i,soup):
    info_categorie = soup.findAll('a')
    list_nom_categorie = info_categorie[i].text.strip()
    list_url_categorie2 = [] 
    for a in info_categorie :
        link = a['href']
        list_url_categorie2.append(link)
    return (list_nom_categorie,list_url_categorie2[i])
    
#find book on url page
def find_book(h3):
    a = h3.find('a')
    lien = a['href']
    lien2 = lien[8:]
    url_cat2 = "http://books.toscrape.com/catalogue" + lien2
    return (url_cat2)

#Request data from url book's page
def scrape_page(url_cat2,information):
    response = requests.get(url_cat2)
    if response.ok: 
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.content, 'html.parser')
        tds = soup.findAll('td')
        categorie = soup.findAll('a')
        description1 = soup.findAll('p')  
        description2 = description1[3].text.encode('utf-8').decode('utf-8').replace(';',',')
        titre = soup.find('h1').text.replace(':','').replace('/',',').replace('"','').replace('*','').replace('?','')
        image_link = []
        image = soup.find('img')
        link = image['src']
        image_link.append('http://books.toscrape.com'+link[5:]) 
        information.write(url_cat2+';'+tds[0].text+';'+titre+';'+tds[2].text+';'+tds[3].text+';'
+tds[5].text+';'+description2+';'+categorie[3].text+';'+tds[6].text+';'+image_link[0]+';\n')

        img_data = requests.get(image_link[0]).content
        with open('../image_scrape/'+titre+'.jpg', 'wb') as download:
            download.write(img_data)