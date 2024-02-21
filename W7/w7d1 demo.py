# Comparing Searching Methods Demo

# Covers: 


import csv
exit()
# functions







# main






# empty lists 
id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open ("W7\w7_demoFile.txt") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

# check file 
# for i in range (len(id_stud)):
#     print (id_stud[i], lname[i], fname[i])
        
# SEQUENTIAL SEARCH
search_name = input("Enter the name you are looking for: ")
found = []

for i in range (len(fname)):
    if search_name.lower() == fname[i].lower():

        # store found names location
        found.append(i)

if len(found) > 0:
    print (f"\n We found {search_name} at index position {found[0]}")
    print (f"\tHere is there info: ")

    for i in range (len(found)):
        print (f"\t\t{fname[i]} \t {lname[i]} \t {id_stud[i]} \t {class1[i]} \t {class2[i]} \t {class3[i]}\n")
        # print (f"\t\t{fname[found]} \t {lname[found]} \t {id_stud[found]} \t {class1[found]} \t {class2[found]} \t {class3[found]}\n")
else: 
    print (f"\nWe did not find {search_name} in the file\n")
    print (f"Please Try again. ")

# BINARY SEARCH
search_name = input("Enter the name you are looking for: ")

min = lname[0]
max = lname[len(lname)-1]
# mid = int((0 + len(lname) -1 ) / 2)
mid = int((min + max) / 2)
bin_count = 0

while (min < max and search_name != lname[mid]):
    bin_count += 1
    if search_name < lname[mid]:
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search_name == lname[mid]:
    print (f"\nWe found {search_name} at index position {mid}")
    print (f"\tHere is there info: ")
    print (f"\t\t{fname[mid]} \t {lname[mid]} \t {id_stud[mid]} \t {class1[mid]} \t {class2[mid]} \t {class3[mid]}\n")

       
        


