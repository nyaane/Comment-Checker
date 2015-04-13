from bs4 import BeautifulSoup
import urllib2

history = urllib2.urlopen('http://www.reddit.com/user/kn0thing/comments/')
soup = BeautifulSoup(history)
html = history.read()

for link in soup.find_all(class='first'):
    print(link.get('href'))