import sys

import lxml.etree as etree

parser = etree.XMLParser(strip_cdata=False)
filename = sys.argv[1]

with open(filename) as f:
    tree = etree.XML(f.read().encode(), parser=parser)

with open(filename, 'wb') as f:
    f.write(etree.tostring(tree, pretty_print=True))
