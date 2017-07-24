
import time, sys, random, datetime
from time import sleep as sl
from random import choice as rand
def intro():
    print("\n---------------------------------------------------------------------------------\n")
    print("\t┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐")
    print("\t╎\t\t🚗 - - - -\t\t\t   ╎")
    print("\t╎\t   WELCOME TO SARA'S GAS STORE™\t\t   ╎\n\t╎\t   I hope your doing well.😄\t\t   ╎")
    print("\t└╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘\n")
    
def pump(money, gallons):
        phrase = "\n\tYou have paid $", str(money), " for ","{0:.2f}" .format(gallons), " gallons."
        for item in phrase:
            slow_type(item)
        print("\n\n\tPumping...⛽\n")
        sl(3)
def random_barcode_lines(length, height):
    '''int-> str'''
    choices =  "▎", "▏", "▍", "▌", "█", "▌", "▌"
    code = []
    for i in range(length):
        code.append(rand(choices))
    line = ''.join(code)
    return line


def rand_numbers(length):
    numbers = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
    code = []
    for i in range(length):
        code.append(rand(numbers))
    line = ''.join(code)
    return '\n║\t   ║'.join(line for _ in range(1))

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        sl(random.random()*10.0/100)
def gas_types(inventory):
    re = []
    for item in inventory:
        re.append(item[0])
    return re





def convert_back(inventory):
    """[[string(item name), int(quantity)]] -> str"""
    new_inventory = ''
    for item in inventory:
        new_inventory += '\n' + str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2])
    return new_inventory
def pretty_inventory(inventory):
    s = ''
    for item in inventory:
        ind = inventory.index(item)
        print("\n\t\t", str(ind + 1), ".", str(inventory[ind][0]).capitalize(), " - $", str(inventory[ind][2]), "\n\t\t\t Gallons in stock: ", str("{0:.2f}".format(inventory[ind][1])))
def check_inventory(inventory, gallons):
    for item in inventory:
        if item[1] - gallons <= 0:
            return 0
        else:
            return 1
def price_of(inventory, type_of_gas):
    type_of_gas = convert_type_of_gas(inventory, type_of_gas)
    for item in inventory:
        if item[0] == type_of_gas:
            return float(item[2])


def pay_after_fill(inventory, type_of_gas, gallons):
    '''str, float -> float'''
    price = price_of(inventory, type_of_gas)
    money = gallons * price 
    money = "{0:.2f}" .format(money)

    
    return float(money)




def pre_pay(inventory, type_of_gas, money):
    '''str, float -> float'''
    price = price_of(inventory, type_of_gas)
    gallons = money / price
    gallons = "{0:.2f}" .format(gallons)
    return float(gallons)


def get_sales_tax(type_of_gas, money):
    '''str, float, float -> float'''
    sales_tax = money * .07
    sales_tax1 =  "{0:.2f}".format(sales_tax)
    sales_tax1 = float(sales_tax1)
    return sales_tax1


def current_time():
    '''None -> str'''
    s = datetime.datetime.now()
    return s

def convert_type_of_gas(inventory, type_of_gas):
    type_of_gas = inventory[int(type_of_gas) - 1][0]
    return type_of_gas
def convert_function(function):
    if function == '1':
        function = 'Pay After Fill'
    elif function == '2':
        function = 'Pre-Pay'
    else:
        print('Invalid Input')
        return None
    return function
def receipt(inventory, type_of_gas, function, gallons, money, date):
    '''str, float, float, str -> str'''
    cost = price_of(inventory, type_of_gas)
    sales_tax = get_sales_tax(type_of_gas, money)
    total_sales = money + sales_tax
    code =random_barcode_lines(20, 2)
    type_of_gas = convert_type_of_gas(inventory, type_of_gas)
    type_of_gas = type_of_gas.capitalize()
    function = convert_function(function)
    slow_type("\tHere is your receipt.\n\t😄Have a good day!😄")
    print("\n")
    print("\t╔══════════════════════════════════════════════╗")
    print("\t║     §      ♥ Sara's Gas Store™ ♥     §       ║")
    print("\t║----------------------------------------------║")
    print("\t║Gas Type:", type_of_gas.ljust(35), "║")
    print("\t║Payment Method:", function.ljust(29), "║")
    print("\t║Total gallons:", gallons, "".ljust(29 - len(str(gallons))), "║")
    print("\t║Cost per gallon:", cost, "".ljust(27 - len(str(cost))), "║")
    print("\t║Sales:", money, "".ljust(37 - len(str(money))), "║")
    print("\t║Sales Tax: 0.07                               ║")
    print("\t║Total Sales Tax:", sales_tax, ''.ljust(27- len(str(sales_tax))), "║")
    print("\t║Total sales:",total_sales , ''.ljust(31 - len(str(total_sales))), "║" )
    print("\t║Transaction time:", date, " ║" )
    print("\t║--------------------------------------------- ║" )
    print("\t║            ",code, "            ║")
    print("\t║            ",code, "            ║")
    print("\t║            ", rand_numbers(20),"            ║")
    print("\t║                                              ║")
    print("\t║                                              ║")
    print("\t║==============================================║")
    print("\t║                                              ║" )
    print("\t║EARN YOUR CHANCE AT $500!!!!!                 ║")
    print("\t║`just go to the link below`                   ║" )
    print("\t║www.earnfreemoney.org                         ║" )
    print("\t║==============================================║" )
    print("\t╚══════════════════════════════════════════════╝")
    print("\n")
    