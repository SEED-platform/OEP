import sys

import lxml.etree as etree

parser = etree.XMLParser(strip_cdata=False, remove_blank_text=True)
filename = sys.argv[1]

with open(filename) as f:
    tree = etree.XML(f.read().encode(), parser=parser)

# # for some reason, the first round of tostring isn't perfect formatting, so do it twice
# tree_str = etree.tostring(tree)
# tree2 = etree.XML(tree_str.decode(), parser=parser)
with open(filename, 'wb') as f:
    f.write(etree.tostring(tree, pretty_print=True))
