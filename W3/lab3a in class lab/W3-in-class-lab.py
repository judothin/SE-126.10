#Jayden Fagre
#1/23/24
#prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

import csv

#-------------variable dictionary----------------#
total_records = 0 #total number of records processed
drcost = 0 #cost to replace  all desktops
lrcost = 0 #cost to replace all laptops
drcount = 0 #number of desktops to be replaced
lrcount = 0 #number of laptops to be replaced
ryear = 16  #replace computers older than this
cpdesktop = 2000  #cost to replace a desktop
cplaptop = 1500  #cost to replace a laptop
#comp_type = type of computer
#manufacturer = manufacturer of computer
#processor = processor of computer
#ram = amount of ram in computer
#hdd_1 = size of first hard drive
#num_hdd = number of hard drives
#hdd_2 = size of second hard drive
#os = operating system
#year = year computer was built
#------------------------------------------------#

#idk if this is needed but i added it when i was trying to figure out why it wasnt working
comp_type = []
manufacturer = []
processor = []
ram = []
hdd_1 = []
num_hdd = []
hdd_2 = []
os = []
year = []
comp_type_list = []
manufacturer_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []


import csv

with open ('W3\lab3a.csv') as csvfile:
    file = csv.reader(csvfile)

    #labels
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Type", "Man", "Proc", "RAM", "HDD1", "HDD_NUM", "HDD2", "OS", "Year"))

    #assigning recs to variables
    for rec in file:

        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            comp_type = "ERROR"

        if rec[1] == "DL":
            manufacturer = "Dell"
        elif rec[1] == "GW":
            manufacturer = "GATEWAY"
        elif rec[1] == "HP":
            manufacturer = rec[1]
        else:
            manufacturer = "ERROR"

        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]
        os = rec[6]
        year = rec[7]

        if num_hdd == "1":
            hdd_2 = "N/A"
        elif num_hdd == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]
            
        #sort file data into lists
        comp_type_list.append(comp_type)
        manufacturer_list.append(manufacturer)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        os_list.append(os)
        year_list.append(year)

        for i in range(len(processor_list)):
            comp_type = comp_type_list[i]
            manufacturer = manufacturer_list[i]
            processor = processor_list[i]
            ram = ram_list[i]
            hdd_1 = hdd_1_list[i]
            num_hdd = num_hdd_list[i]
            hdd_2 = hdd_2_list[i]
            os = os_list[i]
            year = year_list[i]

        if int(year) <= ryear:
            if comp_type == "Desktop":
                drcount += 1
                drcost += cpdesktop
            elif comp_type == "Laptop":
                lrcount += 1
                lrcost += cplaptop

        total_records += 1

        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(comp_type, manufacturer, processor, ram, hdd_1, num_hdd, hdd_2, os, year))

    print(f"\n")
    print(f"Total number of records: {total_records}")
    print (f"To replace {drcount} desktops it will cost: ${drcost}")
    print (f"To replace {lrcount} laptops it will cost: ${lrcost}")
    print (f"\n")
