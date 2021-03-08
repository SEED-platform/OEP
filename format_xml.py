import sys

import lxml.etree as etree

filename = sys.argv[1]
tree = etree.parse(filename)
with open(filename, 'wb') as f:
    f.write(etree.tostring(tree, pretty_print=True))
