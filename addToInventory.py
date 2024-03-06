# Import the displayInventory function from the inventory module
from inventory import displayInventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Define a function to add items to the inventory
def addToInventory(inventory, addedItems):
    for i in addedItems: 
        if i in inventory: # If the item already exists in the inventory
            inventory[i] += 1 # Increase the count of that item
        else: # Otherwise, add the new item to the inventory
            inventory.update({i:1})
            
            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)