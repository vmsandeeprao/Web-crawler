from urllib2 import *
import re

regex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
tocrawl = set([sys.argv[1]])
crawled = set([])

while 1:
    crawling = tocrawl.pop()
    if '.mp3' in crawling or '.png' in crawling:
        crawled.add(crawling)
        continue
    if crawling in crawled:
        continue
    print 'crawling...' + crawling
    try:
        contents = urlopen(crawling)
    except:
        continue
    c = contents.read()
    crawled.add(crawling)

    links = regex.findall(c)
    for link in links:
        if link.startswith('http') and link not in crawled:
            tocrawl.add(link)
