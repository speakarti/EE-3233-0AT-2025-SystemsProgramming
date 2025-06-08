#!/bin/user/env python3
import array as arr

##############################################
# Lab Assignment 2 - Binary Search
##############################################


##############################################
# function to search a val in an array between index:left and right
# my array shoudl be a sorted array
##############################################
def binary_search_recursive(myarray, val, left, right):    
    if left > right:
        print("val: {0} not found".format(val))
        return -1

    nmid = (left+right)//2
    mid_val = myarray[nmid]
    #print("nmid: ", nmid, mid_val)
    
    if val == mid_val:
        #found
        print("found {0} at index {1}".format(val, nmid))
        return nmid
    elif val < mid_val :
        #search left tree
        right=nmid - 1        
    elif val > mid_val:
        #right tree
        left= nmid + 1
        
    return binary_search_recursive(myarray, val, left, right)


##############################################
# function to search a val in an array using binary search method
# my array shoudl be a sorted array
##############################################
def binary_search(myarray, val):
    left=0
    right=len(myarray) - 1
    return binary_search_recursive(myarray, val, left, right)


if __name__ == '__main__':
    myarray = arr.array('i',[n for n in range(10)]) # this will make an array of 0-9
    # val=10
    print("myarray: ", myarray)
    print(binary_search(myarray, 3))
    print(binary_search(myarray, 7))
    print(binary_search(myarray, 11))
    print(binary_search(myarray, 20))
    print(binary_search(myarray, 25))