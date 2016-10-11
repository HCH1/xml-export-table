import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/hhung/2015-6 work/demo0913testXML/country_data.xml')
root = tree.getroot()

f = open("o1.txt", "w")
print >> f, tree
f.close()

#for ruleValue in root.iter('ruleValue'):
#   print ruleValue.attrib
