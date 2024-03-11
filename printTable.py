#! /usr/bin/python3
# that takes a list of lists of strings and displays it in a well-organized table with each column right-justified

tableData = [['apples''oranges''cherries', 'banana'],                 
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# TODO: find the longest list
longest_strings = [max(sublist, key=len) for sublist in tableData]
print