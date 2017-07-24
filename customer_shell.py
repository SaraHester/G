    #user selects if they want regular mid grade or premium

import gas_pump_core
from time import sleep as sl
slow_type = gas_pump_core.slow_type
import sys
import gas_pump_disk
    #pay after fill option
    #user inputs number of gallons
    #computer displays the cost
def pretty_inventory(inventory):
    s = ''
    for item in inventory:
        ind = inventory.index(item)
        # print(item, ind, '\n')
        phrase = ("\n\t\t", str(ind + 1) + "." + str(inventory[ind][0]).capitalize() + " - $" + str(inventory[ind][2]) + "\n\t\t\t Gallons in stock: " + str("{0:.2f}".format(inventory[ind][1])))
        for item in phrase:
          slow_type_phrase
def input_gas_type(inventory):
    while True:
        type_of_gas = input("\n\t\t-> ")
        if int(type_of_gas) in range(len(inventory) + 1) :
            return type_of_gas
        else:
            slow_type("\n\t\tInvalid Input.\n\t\tPlease enter a valid number.\n")

def function_input():
    while True:
        function = input("\n\t\t-> ")
        if function == '1' or function == '2':
            return function
        else:
            slow_type("\n\t\tInvalid Input.\n\t\tPlease enter a valid number.\n")
def gallons_input(inventory, type_of_gas):
    while True:
        gallons = float(input("\n\n\t-> $"))
        if inventory[int(type_of_gas) - 1][1] - gallons > 0:
            return gallons
        else:
            slow_type("\n\t\tSorry. We do not have that many gallons to sell.\n\t\tPlease enter another amount.\n")
def money_input(inventory, type_of_gas, money):
    while True:
        money = float(input("\n\t->"))
        gallons = gas_pump_core.pre_pay(inventory, type_of_gas, money)
        if inventory[int(type_of_gas)- 1][1] - gallons > 0:
            return money
        else:
            slow_type("\n\t\tSorry. We do not have that many gallons to sell.\n\t\tPlease enter another amount.\n")



    #pre-pay
    #user inputs amount of money to pay
    #computer displays amount of gallons paid for
def main():
    print("---------------------------------------------------------------------------------")
    revenue = 0
    money = 0
    gas_pump_core.intro()
    inventory = gas_pump_disk.open_inventory('gas_tank.txt')
    gas_pump_core.pretty_inventory(inventory)
    current_time = gas_pump_core.current_time()
    slow_type('\n\n\tღ   What kind of gas do you want to use?   ღ\n\t\t==PLEASE ENTER NUMBER ONLY==')
    type_of_gas = input_gas_type(inventory)
    slow_type('\n\tღ   What payment method do you want to use?   ღ\n\t\t==PLEASE ENTER NUMBER ONLY==\n\n\t\t1. Pay after fill\n\t\t2. Pre-pay?\n')
    function = function_input()
    if function == '1':
        slow_type("\tღ   How many gallons would you like to use?   ღ\n")
        gallons = gallons_input(inventory, type_of_gas)
        money = gas_pump_core.pay_after_fill(inventory, type_of_gas, gallons) 
    elif function == '2':
        slow_type("\tღ   How much money would you like to pay?  ღ")
        money = money_input(inventory, type_of_gas, money)
        gallons = gas_pump_core.pre_pay(inventory, type_of_gas, money)

    gas_pump_core.pump(money, gallons)
    gas_pump_disk.update_inventory(type_of_gas, gallons, inventory)
    gas_pump_disk.append_log(inventory, type_of_gas, function, gallons, money, revenue, current_time )
    gas_pump_core.receipt(inventory, type_of_gas,function, gallons, money, current_time)
    gas_pump_disk.auto_refuel(inventory)
print("---------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()

#nice clean code
#nice interface and computer experience
#use funtions and make it personalized
