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

else:
    print (f"\nWe did not find {search_name} in the file\n")
    print (f"Please Try again. ")