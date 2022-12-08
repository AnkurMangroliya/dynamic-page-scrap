from requests_html import HTMLSession
import requests
import pandas as pd




url ='https://www.beerwulf.com/en-gb/c/beer-kegs/sub-kegs'

s = HTMLSession()
r = s.get(url)

r.html.render(timeout=40)

beerlist=[]
# print(r.status_code)
products = r.html.xpath('/html/body/div[1]/div[4]/div/div/div[2]',first=True)

for item in products.absolute_links:
    r = s.get(item)
    try:
        name = r.html.find('div.product-detail-info-title',first=True).text
        price = r.html.find('span.price',first=True).text
    except:
        name='None'
        price='None'
    # subtext = r.html.find('div.product-subtitle',first=True).text



    if r.html.find('div.add-to-cart-container'):
        stock = 'in stock'
    else:
        stock = 'Out of stock'

    beer={
        'name':name,
        'price':price,
        'stock':stock
    }

    beerlist.append(beer)

df = pd.DataFrame(beerlist)
print(df)

dfv = df.to_csv('beer_data.csv')