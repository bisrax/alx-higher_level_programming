#!/usr/bin/python3

'''
dont copy the address of the old list
'''

def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    
    new_list=list(my_list)
   
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list[idx]=element
        return new_list
