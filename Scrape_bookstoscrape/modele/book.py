class Book:
    """BLABLA"""

    '''def __init__(self):
        """BLABLA"""
        self.ident = 0
        self.product_page_url = "name"
        self.universal_product_code = "fname"
        self.title = "title"
        self.price_including_tax = "sex"
        self.price_excluding_tax = "rank"
        self.number_available = "a"
        self.product_description = "a"
        self.category = ""
        self.review_rating = ""
        self.image_name = ""
        self.image_url = ""'''

    def __init__(self):
        """BLABLA"""
    response = requests.get(url_book)
    if response.ok: 
        soup = bs(response.content, 'html.parser')
        self.ident = 0
        self.product_page_url = url_book
        self.universal_product_code = tds[0].text
        self.title = soup.find('h1').text
        self.price_including_tax = tds[2].text
        self.price_excluding_tax = tds[3].text
        self.number_available = tds[5].text
        self.product_description = ptag[3].text
        self.category = categorie[3].text
        self.review_rating = review2[1]
        self.image_name = url_book[36:-11]
        self.image_url = image_link[0]

    def get_book(self):
        """BLABLA"""
        self.ident = 0
        self.product_page_url = "name"
        self.universal_product_code = "fname"
        self.title = "title"
        self.price_including_tax = "sex"
        self.price_excluding_tax = "rank"
        self.number_available = "a"
        self.product_description = "a"
        self.image_url = ""

def scrape_page(url_book, information):
    """Request data from url book's page"""
    response = requests.get(url_book)
    if response.ok: 
        self.ident += 1
        soup = bs(response.content, 'html.parser')
        tds = soup.findAll('td')
        categorie = soup.findAll('a')
        ptag = soup.findAll('p')
        review = ptag[2]
        review2 = review['class']
        title = soup.find('h1').text
        image = soup.find('img')
        link = image['src']
        image_link = ['http://books.toscrape.com' + link[5:]]


        list_data = [url_book, tds[0].text, title,
        tds[2].text, tds[3].text, tds[5].text, ptag[3].text, 
        categorie[3].text, review2[1], url_book[36:-11], image_link[0]]
        datawriter = csv.writer(information)
        datawriter.writerow(list_data)

        
        self.product_page_url = url_book
        self.universal_product_code = tds[0].text
        self.title = soup.find('h1').text
        self.price_including_tax = tds[2].text
        self.price_excluding_tax = tds[3].text
        self.number_available = tds[5].text
        self.product_description = ptag[3].text
        self.category = categorie[3].text
        self.review_rating = review2[1]
        self.image_name = url_book[36:-11]
        self.image_url = image_link[0]

        '''img_data = requests.get(image_link[0]).content
        with open('../image_scrape/' + url_book[36:-11] 
        + '.jpg', 'wb') as download:
            download.write(img_data)'''