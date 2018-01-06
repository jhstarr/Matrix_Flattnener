import unittest
import json
import csv
from matrix_flattener_function import process_matrix

class FlattenerTestCase(unittest.TestCase):
    """Tests for run_matrix_flattner.py"""

    # Remember, test methods must begin with the word "test."
    def test_case_1(self):
        """When the input_matrix_filename is put through the process_matrix() 
        function, does the returned results_list match the 
        corresponding output_list_answer.json?"""
        
        input_matrix_filename1 = 'test_files/input_matrix_test1.csv' 
      
        results_list1 = process_matrix(input_matrix_filename1)

        right_answer_file1 = 'test_files/output_list_answer1.json'
        with open(right_answer_file1) as f_obj:
            right_answer1 = json.load(f_obj)

        self.assertEqual(results_list1,right_answer1)

unittest.main()