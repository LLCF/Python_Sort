# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:10:53 2017

@author: charll
"""
from random import  randint
from time import  time
from functools import  wraps

def isSorted(a):
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def print_time(f):
    @wraps(f)
    def wrapped(*argv, **kargs):
        start = time()
        b = f(*argv, **kargs)
        print(isSorted(b),"  "+ f.__name__ +" time: ",time()-start)
        return b
    return wrapped
def create_data():    
    max_mun=10000
    num=50000
    nums=[]
    for i in range(num):
        nums.append(randint(0,max_mun))
    return nums   
@print_time
def insert_sort(a):
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if a[j]<a[j-1]:
                a[j-1],a[j] = a[j],a[j-1]
            else:
                break
    return a
 
def merge(left, right):
    r,l=0,0
    result=[]
    n = 50
    if len(left)<n or len(right)<n:
        #return select_sort(left+right)
        return sorted(left+right)
    if left[-1] < right[0]:
        return left+right
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result
@print_time
def merge_sort(a):
    return Merge_sort(a)

def Merge_sort(a):
    if len(a) <= 1:
        return a
    num = int(len(a)/2)
    left = Merge_sort(a[:num])
    right = Merge_sort(a[num:])
    return merge(left,right)

@print_time
def select_sort(a):
    for i in range(len(a)):
        n_min = i
        for j in range(i,len(a)):
            if a[n_min] > a[j]:
                n_min = j
        a[i],a[n_min] = a[n_min],a[i]  
    return a
@print_time
def hill_sort(a):
    n=5
    N = len(a)
    h=1
    while h<N//n:
        h = n*h + 1
    while h>=1:
        for i in range(h,N):
            for j in range(i,h-1,-h):
                if a[j] < a[j-h]:
                    a[j],a[j-h] = a[j-h],a[j]
                else:
                    break
        h=h//n
    return a

#def partition(a, lo, hi):
#    i, j = lo+1, hi-1
#    key = a[lo]
#    while True:
#        while a[i] < key:
#            if i == hi:
#                break
#            else:
#                i += 1
#        while a[j] > key:
#            if j == lo:
#               break
#            else:
#               j -= 1
#        if i>=j:
#          break
#        a[i], a[j] = a[j], a[i]	
#    a[lo], a[j] = a[j], a[lo]
#    return j
##@print_tim
#def fast_sort(a):
#    def sort(nums, lo, hi):
#        if hi <= lo:
#            return
#        j = partition(nums, lo, hi)
#        sort(nums, lo, j-1)
#        sort(nums, j+1, hi)
#    sort(a, 0, len(a)-1)
#    return a





def quick_sort(array,low,high):
    def sub_sort(array,low,high):
        key = array[low]
        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            while low < high and array[high] < key:
                array[low] = array[high]
                low += 1
                array[high] = array[low]
        array[low] = key
        return low
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)
@print_time
def fast_sort(array):
    quick_sort(array, 0, len(array)-1)
    return array
start = time()
print(isSorted(sorted(create_data()))," System sort time: ", time()-start)
#hill_sort(create_data())
fast_sort(create_data())
merge_sort(create_data())
#insert_sort(create_data())
#select_sort(create_data())
