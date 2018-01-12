# Jeff Starr, 20 December, 2017

# This is a function that takes as input a generic matrix with row labels, 
# column headings, and non-blank cells in the body.  It returns a 
# flattened file with records of of "column heading" + " | " + "row label"
# corresponding to the non-blank cells. 

#------------Imports, initialization, and read the input_matrix----------

import csv

def process_matrix(input_matrix_filename):
    """Take matrix as an argument and return output list."""

    # initialize several lists
    input_matrix = []
    column_headings = []
    row_labels = []
    output_list = []


    # Read in the data from a csv into a reader object.  Iterate through that
    # reader object and append each row (which is a list) to a list-of-lists
    # called input_matrix.

    with open(input_matrix_filename, encoding='utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            input_matrix.append(row)

    # ----Clean up the matrix and create heading and label lists-----

    # Put the first row of input_matrix into list column_headings.  Pop off the 
    # first item which is over the row labels.  Finally, remove this
    # top row from input_matrix.

    column_headings = input_matrix[0]
    column_headings.pop(0)
    input_matrix.pop(0)

    # Grab the first item in each row.
    # Append it to a list of row_labels.
    # Then, pop off the first item. 

    for row in input_matrix:
        row_labels.append(row[0])
        row.pop(0)

    # ---------Build the records of output_list-----------------

    # Walk through the remaining core of the matrix.
    # If item is blank, pass over.
    # If the item is not blank create the record.

    r = 0
    c = 0

    for row in input_matrix:
        for cell in row:
            if cell == '':
                pass
            else:
                output_list.append(
                    column_headings[c].strip() +" | "+
                    row_labels[r].strip()
                    )
            c +=1
        r+=1
        c = 0
    
    output_list.sort()

    return output_list

