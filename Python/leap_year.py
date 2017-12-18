def is_leap(year):
    leap = False
    
    four = year%4
    hundred = year%100
    four_hundred = year%400
    
    if four == 0 and hundred == 0 and four_hundred == 0:
        leap = True
    elif four == 0 and hundred == 0 and four_hundred != 0:
        leap = False  
    elif four == 0:  
        leap = True
    else: 
        leap = False

    return leap
