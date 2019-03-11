# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:42:55 2019

@author: mariakan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:12:48 2019

@author: mariakan
"""
import pytest

def combinePI(iindex,pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: 1 --> Splicing enhancer
            0 --> Neither
            -1 --> Splicing inhibitor
            
            999 --> Function did not do what it is supposed to, check code'''
            
            
    output_value=999
    if iindex > 2.62 and pindex > 2.62:
        output_value = 1
        
    elif iindex < -2.62 and pindex < -2.62:
        output_value = -1
        
    else:
        output_value = 0
    
    if output_value == 999:
        print("Something is wrong, nothing happened")
        output_value= "Something is wrong, nothing happened"
    
    return output_value

def test_combinePI():
    assert combinePI(3,4) == 1
    assert combinePI(0.15,4) == 0
    assert combinePI(-2.9, -3.3) == -1
    



