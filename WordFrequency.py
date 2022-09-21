import csv

infile = open('sometext.txt','r')

paragraphStr = infile.read()

    
count = 0

special_charac = ['“' ,'”' , ',' , '.' , '-' ] 

for i in special_charac:
    paragraphStr = paragraphStr.replace(i,'')

paragraphStr = paragraphStr.lower()
            
paragraph = paragraphStr.split()
words = paragraph

wordList = {}

#add words and counts to list
for i in range(len(words)):
    if words[i] in paragraph:
            wordList[words[i]]=  paragraph.count(words[i])
    i+=1

print(wordList)

infile.close()
