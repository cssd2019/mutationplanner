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
import numpy

#%% Test or dummy dictionary
octamer_scoresT = {'aaaaaaaa': [- 4.3231, - 5.252],
            'aaaaaaca': [- 3.1298, - 3.5631]}



#%%
def newScore(oct_dict,strategy):
    ''' Takes in a dictionary (oct_dict) and returns a disctioary with the same keys, but with the new scores to be used for plot
    strategy is a number: 1, 2 or 3 --> Defines different strategies for calculating the new score
    strategy 1 --> -1=silencer, 1 = enhancer, 0 = neither
    strategy 2 -->
    strategy 3 -->
    '''
    
    output_dict={}
    
    for k,v in oct_dict.items():     # k = key (e.g. 'aaaaaaaa'), v = value
        
        i_inx=v[0]
        p_inx=v[1]
        
        if (strategy == 1):
            pi=combinePI_1(i_inx,p_inx)
            
        elif (strategy == 2):
            pi=combinePI_2(i_inx,p_inx)
            
        elif (strategy == 3):
            pi=combinePI_3(i_inx,p_inx)
        
        output_dict[k]=pi
    
    return output_dict

            
#testing=newScore(octamer_scoresT, 1)    

#%%

def combinePI_1(iindex,pindex):
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


#%%
def combinePI_2(iindex,pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: positive number (over 2.62) --> Splicing enhancer
            0 --> Neither
            negative number (under -2.62) --> Splicing inhibitor
            
            999 --> Function did not do what it is supposed to, check code'''
        
    
    output_value=999
    if iindex > 2.62 and pindex > 2.62:
        output_value = numpy.mean([iindex,pindex])
        
    elif iindex < -2.62 and pindex < -2.62:
        output_value = numpy.mean([iindex,pindex])
        
    else:
        output_value = 0
    
    if output_value == 999:
        print("Something is wrong, nothing happened")
        output_value= "Something is wrong, nothing happened"
    
    return output_value

#%%
def combinePI_3(iindex,pindex):
    ''' Categorizing whether a octamer is a splicing enhancer, splicing inhibitor or neither
    Input: I-index (iindex) and P-index (pindex)
    output: positive number --> Splicing enhancer
            0 --> Neither
            Negative number --> Splicing inhibitor
            
            999 --> Function did not do what it is supposed to, check code'''
        
    
    output_value=999
    if iindex > 2.62 and pindex > 2.62:
        output_value = (iindex-2.62) + (pindex-2.62)
        
    elif iindex < -2.62 and pindex < -2.62:
        output_value = (iindex+2.62) + (pindex+2.62)
        
    else:
        output_value = 0
    
    if output_value == 999:
        print("Something is wrong, nothing happened")
        output_value= "Something is wrong, nothing happened"
    
    return output_value

#%% UNIT TESTING with pytest
    
def test_newScore1():
    dummy_dict={'aaaaaaaa': [- 4.3231, - 5.252],
                'aaaaaaca': [- 3.1298, - 3.5631],
                'whatever': [1,4],
                'abababab': [4, 3] }
    
    t=newScore(dummy_dict,1)
    
    assert t['aaaaaaaa']==-1
    assert t['whatever']==-0
    assert t['abababab']==1
    
#Testing if strategy == 2
def test_newScore2():
    dummy_dict={'aaaaaaaa': [- 4.62, - 5.62],
                'aaaaaaca': [- 3.1298, - 3.5631],
                'whatever': [1,4],
                'abababab': [4.62, 3.62] }
    
    t=newScore(dummy_dict,2)
    
    assert t['aaaaaaaa']==-5.12
    assert t['whatever']==-0
    assert t['abababab']==4.12
    
def test_newScore3():
    dummy_dict={'aaaaaaaa': [- 4.62, - 5.62],
                'aaaaaaca': [- 3.1298, - 3.5631],
                'whatever': [1,4],
                'abababab': [4.62, 3.62] }
    
    t=newScore(dummy_dict,3)
    
    assert t['aaaaaaaa']==-5
    assert t['whatever']==-0
    assert t['abababab']==3


def test_combinePI_1():
    assert combinePI_1(3,4) == 1
    assert combinePI_1(0.15,4) == 0
    assert combinePI_1(-2.9, -3.3) == -1
    

    


