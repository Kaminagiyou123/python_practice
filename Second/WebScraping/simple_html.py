from bs4 import BeautifulSoup

html_doc = """
<html>
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
</html>
"""
simple_soup = BeautifulSoup(html_doc, 'html.parser')

def find_title():
 print(simple_soup.find('h1').string)

def find_list_items():
 print([x.string for x in simple_soup.findAll('li')])

def find_subtitle():
 paragraph= simple_soup.find('p',{'class':'subtitle'})
 print(paragraph.string)

def find_other_paragraph():
 paragraphs=simple_soup.findAll('p') 
 
 other_paragraph=[p for p in paragraphs if 'subtitle' not in (p.attrs.get('class') or[])]
 print(other_paragraph[0].string)

find_other_paragraph()
