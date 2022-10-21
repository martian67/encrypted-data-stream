##TEXTDOCUMENT READ/WRITE##   
with open('cipher.txt','r') as f: #opens a text file from the directory
    lines = f.readlines() #reads lines to a string

#minor line edits
for j in range(len(lines)):
    lines[j] = lines[j].upper()
    lines[j] = lines[j][:-1]
    lines[j] = lines[j] + ">"

#build dictionary
sym_cphr = {}
#for i in range(lines):
#    for j in lines[i]:
#        sym_cphr.update(j)

#print(len(lines[1]))

z = len(lines[0])
for i in range(len(lines[0])):
    sym_cphr.update({lines[0][i]:lines[1][i]})

#open text input
with open('read_in.txt','r') as f: #opens a text file from the directory
    lines = f.readlines() #reads lines to a string

#write to text file
with open('readme_out.txt','w') as f: #opens a text file from the directory
    for line in lines: #convert to uppercase and replace '\n' from lines with '>'
        line = line.upper()
        line = line[:-1]
        line = line + ">"
        for t in line:
            f.writelines(sym_cphr[t]) #writes the line to the text file
