import requests
import logging
import aiohttp
import asyncio
import time
import async_timeout

from pages.all_books_page import AllBookPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger=logging.getLogger('scraping')

logger.debug("Loading books list...")

page_cotent=requests.get("https://books.toscrape.com/").content;
page=AllBookPage(page_cotent)

books=page.book;
max_num=page.page_count

async def fetch_page(session,url):
 page_start=time.time()
 async with async_timeout.timeout(10):
  async with session.get(url) as response:
    print(f'page took {time.time()-page_start}')
    return await response.text()

async def get_multiple_pages(loop,*urls) :
 tasks=[]
 async with aiohttp.ClientSession(loop=loop) as session:
  for url in urls:
   tasks.append(fetch_page(session,url))
  grouped_tasks=asyncio.gather(*tasks)
  return await grouped_tasks
 
loop= asyncio.get_event_loop() 

urls=[f'https://books.toscrape.com/catalogue/page-{page_num}.html' for page_num in range(1,page.page_count)]
start=time.time()
pages=loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f"Total page requests took{time.time()-start}")

for page_content in pages:
 page=AllBookPage(page_content)
 books.extend(page.book)


 
 
