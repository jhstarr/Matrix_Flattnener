# Jeff Starr, 20 December, 2017

# This is a program that calls the matrix_flattener_function then 
# writes the data returned into a file.

import csv
import json
import os
from matrix_flattener_function import process_matrix

input_matrix_filename = os.path.expanduser(
    "~/Documents/Coding/Projects/" +
    "PRODUCTION_DATA/Matrix_Flattener_data/input_matrix_test1.csv"
    )


output_list_filename = os.path.expanduser(
    "~/Documents/Coding/Projects/PRODUCTION_DATA/" +
    "Matrix_Flattener_data/output_list_test11.csv"
    )

output_list = process_matrix(input_matrix_filename)


# Note that writerow expects a sequence. The square brackets around row
# prevent writerow from placing each character in its own column.

with open(output_list_filename, 'w', encoding='utf-8') as f_write:
    writer = csv.writer(f_write)
    for row in output_list:
        writer.writerow([row])


# The following writes the output_list as json to a file so that it can be
# checked by a human then used for testing.

"""
output_json_filename = os.path.expanduser(
    "~/Documents/Coding/Projects/" +
    "Matrix_Flattener/test_files/output_list_answer1.json"
    )
with open(output_json_filename, 'w') as outfile:
    json.dump(output_list, outfile)
"""