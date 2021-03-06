# Programmers: Katie, Chris, Eleni
# CS151, Dr. Rajeev
# Date: October 21, 2021
# Lab 5
# Program Inputs: Room dimensions (length + width) for each room.
# Program Outputs: Cost of floors redone for each room.

# ask user to enter a room 1-5.

# condtionals: outside if statement for room # and cost calculation on the inside.
# NOTE: conditionals are the same for all rooms.

def getFloorLength():
    return float(input("  Floor length (L): "))

def getFloorWidth():
    return float(input("  Floor width  (W): "))

def getFloorType():
    return input("  Floor type   (T): ").strip().lower()

def computeArea(length, width):
    return float(length * width * price_per_unit)

total_cost = float(0)

room_count = 0
while room_count < 5:
    length = getFloorLength()
    width = getFloorWidth()
    type = getFloorType()
    if type == 'hardwood':
        price_per_unit = 1.39
    elif type == 'carpet':
        price_per_unit = 3.99
    elif type == 'tile':
        price_per_unit = 4.99
    else:
        print("invalid floor type (price will be set to $0.00)")
        price_per_unit = 0

    price = computeArea(length, width)
    print (round(price, 2))

    room_count += 1
    print("the price for room ", room_count," is %.2f " %price )
    total_cost += price

print("The total cost of the 5 rooms is $", total_cost)
