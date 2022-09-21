import csv

infile = open('info_security.txt','r')
outfile = open('encrypted.txt','w')


codes = {'A':'!', 'B':'@', 'C':'#', 'D':'$', 'E':'%','F':'^', 'G':'&', 'H':'*', 'I':'(', 'J':')', 'K':'-', 'L':'_', 'M':'=', 'N':'+', 'O':'{','P':'}', 'Q':'/', 'R':'?', 'S':'<', 'T':'>', 'U':'~', 'V':'`', 'W':'|', 'X':',', 'Y':'.','Z':'"', 'a':'9', 'b':'8', 'c':'7', 'd':'6', 'e':'5','f':'4', 'g':'3', 'h':'2', 'i':'1', 'j':'0', 'k':'"', 'l':"'", 'm':':', 'n':';', 'o':'s','p':'f', 'q':'h', 'r':'v', 's':'O', 't':'p', 'u':'g', 'v':'a', 'w':'H', 'x':'E', 'y':'U','z':'C'}

paragraphStr = infile.read()

    
count = 0

special_charac = ['“' ,'”' , ',' , '.' , '-',':' ] 

for i in special_charac:
    paragraphStr = paragraphStr.replace(i,'')

            
paragraph = paragraphStr.split()


for i in paragraph:
    letter = [x for x in i]
    for x in letter:
        outfile.write(codes[x])
    outfile.write(' ')



outfile.close()