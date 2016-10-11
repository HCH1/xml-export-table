xmlformat ch3_3Glossary_of_DR.xml > ch33;
xmlformat ch3_4RX.xml > ch34;
xmlformat ch2_4BEOL.xml > ch24; #format 1st
xmlformat ch99_1.xml > ch991;
python demo_xmlSplitV3.py > ch34_noBKT; #then remove <*>
sed '/\ $/d' ch34_noBKT > ch34_noBKT_noSpc; #remove dummy lines
#egrep -v '\ $' ch34_noBKT > ch34_noBKT_noSpcV2; #remove dummy lines