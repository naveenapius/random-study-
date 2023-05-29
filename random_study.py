import random
from csv import DictReader

#listing subjects with their priority on a scale of 1-5

f = open("subject.csv")
dict_reader = DictReader(f)
sub_dict = list(dict_reader)
f.close()

#parameters required for the extracting randomly generated list
subjects = []
priority = []

for i in sub_dict:
    subjects.append(i['subject'])
    priority.append(float(i['priority']))


daily_count = int(input("How many subjects do you want to study today?: ")) #number of subjects to be studied each day

#extracting list
today = random.choices(subjects,weights=priority, k=daily_count)

#output
print("\nThe wise men say you should study these: \n")
count = 0
for i in today:
    count +=1
    print(count,'. ',i)

print("\nMay we meet again.\n")
# end
