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