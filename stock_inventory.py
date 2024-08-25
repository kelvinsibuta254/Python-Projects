class OutOfStockError(Exception):
    """Custome exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock. "
    
#Inventory
stationary_inventory = {
    "pens": 10,
    "media": 400,
    "markers": 0,
    "books": 10,
    "gauze": 1,
    "soap": 1,
    "ethanol": 2,
    "bleach": 0
}

#Purchasing supplies
def pick_item(item, quantity):
    try:
        if stationary_inventory[item] == 0: #accessing an item from a dict (serves as a stationary in this case)
            raise OutOfStockError(item)
        else:
            print(f"Successful: {quantity} {item} (s)")
            stationary_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

#Testing the Custom exception
try:
    pick_item("markers", 10)
    pick_item("ethanol", 1)
    pick_item("dishes")
except OutOfStockError as e:
    print(e)
