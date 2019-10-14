import csv 
filename = "file3.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("q5_32.csv","w+")
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
# get total number of rows 
# f.write("Total no. of rows: %d"%(csvreader.line_num)) 
# f.write('\n')
# # printing the field names 
# f.write('Field names are:' + ', '.join(field for field in fields)) 

start=list()
start_time=list()
duration=list()
length_stc=list()
length_cts=list()
final_length_stc=list()
final_length_cts=list()

#  printing rows 
# f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:    
        # f.write("%10s"%col),
        s=col.split()
        if len(s)>3:
            if s[3]=='[SYN]' or (s[3]=='[SYN,' and s[4]=='ECN,'):
                for t in row[1:2]:
                    start.append((row[2],row[3],s[0],s[2]))
                    length_cts.append(int(0))
                    length_stc.append(int(0))
            temp1=(row[2],row[3],s[0],s[2])
            temp2=(row[3],row[2],s[2],s[0])
            for l in row[5:6]:
                if temp1 in start:
                    i=start.index(temp1)
                    length_cts[i]=length_cts[i]+int(l)
                if temp2 in start:
                    i=start.index(temp2)
                    length_stc[i]=length_stc[i]+int(l)
            if s[3]=='[FIN,': #or s[3]=='[RST,':
                for t in row[1:2]:
                    temp1=(row[2],row[3],s[0],s[2])
                    temp2=(row[3],row[2],s[2],s[0])
                    if temp1 in start:
                        x=start.index(temp1)
                        start.pop(x);
                        final_length_cts.append(length_cts[x])
                        length_cts.pop(x)
                        final_length_stc.append(length_stc[x])
                        length_stc.pop(x)
                    if temp2 in start:
                        x=start.index(temp2)
                        start.pop(x);
                        final_length_cts.append(length_cts[x])
                        length_cts.pop(x)
                        final_length_stc.append(length_stc[x])
                        length_stc.pop(x)                             
        
# for i in final_length_stc:
#     f.write("%f"%i)
#     f.write('\n') 

for i in final_length_cts:
    f.write("%10f"%i)
    f.write('\n')     

f.close()    