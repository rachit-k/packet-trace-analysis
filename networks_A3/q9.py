import csv 
import re
filename = "file2.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("temp.txt","w+")
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 

    for row in csvreader: 
        rows.append(row) 
  
# get total number of rows 
f.write("Total no. of rows: %d"%(csvreader.line_num)) 
f.write('\n')
# printing the field names 
f.write('Field names are:' + ', '.join(field for field in fields)) 

tup=("128.3.28.48","207.190.63.72","21","33527")
tup1=(tup[1],tup[0],tup[3],tup[2])
time1=list()
seq_nos=list()
time2=list()
ack_nos=list()
  
#  printing rows 
f.write('\nRows are:\n') 
for row in rows:  
    for col in row[6:7]:
        s=col.split()
        if len(s)>4:
            temp=(row[2],row[3],s[0],s[2])
            if temp==tup:
                for s1 in s:
                    if re.search("^Ack=",s1):
                        ack_nos.append(s1[4:])
                for t in row[1:2]:
                    time2.append(float(t))
            if temp==tup1:
                for s1 in s:
                    if re.search("^Seq=",s1):
                        seq_nos.append(s1[4:])
                for t in row[1:2]:
                    time1.append(float(t)) 
f1= open("q9_2_1.csv","w+")
f2= open("q9_2_2.csv","w+")
f3= open("q9_2_3.csv","w+")
f4= open("q9_2_4.csv","w+")
for i in seq_nos:
    f1.write("%10s"%i)
    f1.write('\n') 

for i in time1:
    f2.write("%10f"%i)
    f2.write('\n')    

for i in ack_nos:
    f3.write("%10s"%i)
    f3.write('\n')

for i in time2:
    f4.write("%10f"%i)
    f4.write('\n')

f.close()    