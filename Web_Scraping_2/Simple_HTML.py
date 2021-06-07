from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup=BeautifulSoup(SIMPLE_HTML,'html.parser')

def find_title(tag):
 h1_tag=simple_soup.find(tag)
 print(h1_tag.string)
 
def find_list_items(tag):
 list_items=simple_soup.find_all(tag)
 list_contents=[x.string for x in list_items]
 return list_contents

def find_subtitle(tag,type,name):
 paragrah=simple_soup.find(tag,{type:name})
 return paragrah.string

def find_other_paragrah():
 ps=simple_soup.find_all("p");
 
 find_other_paragrah=[p for p in ps if "subtitle" not in p.attrs.get('class',[])]
 print(find_other_paragrah[0].string)

# find_title("h1")
# print(find_list_items('li'))
# print(find_subtitle('p',"class","subtitle"))

find_other_paragrah()

