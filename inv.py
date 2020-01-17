
def displayInventory(inventory):
    count = 0
    for item, amountOf in inventory.items():
        print(item, amountOf)
    for numberOf in inventory:
        count += inventory[numberOf]
    print('Total number of items: ' + str(count))


# dict1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}
# displayInventory(dict1)
def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        if item in inventory:
            inventory[item] = inventory.get(item) + 1
        else:
            inventory[item] = 1
    return inventory
    # inventory[added items]
print("Inventory:")
inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)

print("This is for example purpooses, not real code")