import csv
from matplotlib import pyplot as plt
from array import array

filename = "file2.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("q3_2.csv","w+")
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
# printing the field names 
# f.write('Field names are:' + ', '.join(field for field in fields)) 

tcp_flows=list()

#  printing rows 
# f.write('\nRows are:\n') 
for i in range(0,24):
	flows=set()	
	for row in rows:  
		for col in row[6:7]:
			s=col.split()
			if row[4]=='TCP':
				for t in row[1:2]:
					if (float(t)>=3600.0*i) and (float(t)<3600.0*(i+1)):
						for ip1 in row[2:3]:
							for ip2 in row[3:4]:
								flows.add((ip1,ip2,s[0],s[2]))
	tcp_flows.append(len(flows))					
for i in range(0,24):
	f.write("%i"%tcp_flows[i])
	f.write('\n')
f.write('\n')	
t=list()	
for i in range(0,24):
	t.append(i)
# for i in range(0,24):
# 	f.write("%10i"%t[i])
# 	f.write('\n')	
x=array("i",t)
y=array("i",tcp_flows)	
# for i in range(0,24):
# 	f.write("%10i"%x[i])
# 	f.write('\n')
# for i in range(0,24):
# 	f.write("%10i"%y[i])
# 	f.write('\n')	
plt.bar(x,y)
plt.ylabel('Number of connections')
plt.xlabel('Time of the day(hrs)')
plt.show()	
f.close()
