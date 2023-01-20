# Place code below to do the analysis part of the assignment.

# import csv module
import csv

# open a file in read mode
with open('clean_data.csv', 'r') as f:

    reader = csv.reader(f)

    # skip header
    next(reader)
    year_average_list=[]
    n=10
    year=[]

    # loop through each row in the file
    for row in reader:
        if n%10==0 or row[0]=='2021':
            year.append(row[0])
        temp_list = row[1:]
        temp_list = [float(i) for i in temp_list]
        year_average=sum(temp_list)/len(temp_list)
        year_average_list.append(year_average)
        n+=1
    n=10

    # create a list that will hold the average values
    decade_average=[]
    decade_list=[]

    # loop through each values in the list
    for year_average in year_average_list:
        if (n%10==0 and n!=10) or n==151:
            average=sum(decade_list)/len(decade_list)
            decade_average.append(format(average,'.2f'))

            # create a list that will hold the decades
            decade_list=[]
        n+=1
        decade_list.append(year_average)
    for i in range(len(year)-2):

        # print out results
        print('year '+year[i]+' to '+str(int(year[i+1])-1)+'\t'+decade_average[i])
    print('Year 2020 to 2021'+'\t'+decade_average[-1])