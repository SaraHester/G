import gas_pump_core
def open_log(file):
    """() -> [[string(item name), int(quantity)]]"""
    new_inventory = []
    with open (file, 'r') as file_2:
        file_2.readline()
        inventory = file_2.readlines()
    for element in inventory:
        type1, method, gallons, price, revenue, time = element.split(', ')
        new_inventory.append([type1.strip(), method.strip(), float(gallons.strip()), float(price.strip()), float(revenue.strip()),  time.strip()])
    return new_inventory
def append_log(inventory, type_of_gas, function, gallons, money, revenue, date):
    '''str, float, float -> str'''
    type_of_gas = gas_pump_core.convert_type_of_gas(inventory, type_of_gas)
    revenue = total_revenue(revenue)
    function = gas_pump_core.convert_function(function)
    with open('gas_pump_log.txt', 'a') as file_1:
        date = str(date)
        file_1.write(type_of_gas+ " ,  " +  function + " , " + str(gallons)+ " , " + str(money) + " , " + str(revenue) + ", " +  date + "\n")
    print("\n\n")
    print("\t===Transaction Added To Log===")
    print("\n")
def open_inventory(file):
    """() -> [[string(item name), int(quantity)]]"""
    new_inventory = []
    with open (file, 'r') as file_2:
        file_2.readline()
        inventory = file_2.readlines()
    for element in inventory:
        type1, quantity, price = element.split(', ')
        new_inventory.append([type1.strip(), float(quantity.strip()),float(price.strip())])
    return new_inventory
def update_inventory(type_of_gas, gallons, inventory):
    if type_of_gas == '1':
        inventory[0][1] = inventory[0][1] - gallons
    elif type_of_gas == '2':
        inventory[1][1] = inventory[1][1] - gallons
    elif type_of_gas == '3':
        inventory[2][1] = inventory[2][1] - gallons
    
    with open ('gas_tank.txt', 'w') as file_2:
        new_inventory = gas_pump_core.convert_back(inventory)
        file_2.write(new_inventory)
def auto_refuel(inventory):
    for item in inventory:
        if item[1] <= 100:
            item[1] = 5000
  
    with open ('gas_tank.txt', 'w') as file_2:
        new_inventory = gas_pump_core.convert_back(inventory)
        file_2.write(new_inventory)
def refuel(inventory):
    for item in inventory:
        item[1] = 5000
    with open ('gas_tank.txt', 'w') as file_2:
        new_inventory = gas_pump_core.convert_back(inventory)
        file_2.write(new_inventory)
def total_revenue(revenue):
    log = open_log('gas_pump_log.txt')
    for item in log:
        revenue += item[3] 
    return revenue