
#jayden fagre
#1/24/24
#lab3b
#prompt: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

import csv

#-------------variable dictionary----------------#
total_records = 0 #total number of records processed
cant_register = 0 #number of people who cant register
canbutwontreg = 0 #number of people who can vote but didnt register
regbutdidntvote = 0 #number of people who registered but didnt vote
voted_count = 0 #number of people who voted
#id_num = id number of voter
#age = age of voter
#reg = is the voter registered
#voted = did the voter vote
#------------------------------------------------#

with open ('W3/lab3b homework lab/voters_202040.csv') as csvfile:
    file = csv.reader(csvfile)

    #assigning recs to variables
    for rec in file:
        id_num = rec[0]
        age = int(rec[1])
        reg = rec[2]
        voted = rec[3]
    #--------------------------#

        #sort data into lists
        id_num_list = []
        age_list = []
        reg_list = []
        voted_list = []
        id_num_list.append(id_num)
        age_list.append(age)
        reg_list.append(reg)
        voted_list.append(voted)

        for i in range(len(id_num_list)):
            id_num = id_num_list[i]
            age = age_list[i]
            reg = reg_list[i]
            voted = voted_list[i]
        #--------------------#

        #determine totals
        if age < 18:
            cant_register += 1
        
        if reg == "N" and age >= 18:
            canbutwontreg += 1
        
        if reg == "Y" and voted == "N" and age >= 18:
            regbutdidntvote += 1

        if reg == "Y" and voted == "Y" and age >= 18:
            voted_count += 1
        
        total_records += 1
        #----------------#

#final output msgs
print('\n')
print("Number of individuals not eligable to register: ", cant_register)
print("Number of individuals who are old enough to vote but have not registered: ", canbutwontreg)
print("Number of individuals who are eligable to vote but did not: ", regbutdidntvote)
print("Number of individuals who did vote: ", voted_count)
print("Number of records processed: ", total_records)
print('\n')
#-----------------#

            
    
