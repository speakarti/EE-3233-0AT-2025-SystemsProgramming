#!/bin/user/env python3
import array as arr

##############################################
# Lab Assignment 2 - Binary Search
##############################################
def binary_search(myarray, val):
    nmid = len(myarray)//2
    mid_val = myarray[len(myarray)//2]
    print("nmid: ", nmid, mid_val)

    if mid_val < nmid:
        #let
        print("nmid: NOT FOUND", nmid)
        #fing left subarray 
        binary_search(myarray[:nmid], val)
    elif mid_val > nmid:
        #right
        print("nmid: NOT FOUND", nmid)
        binary_search(myarray[nmid:], val)
    elif mid_val == nmid:
        #found
        print("nmid: NOT FOUND", nmid)
        return nmid
    else:
        print("nmid: NOT FOUND", nmid)
        print("nmid: NOT FOUND", nmid)
        
    return nmid


if __name__ == '__main__':
    myarray = arr.array('i',[n for n in range(10)]) # this will make an array of 0-9
    # val=10
    print("myarray: ", myarray)
    print(binary_search(myarray, 3))
    print(binary_search(myarray, 7))
    print(binary_search(myarray, 11))
    print(binary_search(myarray, 20))
