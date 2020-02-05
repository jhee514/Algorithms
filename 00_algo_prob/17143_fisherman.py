import sys

sys.stdin = open("17143_input.txt", "r")

"""
1. fisher indexing
    if fisher_dir = 0:
        index -= 1
    elif fisher_dir = 1:
        index += 1
2. start
    fisher_dir = 0
    fisher_index = 0 ~ col-1
    if fisher_index > c-1: fisher_dir = 0 : index -= 1 
    if fisher_index < 0 : fisher_dir = 1 : index += 1
"""

