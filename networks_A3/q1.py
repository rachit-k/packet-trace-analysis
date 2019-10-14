import csv 
filename = "file3.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("temp.txt","w+")
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
f.write("Total no. of rows: %d"%(csvreader.line_num)) 
f.write('\n')
# printing the field names 
f.write('Field names are:' + ', '.join(field for field in fields)) 

clients=set()
servers=set()
  
#  printing rows 
f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:	
    	# f.write("%10s"%col),
    	s=col.split()
    	if len(s)>3:
    		# f.write("%10s"%s[3])
    		# f.write('\n')
    		if s[3]=='[SYN]': #or s[3]=='[SYN,':
    			for ip1 in row[2:3]:
    				clients.add(ip1)
    				# f.write("%10s"%ip1)
    			for ip2 in row[3:4]:
    				servers.add(ip2)
    				# f.write("%10s"%ip2)

    # f.write('\n') 
f.write("%10i"%len(clients))
f.write("%10i"%len(servers)) 
f.close()    