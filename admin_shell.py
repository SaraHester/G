import gas_pump_core, gas_pump_disk
from time import sleep as sl
slow_type = gas_pump_core.slow_type
import sys
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
def password():
    password = '12345678'
    while True:
        password_guess = input("\n\t\tPLease enter Password\n\n\t\t\t")
        if password_guess == password:
            return password
        else:
            print("\n\t\tWrong password. Try Again\n\n\n")
def main():
    revenue = 0
    print("---------------------------------------------------------------------------------")
    inventory = gas_pump_disk.open_inventory('gas_tank.txt')
    password()
    slow_type("\n\t\t    Welcome Administrator")
    desicion = ''
    while desicion != '5':
        slow_type(".\n\t\tWhat would you like to do today?\n\t\t===PLEASE ENTER NUMBER ONLY===\n")
        slow_type("\n\t\t1. Pump\n\t\t2. Refuel\n\t\t3. Check our inventory\n\t\t4. Check your revenue\n\t\t5. Leave")
        desicion = input("\n\n\t\t-> ")
        if desicion == '1':
            inventory = gas_pump_disk.open_inventory('gas_tank.txt')
            gas_pump_core.pretty_inventory(inventory)
            type_of_gas = input("\n\t-> ").strip()
            slow_type('\n\tღ   What payment method do you want to use?   ღ\n\t\t==PLEASE ENTER NUMBER ONLY==\n\n\t\t1. Pay after fill\n\t\t2. Pre-pay?\n')
            function = input("\n\t-> ")
            current_time = gas_pump_core.current_time()
            if function == '1':
                slow_type("\tღ   How many gallons would you like to use?   ღ\n")
                gallons = float(input("\n\t->"))
                money = gas_pump_core.pay_after_fill(inventory, type_of_gas, gallons)

            elif function == '2':
                slow_type("\tღ   How much money would you like to pay?  ღ")
                money = float(input("\n\n\t-> $"))
                gallons = gas_pump_core.pre_pay(inventory, type_of_gas, money)

            else:
                print("\t⚠ Invalid Input! ⚠")
                sys.exit()
                
            print("\n\n\tPumping...⛽\n")
            sl(3)
            revenue = 0
            gas_pump_disk.append_log(inventory, type_of_gas, function, gallons, money, revenue, current_time )
            gas_pump_core.receipt(inventory, type_of_gas,function, gallons, money, current_time)
            gas_pump_disk.update_inventory(type_of_gas, gallons, inventory)
            gas_pump_disk.auto_refuel(inventory)
            revenue = gas_pump_disk.total_revenue(revenue)
        elif desicion == '2':
            slow_type("\n\tAre you sure you want to refuel?\n\t\t===PLEASE ENTER NUMBER ONLY===\n\t\t1. Yes\n\t\t2. No")
            answer = input("\n\n\t\t-> ")
            if answer == '1':
                gas_pump_disk.refuel(inventory)
                slow_type("Tanks have been refueled")
            elif anser == '2':
                slow_type("\n\tOk sir/mam. Have a nice day!!!")
        elif desicion == '3':
            gas_pump_core.pretty_inventory(inventory)
        elif desicion == '4':
            revenue = gas_pump_disk.total_revenue(revenue)
            print("\tTotal Revenue So Far:", revenue)
    print("---------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()