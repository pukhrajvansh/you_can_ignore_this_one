
machine =  '''
   ________________________________
  |                                |
  |         COFFEE MACHINE         |
  |________________________________|
  |  [1] Espresso       [2] Latte  |
  |                                |
  |  [3] Cappuccino                |
  |________________________________|
  |                                |
  |  [4] Start     [5] Power Off   |
  |________________________________|
  |       OWNER FUNCTIONS          |
  |________________________________|
  |  [6] Check level of ingredients|
  |  [7] Check total cup sold      |
  |  [8] fill up ingredients       |
  |  [9] check total earnings      |
  |________________________________|

'''

def round_num(num):
    a = 2.34
    b = round(a * 2) / 2
    print(b)



coffee_menu = {
    "Espresso": {
        "water": 50,     # in ml
        "milk": 0,       # in ml
        "coffee": 18,    # in grams
        "money": 100     # in INR
    },
    "Latte": {
        "water": 200,    # in ml
        "milk": 150,     # in ml
        "coffee": 24,    # in grams
        "money": 150     # in INR
    },
    "Cappuccino": {
        "water": 250,    # in ml
        "milk": 100,     # in ml
        "coffee": 24,    # in grams
        "money": 180     # in INR
    }
}

total = 0
total_cups = {
    "Espresso": 0,
    "Latte": 0,
    "Cappuccino": 0
}
    

money = {
    "ten": 0,
    "fifty": 0,
    "hundred": 0
}

watter = 250
milk = 250
coffee = 100
money = 0

def report():
    return f"{watter}\n{milk}\n{coffee}\n{money}"





# not_sufficent = []


end_session = False
while not end_session:

    off = False
    while not off:
        print(machine)
        
        ask = int(input("___"))
        if ask == 6:
            print(report())
            jjjj = input()
            if jjjj == "nothing":
                True
            else:
                off = True
                break

        elif ask == 7:
            print(total_cups)
            jjjj = input()
            if jjjj == "nothing":
                True
            else:
                off = True
                break

        elif ask == 8:
            watter += int(input("how much watter?"))
            milk += int(input("how much milk?"))
            coffee += int(input("how much cofee?"))

        elif ask == 9:
            print(f"the total earnings is {total}")
            off = True
            break

        elif ask == 5:
            end_session = True
            break

        
        elif ask == 1 or ask == 2 or ask == 3:
            if ask == 1:
                varient = "Espresso"
            elif ask == 2:
                varient = "Latte"
            elif ask == 3:
                varient = "Cappuccino"


            if not coffee_menu[varient]["water"] < watter:
                print("sorry some ingredients is insufficient.")
                off = True
                break
            else:
                ten, fifty, hundred = map(int, input("ten fifty hundred (separated by space): ").split())
            
                fund = (ten * 10) + (fifty * 50) + (hundred * 100)
                
                

            if fund < coffee_menu[varient]["money"]:
                print("insert more money")
                ten, fifty, hundred = map(int, input("ten fifty hundred (separated by space): ").split())
            
                fund += (ten * 10) + (fifty * 50) + (hundred * 100)

            
            total_cups[varient] += 1
            money += coffee_menu[varient]["money"]
            watter -= coffee_menu[varient]["water"]
            milk -= coffee_menu[varient]["milk"]
            coffee -= coffee_menu[varient]["coffee"]
            refund = fund - coffee_menu[varient]["money"]
            total += coffee_menu[varient]["money"]
            if refund > 0:
                print(f"take your money INR{refund} back\nand enjoy the {varient}")
            else:
                print(f"enjoy your {varient}")
                off = True
        
    






        
        



























