import random

#listing subjects with their priority on a scale of 1-5
sub_dict = {'Subject 1' : 4, 
'Subject 2' : 2,  
'Subject 3' : 1,
'Subject 4' : 3 ,
'Subject 5' : 3 ,
'Subject 6' : 1, 
'Subject 7' : 2, 
'Subject 8' : 3, 
}

#parameters required for the extracting randomly generated list
subjects = list(sub_dict.keys())  #list of subjects
priority = list(sub_dict.values()) #list of scores
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
#end
