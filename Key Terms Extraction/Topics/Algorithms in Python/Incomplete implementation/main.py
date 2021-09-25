def startswith_capital_counter(names):

    quantity = 0
    for name in names:        
        if name == name.title():
            quantity += 1    
       
    return quantity
