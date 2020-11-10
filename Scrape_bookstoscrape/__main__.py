# -*-coding:Utf-8 -*

import requests
from bs4 import BeautifulSoup

import fscrape as fs


#get data of homepage
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    fs.createdir()

    #recuperate all categorie's name and address
    for i in range(3, 53):
        nom_categorie,url_categorie = fs.list_cat(i,soup)
        
        #create file.csv of all categorie
        with open('../data_scrape/'+nom_categorie+'.csv', 'w', encoding='utf-8') as information:
            information.write('product_page_url; universal_product_code(upc); title; price_including_tax;\
            price_excluding_tax; number_available; product_description; category; review_rating; image_url;\n')
            
            #Request data from url book's categorie                                                                                          
            url_cat = 'http://books.toscrape.com/catalogue/'+url_categorie[:-11]+'/index.html' 
            response2 = requests.get(url_cat)                                                                    
            print (url_cat)
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
                        #3-53