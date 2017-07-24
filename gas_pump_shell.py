    #user selects if they want regular mid grade or premium

import gas_pump_core
from time import sleep as sl
slow_type = gas_pump_core.slow_type
import sys

    #pay after fill option
    #user inputs number of gallons
    #computer displays the cost



    #pre-pay
    #user inputs amount of money to pay
    #computer displays amount of gallons paid for
def main():
    inventory = gas_pump_core.open_inventory('gas_tank.txt')
    gas_pump_core.intro()
    gas_pump_core.pretty_inventory(inventory)
    type_of_gas = input("\n\t-> ").strip()
    slow_type('\n\tღ   What payment method do you want to use?   ღ\n\t\t==PLEASE ENTER NUMBER ONLY==\n\n\t\t1. Pay after fill\n\t\t2. Pre-pay?\n')
    function = input("\n\t-> ")
    current_time = gas_pump_core.current_time()
    if function == '1':
        slow_type("\tღ   How many gallons would you like to use?   ღ\n")
        gallons = float(input("\n\t->"))
        money = gas_pump_core.pay_after_fill(type_of_gas, gallons)

    elif function == '2':
        slow_type("\tღ   How much money would you like to pay?  ღ")
        money = float(input("\n\n\t-> $"))
        gallons = gas_pump_core.pre_pay(type_of_gas, money)

    else:
        print("\t⚠Invalid Input.!⚠")
        sys.exit()
        
    print("\n\n\tPumping...⛽\n")
    sl(3)
    revenue = 0
    gas_pump_core.append_log(type_of_gas,function, gallons, money, current_time )
    gas_pump_core.receipt(type_of_gas,function, gallons, money, current_time)
    gas_pump_core.update_inventory(type_of_gas, gallons, inventory)
    gas_pump_core.refuel(type_of_gas, inventory)
    revenue = gas_pump_core.total_revenue(revenue, inventory)
    print("\tTotal Revenue So Far:", revenue)
    print("---------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()

#nice clean code
#nice interface and computer experience
#use funtions and make it personalized
