
# name in Python

import xlrd
import subprocess
import os
 
 
loc = ("../excelread.xlsx")

os.system("ls")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)

def getdataset(columnval):
    val = columnval.replace(":",".")
    return val.split(".")[0]

# For row 0 and column 0
sheet.cell_value(0, 0)
enableList = []
disableList = []
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 1).lower())
    if sheet.cell_value(i, 1).lower() == "enable":
      enableList.append(getdataset(sheet.cell_value(i, 2)))
    elif sheet.cell_value(i, 1).lower() == "disable":
      disableList.append(getdataset(sheet.cell_value(i, 2)))
print(list( dict.fromkeys(enableList) ))
print(list( dict.fromkeys(disableList) ))


os.system("chmod +x datastores.txt")

with open("datastores.txt") as file_in:
    lines = []
    for line in file_in:
       lines.append(line.rstrip())
    print(lines)

for x in enableList:
   if x not in lines:
     append_new_line('datastores.txt', x)
print(lines)


os.system("git add .")
os.system("git commit -m 'code push'")
os.system("git push")

