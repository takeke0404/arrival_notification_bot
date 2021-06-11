from selenium import webdriver
import os
import time
import re
from selenium.webdriver.chrome.options import Options

dir = os.path.dirname(os.path.abspath(__file__))

def gethtml(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(dir+"\\chromedriver",options=options)
    driver.get(url)
    time.sleep(10)
    source = driver.page_source
    driver.quit()
    return source

urlList=[]
with open(dir+"\\検索先url.txt") as f:
    urlList=f.readlines()

keywords=[]
with open(dir+"\\検索word.txt") as fa:
    keywords=fa.readlines()

for url in urlList:
    url=url.strip()
    str = re.sub('<style\stype="text/css">(.|\s)*?</style>','',gethtml(url))
    html = re.sub('<[^<>]+>',',',str)
    words = html.split(',')
    for word in words:
        for keyword in keywords:
            keyword=keyword.strip()
            if keyword in word:
                url2=url
                word2=re.sub("\(","\\\(",word)
                word2=re.sub("\)","\\\)",word2)
                word2=re.sub("\s","\\s",word2)
                word2=re.sub("\.","\\\.",word2)
                pattern=re.compile('<a[^<>]+>%s</a>' % word2)
                mo=re.search(pattern,str)
                if mo:
                    a=mo.group()
                    pattern=re.compile('href="(?P<url>[^\"]+)"')
                    mo2=re.search(pattern,a)
                    url2=mo2.group('url')
                print(word+":"+url2)
