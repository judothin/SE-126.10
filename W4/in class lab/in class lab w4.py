# Jayden Fagre
# Date: 2/2/24
# Prompt: Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

# Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third time, record by record including average score and average letter equivalent.  After this third print of the original file data, print to the console the total number of student's in the class along with the class numeric average.  

# After your final display using the 1D parallel lists, create one new, empty list, that will become a 2D list.  Then, using a for loop and the 1D parallel lists, store the data to the 2D list you have created. Each index in the 2D list should contain a list of data. This list of data should contain the fname, lname, test1, test2, test3, num_average, and letter_average for the respective student.

import csv

fname = []
lname = []
test1 = []
test2 = []
test3 = []

# path to file
with open ('W4\in class lab\listPractice1-1.txt') as csvfile:

    # read file
    reader = csv.reader(csvfile)

    # store data from file fields to their respective lists
    for rec in reader:
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
# labels
print (f"{'First':12} \t {'Last':12} \t {'Test1'} \t {'Test2'} \t {'Test3'}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# display the file data
for i in range(0, len(fname)):
    print (f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]} \t {test2[i]} \t {test3[i]}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print (f"\n")

numavg = 0
total = 0
avg = []
let_avg = []

for i in range(0, len(test1)):

    # math
    numavg = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(numavg)

print (f"{'First':12} \t {'Last':12} \t {'Average'}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(0, len(fname)):
    print (f"{fname[i]:12} \t {lname[i]:12} \t {avg[i]:.1f}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# convert numavg to letter
# idk if these are accurate conversions, i just guessed
for i in range(0, len(avg)):
    if avg[i] >= 90:
        let_avg.append('A')
    elif avg[i] >= 80:
        let_avg.append('B')
    elif avg[i] >= 70:
        let_avg.append('C')
    elif avg[i] >= 60:
        let_avg.append('D')
    else:
        let_avg.append('F')

# 2d list
all_data = []

for i in range(0, len(fname)):
    all_data.append([fname[i], lname[i], test1[i], test2[i], test3[i], avg[i], let_avg[i]])

# final print    
print (f"{'First':<12} \t {'Last':<12} \t {'Test1'} \t {'Test2'} \t {'Test3'} \t {'Average'} {'Letter'}")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for rec in all_data:
    print(f"{rec[0]:<12} \t {rec[1]:<12} \t {rec[2]} \t {rec[3]} \t {rec[4]} \t {rec[5]:.1f} \t {rec[6]}")

# total number of students
total_students = len(all_data)

# class average
class_average = sum(student[5] for student in all_data) / total_students

print(f"\nTotal number of students: {total_students}")
print(f"Class average: {class_average:.1f}")