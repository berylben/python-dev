import sys

# This is an infinite loop that will keep running until the user types 'exit'
while True:
    
     # This print statement will display the message "Type exit to exit." to the user
    print('Type exit to exit.')
    
    # This line gets input from the user and saves it as a string in the variable 'response'
    response = input()
    
    # This if-statement checks if the user's input matches the string 'exit'
    if response == 'exit':
        sys.exit()
        
         # This print statement will display the message "You typed ' + response + '." to the user
    print('You typed ' + response + '.')


