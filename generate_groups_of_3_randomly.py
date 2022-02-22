import random
import  csv 
import pandas as pd
group=1
membersInGroup=3
df = pd.read_csv("class_list.csv") #you can define if there is a header or not in the file
participants= df.values.tolist()


# with open('class_list.csv', 'r') as csvfile:
#   data = csv.reader(csvfile)
#   participants = list(data)
# participants=["Mugoya Dihfahsih", "Musa Rahim", "David Tugume", "Robert Masajjage", "Fahad Guma", "Henry Mugume","Denis Mbabazi", "Florence Nanteza", "Mwanje Felix", "Gerald Masaba" ,"Isaac King Nsengiyunva"]
print(participants)
for participant in participants[:]:               
    if membersInGroup==3:
        print("Group {} consists of;".format(group))
        membersInGroup=0
        group+=1
    person=random.choice(participants)
    print(person)
    membersInGroup+=1
    participants.append(str(person))