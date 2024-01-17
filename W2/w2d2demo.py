#w2d2 demo file

import csv

total_records = 0

#create empty list for each field
fnames = []
lnames = []
favnumbers = []
favanimals = []

with open("W2/w2d2_demo.txt") as csvfile:
    #must indent when connected to and reading the file
    file = csv.reader(csvfile)

    for rec in file:
        print(rec)
        #append field data to the appropriate list
        fnames.append(rec[0])
        lnames.append(rec[1])
        favnumbers.append(int(rec[2]))
        #len() --> returns length of a structure (list)
        #the max length of rec is: 4
        if len(rec) == 4:
            favanimals.append(rec[3])
        else:
            
            favanimals.append('---')
            
#process fnames + favanimals list to display
for index in range(0, len(fnames)):
    print(f"{fnames[index]}'s fav animal is: {favanimals[index]}")





