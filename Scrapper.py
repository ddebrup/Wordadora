import urllib.request as urllib2
from bs4 import BeautifulSoup
import re

Newlines = re.compile(r'[\r\n]\s+')

def getPageText(url):
    # given a url, get page content
    data = urllib2.urlopen(url).read()
    # parse as html structured document
    bs = BeautifulSoup(data)
    # kill javascript content
    for s in bs.findAll('script'):
        s.replaceWith('')
    # find body and extract text
    txt = bs.find('body').getText('\n')
    # remove multiple linebreaks and whitespace
    return Newlines.sub('\n', txt)

def main():
    urls = [
        'http://www.stackoverflow.com/questions/5331266/python-easiest-way-to-scrape-text-from-list-of-urls-using-beautifulsoup',
        'http://stackoverflow.com/questions/5330248/how-to-rewrite-a-recursive-function-to-use-a-loop-instead',
        'https://www.geeksforgeeks.org/programming-language-choose/'
    ]
    txt = [getPageText(url) for url in urls]

if __name__=="__main__":
    main()
