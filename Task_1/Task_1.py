import json
import csv

filepath='/content/drive/MyDrive/Task_1/'
with open(filepath+'Copy of data.json') as file:
  data = json.loads("[" + 
  file.read().replace("}\n{", "},\n{") + 
    "]")

all_keys=['a','t','e','liid','linkedin','n']
for individual_data in data:
  for key in all_keys:
    if(key not in individual_data):
      individual_data[key]="NULL"



#data_main.csv
# path loading
path='/content/drive/MyDrive/Task_1/'

#creating file and writeable object of file
data_main=open(path+'data_main.csv','w')
writer=csv.writer(data_main)

#this counter is used to count for the first row
count=0

#writing data in file
for user in data:
  if(count==0):
    writer.writerow(all_keys)
    count+=1
  else:
    row=[]
    for key in all_keys:
      row.append(user[key])
    writer.writerow(row)

#Closing The file
data_main.close()





#data_number.csv
# path loading
path='/content/drive/MyDrive/Task_1/'
num_keys=['liid','t']

#creating file and writeable object of file
data_number=open(path+'data_number.csv','w') 
num_writer=csv.writer(data_number)

#this counter is used to count for the first row
c=0

#writing data in file
for users in data:
  if(c==0):
    num_writer.writerow(num_keys)
    c+=1

  elif(c!=0 and users['t']!="NULL"):#check for non-NULL values
    row=[]
    for key in num_keys:
      if(key=='t'):
        row.append(users[key][0])
      else:
        row.append(users[key])
    num_writer.writerow(row)



#Closing The file
data_number.close()


#data_email.csv

# path loading
path='/content/drive/MyDrive/Task_1/'
mail_keys=['liid','e']

#creating file and writeable object of file
data_email=open(path+'data_email.csv','w')
mail_writer=csv.writer(data_email)

#this counter is used to count for the first row
e_c=0

#writing data in file
for user in data:
  if(e_c==0):
    mail_writer.writerow(mail_keys)
    e_c+=1

  elif(e_c!=0 and user['e']!="NULL"):#check for non-NULL values
    row=[]
    for key in mail_keys:
      if(key=='e'):
        row.append(user[key][0])
      else:
        row.append(user[key])
    mail_writer.writerow(row)


#Closing The file
data_email.close()
