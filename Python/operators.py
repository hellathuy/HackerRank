# Given the meal price (base cost of a meal), 
# tip percent (the percentage of the meal price being added as tip), 
# and tax percent (the percentage of the meal price being added as tax) for a meal, 
# find and print the meal's total cost.

def get_total_cost_of_meal():
    
    #original meal price
    meal_cost = float(raw_input())
    
    #tip percentage
    tip_percent = int(raw_input())
    
    #tax percentage
    tax_percent = int(raw_input())

    tip = meal_cost * (tip_percent/float(100)) #calculate tip
    tax = meal_cost * (tax_percent/float(100)) #caclulate tax

    #cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tip + tax))
    
    return str(total_cost)

print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
