import csv 
import statistics
filename = "file3.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("q7_3.csv","w+")
#f= open("temp.txt","w+")
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    #fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 


t=0.0
tlist=list()
start=list()
#  printing rows 
# f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:
        s=col.split()
        if len(s)>3:
            if s[3]=='[SYN]' or (s[3]=='[SYN,' and s[4]=='ECN,'):
                start.append((row[2],row[3],s[0],s[2]))
            temp1=(row[2],row[3],s[0],s[2])
            if temp1 in start:
                for t1 in row[1:2]:
                    tlist.append(float(t1)-t)
                    t=float(t1)

            if s[3]=='[FIN,': #or s[3]=='[RST,':
                for t1 in row[1:2]:
                    temp1=(row[2],row[3],s[0],s[2])
                    temp2=(row[3],row[2],s[2],s[0])
                    if temp1 in start:
                        x=start.index(temp1)
                        start.pop(x);
                    if temp2 in start:
                        x=start.index(temp2)
                        start.pop(x);                
                 

# f.write("mean %f"%statistics.mean(tlist))
# f.write('\n')
# f.write("median %f"%statistics.median(tlist))    
for tt in tlist:
    f.write("%f"%tt)
    f.write('\n')                

f.close()    