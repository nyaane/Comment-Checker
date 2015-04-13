try:
    from bs4 import BeautifulSoup as BS
except:
    from BeautifulSoup import BeautifulSoup as BS

import urllib2

import config
import files

response = urllib2.urlopen(config.user_url.format(config.user))
html = response.read()
soup = BS(html)

links = [a["href"] for a in soup.findAll(attrs = {"class": "bylink"})]
print "We got {} links".format(len(links))

live = files.readLive()
print "We have {} live links.".format(len(live))

dead = files.readDead()
print "We have {} dead links.".format(len(dead))

deadened = 0
for a in live:
    if a not in links:
        dead.append(a)
        deadened += 1
print "We've deadened {} links.".format(deadened)
files.writeDead(dead)

added = 0
for a in links:
    if a not in live:
        live.append(a)
        added += 1
print "We've added {} links.".format(added)
files.writeLive(live)
