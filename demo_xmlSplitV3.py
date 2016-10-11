# -*- coding: utf-8 -*-
import re
file = open('/Users/HCHung/Documents/2016demo/0912testXML/ch34', "r")    
line = file.read()    
exp = re.compile(r'<.*?>')
text_only = exp.sub('',line).strip() #for all <*>, do replace as ''
print text_only