# -*- coding: utf-8 -*-
import re
file = open('.xml', "r")    
line = file.read()    
exp = re.compile(r'<.*?>')
text_only = exp.sub('',line).strip() #for all <*>, do replace as ''
print text_only
