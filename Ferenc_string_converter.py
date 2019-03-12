#!/bin/bash/python

''' 
Function for converting a fasta dictionary upper case sequences to lower case sequences. 
'''

import string

def string_case_converter( fastaDictionary ):
	
	for k, v in fastaDictionary.items():
		
		fastaDictionary[k] = v.lower()

	return fastaDictionary
