import csv 

# class packet:
#     def __init__(self, no, time, source, dest, protocol, length, info):
#     self.no = no
#     self.time = time
#     self.source = source
#     self.dest = dest
#     self.protocol = protocol
#     self.length = length
#     self.info = info
    
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

tcp_flows=set()
  
#  printing rows 
f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:	
    	# f.write("%10s"%col),
    	s=col.split()
    	if row[4]=='TCP':
            for ip1 in row[2:3]:
                for ip2 in row[3:4]:
	               tcp_flows.add((ip1,ip2,s[0],s[2]))

# f.write("%10s"%tcp_flows)
# f.write('\n') 
f.write("%10i"%len(tcp_flows))
f.close()     