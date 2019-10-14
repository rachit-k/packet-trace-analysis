import csv 
filename = "file3.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
f= open("q4_3.csv","w+")
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
                    start_time.append(float(t))
            # elif s[3]=='[FIN]' or s[3]=='[RST]':
            #     for t in row[1:2]:
            #         x=start.index((row[2],row[3],s[0],s[2]))
            #         start.pop(x);
            #         duration.insert(float(t)-start_time[x])
            elif s[3]=='[FIN,': #or s[3]=='[RST,':
                for t in row[1:2]:
                    temp1=(row[2],row[3],s[0],s[2])
                    temp2=(row[3],row[2],s[2],s[0])
                    if temp1 in start:
                        x=start.index(temp1)
                        start.pop(x);
                        duration.append(float(t)-start_time[x]) 
                        start_time.pop(x)
                    if temp2 in start:
                        x=start.index(temp2)
                        start.pop(x);
                        duration.append(float(t)-start_time[x]) 
                        start_time.pop(x)
# for i in start_time:
#     f.write("%10f"%i)
#     f.write('\n')  
# for i in start:
#     f.write("%10s"%i[0])
#     f.write("%10s"%i[1])
#     f.write("%10s"%i[2])
#     f.write("%10s"%i[3])
#     f.write('\n')              

for i in duration:
    f.write("%10f"%i)
    f.write('\n') 
# f.write("%10i"%len(clients))
# f.write("%10i"%len(servers)) 
f.close()    