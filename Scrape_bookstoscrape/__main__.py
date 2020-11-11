# -*-coding:Utf-8 -*

import requests
from bs4 import BeautifulSoup

import fscrape as fs

#get data of homepage
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)

#create data's directory and categorie's number
if response.ok:
    print ("Scraping site bookstoscrape en cour :")
    fs.createdir()
    soup = BeautifulSoup(response.content, 'html.parser')
    cat_column = soup.findAll('ul')
    cat_list = cat_column[2].findAll('a')
    print ('Nombres de categorie : ',len(cat_list))

    #recuperate all categorie's name and address
    nb=0
    while nb < len(cat_list):
        nom_categorie,url_categorie = fs.list_cat(nb,cat_list)
        nb += 1

        #create file.csv of all categorie
        with open('../data_scrape/'+nom_categorie+'.csv', 'w', encoding='utf-8') as information:
            information.write('product_page_url; universal_product_code(upc); title; price_including_tax;\
            price_excluding_tax; number_available; product_description; category; review_rating; image_url;\n')
            
            #Request data from url book's categorie                                                                                          
            url_cat = 'http://books.toscrape.com/catalogue/'+url_categorie[:-11]+'/index.html' 
            response2 = requests.get(url_cat)                                                                    
            print ("Scraping de",nom_categorie)

            if response2.ok:
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                livre = soup2.findAll('article')                       
                    
                for h3 in livre:
                    url_cat2 = fs.find_book(h3)
                    fs.scrape_page(url_cat2,information)
                    
            i = 2
            while response2.ok:                                                                                      
                url_cat = 'http://books.toscrape.com/catalogue/'+url_categorie[:-11]+'/page-'+str(i)+'.html' 
                response2 = requests.get(url_cat)                                                                    
                i += 1
                                
                if response2.ok:
                    soup2 = BeautifulSoup(response2.content, 'html.parser')
                    livre = soup2.findAll('article')                       
                        
                    for h3 in livre:
                        url_cat2 = fs.find_book(h3)
                        fs.scrape_page(url_cat2,information)
                        