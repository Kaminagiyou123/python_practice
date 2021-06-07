import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''
soup=BeautifulSoup(ITEM_HTML,'html.parser')

def find_item_name():
 locator='article.product_pod h3 a'
 item_link=soup.select_one(locator)
 item_name=item_link.attrs["title"]
 print(item_name)
 
def find_product_link():
 locator='article.product_pod h3 a'
 item_link=soup.select_one(locator).attrs['href']
 print(item_link)
 
def find_tag(c):
 ps=soup.find_all("p");
 tag_p= [p for p in ps if c in p.attrs.get('class',[])]
 print (tag_p)
 
def find_price():
 locator='article.product_pod div.product_price p.price_color'
 price=soup.select_one(locator).string
 expression="£([0-9]+\.[0-9])"
 matches=re.search(expression,price)
 print(float(matches[1]))
 
def find_item_rating():
  locator='article.product_pod p.star-rating'
  rating_tag=soup.select_one(locator).attrs['class']
  rating=[x for x in rating_tag if x!='star-rating'][0]
  print(rating)
 
# find_item_name()
# find_product_link()
# find_price()
# find_item_rating()
