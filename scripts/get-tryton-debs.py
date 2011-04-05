#!/usr/bin/python
import optparse

parser = optparse.OptionParser(description='Grab the latest Tryton packages from Debian.')
parser.add_option('-m', "--mirror", dest="mirror", default="http://ftp.us.debian.org/debian/", help='specify a mirror other than ftp.us.debian.org')

(options, args) = parser.parse_args()
