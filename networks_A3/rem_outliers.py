import csv 
import statistics

filename = "q5_31.csv"
filename2="q4_3.csv"

f= open("q5_31_2.csv","w+")
f2=open("q4_3_12.csv","w+")

rows = [] 
nos=list()
nos1=list()
f_list=list()
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)
rows1=[]
with open(filename2, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows1.append(row)        

for row in rows:
	for col in row:
		nos.append(float(col))

for row in rows1:
	for col in row:
		nos1.append(float(col))
for no in nos:
	i=nos.index(no)
	f_list.append(no/nos1[i])

m=statistics.mean(f_list)
d=statistics.stdev(f_list)
# f.write("mean %f"%statistics.mean(nos))
# f.write('\n')
# f.write("median %f"%statistics.median(nos))
# f.write('\n')
# f.write("standard dev %f"%statistics.stdev(nos))

for temp in f_list:
	if temp<m+2*d and temp>m-2*d :
		i=f_list.index(temp)
		f.write("%f"%nos[i])
		f.write('\n')
		f2.write("%s"%nos1[i])
		f2.write('\n')

# for no in nos:
# 	if no<m+2*d and no>m-2*d :
# 		f.write("%f"%no)
# 		f.write('\n')
# 		i=nos.index(no)
# 		f2.write("%s"%nos1[i])
# 		f2.write('\n')

f.close()	