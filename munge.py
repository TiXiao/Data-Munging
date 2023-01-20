# Place code below to do the munging part of this assignment.
data = open("data.txt", "r")
lines = data.readlines()
data.close()
munging_process = []

# Delete irrelevant lines
for line in lines:
    if line[0] in "Year1234567890":
        munging_process.append(line)

# Remove redundant headers
remove_index = []
for line in range(1, (len(munging_process) - 1)):
    if munging_process[line] == munging_process[0]:
        remove_index.append(line)

x = 0
for i in remove_index:
    del munging_process[i + x]
    x -= 1

del munging_process[-1]

# Write a averaging function to clean up nan
def average(line):
    valid_numbers = []
    for item in line[1:-1]:
        if item != "nan":
            try:
                valid_numbers.append(int(item))
            except:
                pass
    average = sum(valid_numbers) / len(valid_numbers)
    return average

# Split the lines
# Write data into csv
# /100 * 1.8 for conversion in farenheiht
clean_data = open("clean_data.csv", "w")

for line in munging_process:
    line = line.split()
    for item in range(len(line) - 1):
        if item == 0:
            clean_data.write(line[item])
            clean_data.write(",")
        else:
            if "*" in line[item]:
                averaged = format(average(line) / 100 * 1.8, ".1f")
                clean_data.write(str(averaged))
                if item != len(line) - 2:
                    clean_data.write(",")
                else:
                    clean_data.write("\n")
            else:
                try:
                    clean_data.write(str(format(int(line[item]) / 100 * 1.8, ".1f")))
                except:
                    clean_data.write(line[item])
                if item != len(line) - 2:
                    clean_data.write(",")
                else:
                    clean_data.write("\n")    

# close file 
clean_data.close()