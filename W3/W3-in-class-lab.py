#Jayden Fagre
#1/23/24
#prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

import csv
total_records = 0

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

processor_list = []
year_list = []
os_list = []
comp_type_list = []
manufacturer_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []

import csv

with open ('W2/w2d2 lab2/lab2b.csv') as csvfile:
    file = csv.reader(csvfile)

    #labels (yes i looked up how to line them up like this)
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Type", "Man", "Proc", "RAM", "HDD1", "HDD_NUM", "HDD2", "OS", "Year"))

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

        #figuring this out was annoying ngl
        if num_hdd == "1":
            hdd_2 = "N/A"
        elif num_hdd == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]

        total_records += 1

        os_list.append(os)
        comp_type_list.append(comp_type)
        manufacturer_list.append(manufacturer)
        processor_list.append(processor)
        ram_list.append(ram)
        hdd_1_list.append(hdd_1)
        num_hdd_list.append(num_hdd)
        hdd_2_list.append(hdd_2)
        year_list.append(year)

        #final printed msg
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(comp_type, manufacturer, processor, ram, hdd_1, num_hdd, hdd_2, os, year))

        if comp_type == "Desktop":
            desktop_num = comp_type.count("Desktop")
            print("Number of desktops: ", desktop_num)
            if year <= ("16"):
                print(f"Cost to replace {desktop_num} desktops: ", 2000 * desktop_num)
        if comp_type == "Laptop":
            laptop_num = comp_type.count("Laptop")
            if year <= "16":
                print("Cost to replace laptops: ", 1500 * laptop_num)

#start of lab 3
#print total amount of records processed

print(f"Total number of records: {total_records}")
