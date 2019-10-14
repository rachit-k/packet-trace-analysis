import csv 
import statistics
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
    # fields = csvreader.next() 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
# get total number of rows 
# f.write("Total no. of rows: %d"%(csvreader.line_num)) 
# f.write('\n')
# f.write('Field names are:' + ', '.join(field for field in fields)) 

t=0.0
tlist=list()
  
#  printing rows 
# f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:
    	s=col.split()
    	if len(s)>3:
            if s[3]=='[SYN]': #or s[3]=='[SYN,':
                for t1 in row[1:2]:
                    f.write("%10f"%(float(t1)-t))
                    f.write('\n')
                    tlist.append(float(t1)-t)
                    t=float(t1)

# f.write("mean %f"%statistics.mean(tlist))
# f.write('\n')
# f.write("median %f"%statistics.median(tlist))
f.close()    