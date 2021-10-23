# Chris, Katie, Eleni
# CS-151
# 10/21/21
# Lab 5

room_count = 0
total_cost = float(0)
while room_count < 5:
    length = input("Enter the length of the floor ")
    length = float(length)
    width = input("Enter the width of the floor ")
    width = float(width)
    floor_type = input("Enter the type of floor ")
    floor_type = floor_type.strip().lower()
    if floor_type == 'hardwood':
        price_per_unit = 1.39
    elif floor_type == 'carpet':
        price_per_unit = 3.99
    elif floor_type == 'tile':
        price_per_unit = 4.99
    else:
        print ("invalid floor type price will be set to 0 for that room")
        price_per_unit = 0


    def area(length,width):
        return float(length * width * price_per_unit)
    price = area(length,width)

    room_count += 1
    print ("the price for room ", room_count," is %.2f " %price )
    total_cost += price

print("The total cost of the 5 rooms is $",total_cost)




