stuff ={
    "knife":3,
    "rope":1,
    "torch":2,
    "gold-coin":7,
    "dagger":5,
    "arrows":12
}

def displayInventory(inventory):
    print("Inventory:")
    item_total= 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff) 