#!/bin/sh
for arg in "http://mirror.cs.umn.edu/debian/pool/main/t/tryton-server/*1.8*.deb" "http://mirror.cs.umn.edu/debian/pool/main/t/tryton-modules-account/*1.8*.deb" "http://mirror.cs.umn.edu/debian/pool/main/t/tryton-modules-party/tryton-modules-party_1.8.0-2_all.deb"
do
  /usr/bin/wget $arg
done
