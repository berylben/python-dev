#! /usr/bin/python3
# that takes a list of lists of strings and displays it in a well-organized table with each column right-justified

# table data to be displayed
tableData = [['apples', 'oranges', 'cherries', 'banana'],                 
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)  # Create a list containing the same number of 0 values as the number of inner lists in tableData

    # Find the longest strings in each column
    for i, sublist in enumerate(tableData):
        colWidths[i] = len(max(sublist, key=len))  # Update the width of each column

    # Compute the width of each column
    # column_widths = [len(max(col, key=len)) for col in zip(*tableData)] 

    # Print the column widths
    # print(column_widths)

    # Print the table data
    for row in zip(*tableData):
        print(f"| {' | '.join(string.rjust(colWidths[i]) for i, string in enumerate(row))} |")
printTable(tableData)