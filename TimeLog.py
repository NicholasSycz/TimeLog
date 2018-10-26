# This script is designed to read in a file containing the employee's name and the hours they worked for each day
# USAGE: python TimeLog.py
#        <directory path of files>

import os,sys
import string
# path input from the user
path = raw_input("Where are the files?\n")

# storage for the data in the file
files = []

# looping through the directory and appends the files into the file array
for i in os.listdir("%s" % path):
    if i.endswith('.txt'):
        files.append(i)

# searching throught the files
for element in files:
    f = open(element, 'r')
    x = f.readlines()
    hours = x[1:]
    employee = x[0]
    f.close()

    # storage for the hour values
    hr_vals = []
    mn_vals = []

    # loop through the data to find the hours
    for line in hours:
        data = line.split()

        if len(data) > 1:
            # getting the hours and converting them to minutes
            col = data[1]
            col_len = len(col)
            val = col[col_len-3]
            val = int(val) * 60
            hr_vals.append(val)

            # getting the minutes
            col2 = data[2]
            col2len = len(col2)
            val2 = [col2[col2len-5], col2[col2len-4]]
            new_val = ''.join(val2)
            new_val = string.join(val2, '')
            new_val = int(new_val)
            mn_vals.append(new_val)

    # Adding together all the values then converting them to seconds
    hr_vals = sum(hr_vals)
    mn_vals = sum(mn_vals)
    total_vals = hr_vals + mn_vals
    seconds = total_vals * 60

    # function for converting the employee times
    def timeConversion(employee, seconds):
        time = seconds
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        out = [employee, "%dhrs "%(hour), "%dmins" %(minutes)]
        out = ''.join(out)
        return "%s\n\n" %out

    # appending the data to output.yeet
    with open('output.yeet', 'a') as output:
        output.write(timeConversion(employee,seconds))
