def spam():
    global eggs
    eggs = 'spam' # this is the    global
def bacon():
    eggs = 'bacon' # this is a local  
def bacon():
    eggs = 'bacon' # this is a local      
    eggs = 42 # this is the global
    spam()
    print(eggs)