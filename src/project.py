import time
import csv
import os.path
import operator

def csv_to_list(csv_file, delimiter=','):
   
    #Reads in a CSV file and returns the contents as list,
    #where every row is stored as a sublist, and each element
    #in the sublist represents 1 cell in the table.
    
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)

def print_csv(csv_content):
    # Prints CSV file to standard output.
    print(50*'-')
    for row in csv_content:
        row = [str(e) for e in row]
        print('\t\t'.join(row))
    print(50*'-')
    
def convert_cells_to_floats(csv_cont):
    
    #Converts cells to floats if possible (modifies input CSV content list).
    
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = float(csv_cont[row][cell])
            except ValueError:
                pass 
    
def sort_by_column(csv_cont, col, reverse=False):
  
    #Sorts CSV contents by column name (if col argument is type <str>) 
    #or column index (if col argument is type <int>). 
    
    header = csv_cont[0]
    body = csv_cont[1:]
    if isinstance(col, str):  
       col_index = header.index(col)
    else:
        col_index = col
    body = sorted(body, 
           key=operator.itemgetter(col_index), 
           reverse=reverse)
    body.insert(0, header)
    return body

def write_csv(dest, csv_cont):
    #Writes a comma-delimited CSV file.

    with open(dest, 'w') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in csv_cont:
            writer.writerow(row)


	
#Welcome screen

print("Welcome to the Statistical Organiser!")

time.sleep(.5)

statsfile = raw_input("\nWhat file do you want to use: ")
time.sleep(1)

if(os.path.exists(statsfile) == False):
	print("File does not exist")
	statsfile = raw_input("What file do you want to use: ")

#Opens file

csv_cont = csv_to_list(statsfile)

print('\nRaw CSV format')
for row in range(4):
    print(csv_cont[row])
time.sleep(1)
print("\nMaking it look better! :)")

time.sleep(2)

print('\nCleaner CSV file:')
print_csv(csv_cont)

column_sort = raw_input("\nWhich column you would like to sort by?")

print('\n\nCSV sorted by column %s' %column_sort)
convert_cells_to_floats(csv_cont)
csv_sorted = sort_by_column(csv_cont, column_sort)
print_csv(csv_sorted)

new_file = raw_input("\nWhat should the new file name be?")

write_csv(new_file, csv_sorted)
