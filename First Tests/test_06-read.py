#!/usr/bin/env python

# filename = "DB_audiokitvehicles"
# with open(filename) as fn:
#     content = fn.readlines()
# print(content)

from xml.dom import minidom
filename = "DB_audiokitvehicles"
xmldoc = minidom.parse(filename)
itemlist = xmldoc.getElementsByTagName('audiokit')
# print(len(itemlist))
# print(itemlist[0].attributes['vehicleKey'].value)
# print(itemlist[0].attributes['sourcescriptval'].value)
for s in itemlist:
    print(s.attributes['vehicleKey'].value)
    print(s.attributes['sourcescriptval'].value)
