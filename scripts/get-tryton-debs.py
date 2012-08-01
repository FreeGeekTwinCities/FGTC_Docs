#!/usr/bin/python
import optparse
from urllib import urlopen, urlretrieve
from HTMLParser import HTMLParser

debug=False

parser = optparse.OptionParser(description='Grab the latest Tryton packages from Debian.')
parser.add_option('-m', "--mirror", dest="mirror", default="http://ftp.us.debian.org/debian/", help='specify a mirror other than ftp.us.debian.org')
parser.add_option('-t', "--tryton-version", dest="tryton_version", default="2.0", help='specify a Tryton version other than 2.0')

(options, args) = parser.parse_args()

base_url = options.mirror + "/pool/main/t"
tryton_dirs=[]
tryton_debs=[]
wget_file = open("wget-tryton-debs", "w")

class DirParser(HTMLParser):
    def __init__(self, url): 
        HTMLParser.__init__(self)
        req = urlopen(url) 
        self.feed(req.read())
        
    def handle_starttag(self, tag, attrs): 
        if tag == 'a' and attrs: 
            link = attrs[0][1]
            if link.find("tryton") >= 0:
                tryton_dirs.append(link)

class FileParser(HTMLParser):
    def __init__(self, url): 
        HTMLParser.__init__(self)
        req = urlopen(url) 
        self.feed(req.read())
        
    def handle_starttag(self, tag, attrs): 
        if tag == 'a' and attrs: 
            link = attrs[0][1]
            if (link.find(options.tryton_version) >= 0) and (link.rfind(".deb") == (len(link)-4)):
                print "Found package %s, downloading..." % link
                fileurl = fullurl + link
                wget_file.write(fileurl + "\n")
                urlretrieve(fileurl, link)

DirParser(base_url)

for d in tryton_dirs:
    fullurl = base_url + "/" + d
    if debug: print "Found directory %s, scanning for Tryton %s packages..." % (fullurl, options.tryton_version)
    FileParser(fullurl)
