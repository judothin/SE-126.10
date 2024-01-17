#jayden fagre
#01/17/24
#prompt:
#The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room
#can accommodate, and the number of people currently registered for the event. Write a
#program that displays all rooms that are over the maximum limit of people and the number of
#people that have to be notified that they will have to be put on the wait list. After the file is
#completely processed the program should display the number of records processed and the
#number of rooms that are over the limit.

import csv
total_records = 0
limit = 0
over_limit_rooms = 0

with open('W2\class lab\lab2a.csv') as csvfile:
    file = csv.reader(csvfile)

    #labels
    print("{:<20} {:<20} {:<20} {:<20}".format("Room:", " Max:", " Current:", "Over:"))

    for rec in file:
        total_records += 1
        if int(rec[2]) > int(rec[1]):
            limit = int(rec[2]) - int(rec[1])
            over_limit_rooms += 1

            
            #final msg
            print("{:<20} {:<20} {:<20} {:<20}".format(rec[0], rec[1], rec[2], limit))
        else:
            limit = 0
#final msg's
print("\n")
print(f'processed {total_records} record/s')
print(f'there are {over_limit_rooms} rooms over the limit')
